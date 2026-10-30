using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using TVM_Demo.Controllers;
using TVM_Demo.Models;

namespace TVM_Demo
{
    public partial class MainForm : Form
    {
        private readonly TicketController _controller;
        private List<Destination> _destinations = new List<Destination>();

        public MainForm()
        {
            InitializeComponent();
            _controller = new TicketController();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            LoadDestinations();
        }

        private void LoadDestinations()
        {
            try
            {
                _destinations = _controller.GetDestinations();
                cmbDestination.DataSource = _destinations;
                cmbDestination.DisplayMember = "Name";
                cmbDestination.ValueMember = "DestinationID";

                if (_destinations.Count > 0)
                {
                    cmbDestination.SelectedIndex = 0;
                    UpdateFareDisplay();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error initializing destinations: {ex.Message}", "System Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void cmbDestination_SelectedIndexChanged(object sender, EventArgs e)
        {
            UpdateFareDisplay();
        }

        private void UpdateFareDisplay()
        {
            if (cmbDestination.SelectedItem is Destination selected)
            {
                lblFareDisplay.Text = $"Standard Fare: {selected.Fare:N0} VND";
            }
        }

        private void btnBuy_Click(object sender, EventArgs e)
        {
            if (cmbDestination.SelectedItem is not Destination selected)
            {
                MessageBox.Show("Please select a transit destination.", "Validation Notice",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            string paymentMethod = rdoCard.Checked ? "CreditCard" : "DigitalWallet";

            // Visual feedback of in-progress transaction
            btnBuy.Enabled = false;
            btnCancel.Enabled = false;
            lblStatus.Text = paymentMethod == "CreditCard"
                ? "Connecting to Payment Gateway... Please tap or insert card."
                : "Generating dynamic QR code... Awaiting mobile app scan.";
            txtOutputReport.ForeColor = Color.DarkSlateGray;
            txtOutputReport.Text = $"[PROCESSING PAYMENT]\n" +
                                   $"Destination: {selected.Name}\n" +
                                   $"Amount: {selected.Fare:N0} VND\n" +
                                   $"Method: {paymentMethod}\n" +
                                   $"Please follow on-screen instructions...";
            Application.DoEvents();

            // Execute purchase flow
            var (success, message, barcode, txnId) = _controller.ProcessPurchase(
                selected.DestinationID, selected.Fare, paymentMethod);

            btnBuy.Enabled = true;
            btnCancel.Enabled = true;

            var sb = new StringBuilder();
            if (success)
            {
                lblStatus.Text = "Status: Ticket Issued Successfully! | Transaction Complete.";
                txtOutputReport.ForeColor = Color.DarkGreen;

                sb.AppendLine("========================================");
                sb.AppendLine("         SMART METRO TRANSIT TICKET     ");
                sb.AppendLine("========================================");
                sb.AppendLine($"Ticket ID    : TKT-{txnId:D6}");
                sb.AppendLine($"Txn ID       : TXN-{txnId:D6}");
                sb.AppendLine($"Destination  : {selected.Name}");
                sb.AppendLine($"Payment Mode : {paymentMethod}");
                sb.AppendLine($"Total Fare   : {selected.Fare:N0} VND");
                sb.AppendLine($"Issued At    : {DateTime.Now:yyyy-MM-dd HH:mm:ss}");
                sb.AppendLine($"Terminal     : TVM-Kiosk-01");
                sb.AppendLine("----------------------------------------");
                sb.AppendLine($"BARCODE      : ||| {barcode} |||");
                sb.AppendLine("----------------------------------------");
                sb.AppendLine("    Valid for single trip entry today   ");
                sb.AppendLine("========================================");
            }
            else
            {
                lblStatus.Text = "Status: Transaction Failed / Declined.";
                txtOutputReport.ForeColor = Color.Crimson;

                sb.AppendLine("========================================");
                sb.AppendLine("         TRANSACTION DECLINED           ");
                sb.AppendLine("========================================");
                sb.AppendLine($"Status       : FAILED");
                sb.AppendLine($"Txn Reference: TXN-{txnId:D6}");
                sb.AppendLine($"Reason       : {message}");
                sb.AppendLine($"Timestamp    : {DateTime.Now:yyyy-MM-dd HH:mm:ss}");
                sb.AppendLine("----------------------------------------");
                sb.AppendLine("No funds were deducted. Please try again");
                sb.AppendLine("or contact station customer service.");
                sb.AppendLine("========================================");
            }

            txtOutputReport.Text = sb.ToString();
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            if (cmbDestination.Items.Count > 0)
            {
                cmbDestination.SelectedIndex = 0;
            }
            rdoCard.Checked = true;
            txtOutputReport.ForeColor = Color.Black;
            txtOutputReport.Text = "Transaction cancelled by user. Session reset to idle.";
            lblStatus.Text = "System Status: Online | Kiosk Terminal #TVM-01";
        }
    }
}
