namespace TVM_Demo
{
    partial class MainForm
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        private void InitializeComponent()
        {
            this.lblTitle = new System.Windows.Forms.Label();
            this.lblSubtitle = new System.Windows.Forms.Label();
            this.grpDestination = new System.Windows.Forms.GroupBox();
            this.lblFareDisplay = new System.Windows.Forms.Label();
            this.cmbDestination = new System.Windows.Forms.ComboBox();
            this.grpPayment = new System.Windows.Forms.GroupBox();
            this.rdoQR = new System.Windows.Forms.RadioButton();
            this.rdoCard = new System.Windows.Forms.RadioButton();
            this.btnBuy = new System.Windows.Forms.Button();
            this.btnCancel = new System.Windows.Forms.Button();
            this.grpOutput = new System.Windows.Forms.GroupBox();
            this.txtOutputReport = new System.Windows.Forms.RichTextBox();
            this.statusStrip = new System.Windows.Forms.StatusStrip();
            this.lblStatus = new System.Windows.Forms.ToolStripStatusLabel();
            this.grpDestination.SuspendLayout();
            this.grpPayment.SuspendLayout();
            this.grpOutput.SuspendLayout();
            this.statusStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // lblTitle
            // 
            this.lblTitle.BackColor = System.Drawing.Color.MidnightBlue;
            this.lblTitle.Dock = System.Windows.Forms.DockStyle.Top;
            this.lblTitle.Font = new System.Drawing.Font("Segoe UI", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.lblTitle.ForeColor = System.Drawing.Color.White;
            this.lblTitle.Location = new System.Drawing.Point(0, 0);
            this.lblTitle.Name = "lblTitle";
            this.lblTitle.Size = new System.Drawing.Size(860, 60);
            this.lblTitle.TabIndex = 0;
            this.lblTitle.Text = "  SMART TICKETING SYSTEM — TICKET VENDOR MACHINE";
            this.lblTitle.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // lblSubtitle
            // 
            this.lblSubtitle.AutoSize = true;
            this.lblSubtitle.Font = new System.Drawing.Font("Segoe UI", 10.5F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.lblSubtitle.ForeColor = System.Drawing.Color.DarkSlateGray;
            this.lblSubtitle.Location = new System.Drawing.Point(20, 72);
            this.lblSubtitle.Name = "lblSubtitle";
            this.lblSubtitle.Size = new System.Drawing.Size(460, 20);
            this.lblSubtitle.TabIndex = 1;
            this.lblSubtitle.Text = "Touchscreen Kiosk Interface | Metro & Bus Automated Fare Collection";
            // 
            // grpDestination
            // 
            this.grpDestination.Controls.Add(this.lblFareDisplay);
            this.grpDestination.Controls.Add(this.cmbDestination);
            this.grpDestination.Font = new System.Drawing.Font("Segoe UI", 11F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.grpDestination.Location = new System.Drawing.Point(24, 105);
            this.grpDestination.Name = "grpDestination";
            this.grpDestination.Size = new System.Drawing.Size(430, 115);
            this.grpDestination.TabIndex = 2;
            this.grpDestination.TabStop = false;
            this.grpDestination.Text = " Step 1: Select Route / Destination ";
            // 
            // lblFareDisplay
            // 
            this.lblFareDisplay.AutoSize = true;
            this.lblFareDisplay.Font = new System.Drawing.Font("Segoe UI Semibold", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.lblFareDisplay.ForeColor = System.Drawing.Color.DarkBlue;
            this.lblFareDisplay.Location = new System.Drawing.Point(15, 78);
            this.lblFareDisplay.Name = "lblFareDisplay";
            this.lblFareDisplay.Size = new System.Drawing.Size(125, 19);
            this.lblFareDisplay.TabIndex = 1;
            this.lblFareDisplay.Text = "Standard Fare: 0 VND";
            // 
            // cmbDestination
            // 
            this.cmbDestination.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbDestination.Font = new System.Drawing.Font("Segoe UI", 11.5F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.cmbDestination.FormattingEnabled = true;
            this.cmbDestination.Location = new System.Drawing.Point(15, 35);
            this.cmbDestination.Name = "cmbDestination";
            this.cmbDestination.Size = new System.Drawing.Size(395, 29);
            this.cmbDestination.TabIndex = 0;
            this.cmbDestination.SelectedIndexChanged += new System.EventHandler(this.cmbDestination_SelectedIndexChanged);
            // 
            // grpPayment
            // 
            this.grpPayment.Controls.Add(this.rdoQR);
            this.grpPayment.Controls.Add(this.rdoCard);
            this.grpPayment.Font = new System.Drawing.Font("Segoe UI", 11F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.grpPayment.Location = new System.Drawing.Point(24, 235);
            this.grpPayment.Name = "grpPayment";
            this.grpPayment.Size = new System.Drawing.Size(430, 110);
            this.grpPayment.TabIndex = 3;
            this.grpPayment.TabStop = false;
            this.grpPayment.Text = " Step 2: Choose Payment Mode ";
            // 
            // rdoQR
            // 
            this.rdoQR.AutoSize = true;
            this.rdoQR.Font = new System.Drawing.Font("Segoe UI", 11F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.rdoQR.Location = new System.Drawing.Point(20, 68);
            this.rdoQR.Name = "rdoQR";
            this.rdoQR.Size = new System.Drawing.Size(340, 24);
            this.rdoQR.TabIndex = 1;
            this.rdoQR.Text = "📱 Digital Wallet / Banking App QR Code (120s)";
            this.rdoQR.UseVisualStyleBackColor = true;
            // 
            // rdoCard
            // 
            this.rdoCard.AutoSize = true;
            this.rdoCard.Checked = true;
            this.rdoCard.Font = new System.Drawing.Font("Segoe UI", 11F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.rdoCard.Location = new System.Drawing.Point(20, 32);
            this.rdoCard.Name = "rdoCard";
            this.rdoCard.Size = new System.Drawing.Size(315, 24);
            this.rdoCard.TabIndex = 0;
            this.rdoCard.TabStop = true;
            this.rdoCard.Text = "💳 Credit / Debit Card (Tap or Insert Card)";
            this.rdoCard.UseVisualStyleBackColor = true;
            // 
            // btnBuy
            // 
            this.btnBuy.BackColor = System.Drawing.Color.SeaGreen;
            this.btnBuy.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnBuy.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnBuy.Font = new System.Drawing.Font("Segoe UI", 13F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.btnBuy.ForeColor = System.Drawing.Color.White;
            this.btnBuy.Location = new System.Drawing.Point(24, 365);
            this.btnBuy.Name = "btnBuy";
            this.btnBuy.Size = new System.Drawing.Size(260, 55);
            this.btnBuy.TabIndex = 4;
            this.btnBuy.Text = "✔ CONFIRM & PAY";
            this.btnBuy.UseVisualStyleBackColor = false;
            this.btnBuy.Click += new System.EventHandler(this.btnBuy_Click);
            // 
            // btnCancel
            // 
            this.btnCancel.BackColor = System.Drawing.Color.IndianRed;
            this.btnCancel.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnCancel.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnCancel.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.btnCancel.ForeColor = System.Drawing.Color.White;
            this.btnCancel.Location = new System.Drawing.Point(300, 365);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.Size = new System.Drawing.Size(154, 55);
            this.btnCancel.TabIndex = 5;
            this.btnCancel.Text = "✖ CANCEL";
            this.btnCancel.UseVisualStyleBackColor = false;
            this.btnCancel.Click += new System.EventHandler(this.btnCancel_Click);
            // 
            // grpOutput
            // 
            this.grpOutput.Controls.Add(this.txtOutputReport);
            this.grpOutput.Font = new System.Drawing.Font("Segoe UI", 11F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.grpOutput.Location = new System.Drawing.Point(475, 105);
            this.grpOutput.Name = "grpOutput";
            this.grpOutput.Size = new System.Drawing.Size(360, 315);
            this.grpOutput.TabIndex = 6;
            this.grpOutput.TabStop = false;
            this.grpOutput.Text = " Dispenser / Output Report ";
            // 
            // txtOutputReport
            // 
            this.txtOutputReport.BackColor = System.Drawing.Color.FloralWhite;
            this.txtOutputReport.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtOutputReport.Font = new System.Drawing.Font("Consolas", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.txtOutputReport.ForeColor = System.Drawing.Color.Black;
            this.txtOutputReport.Location = new System.Drawing.Point(3, 23);
            this.txtOutputReport.Name = "txtOutputReport";
            this.txtOutputReport.ReadOnly = true;
            this.txtOutputReport.Size = new System.Drawing.Size(354, 289);
            this.txtOutputReport.TabIndex = 0;
            this.txtOutputReport.Text = "Ready. Please select a destination and payment mode to issue ticket.";
            // 
            // statusStrip
            // 
            this.statusStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.lblStatus});
            this.statusStrip.Location = new System.Drawing.Point(0, 445);
            this.statusStrip.Name = "statusStrip";
            this.statusStrip.Size = new System.Drawing.Size(860, 24);
            this.statusStrip.TabIndex = 7;
            this.statusStrip.Text = "statusStrip1";
            // 
            // lblStatus
            // 
            this.lblStatus.Font = new System.Drawing.Font("Segoe UI", 9.5F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(260, 19);
            this.lblStatus.Text = "System Status: Online | Kiosk Terminal #TVM-01";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.WhiteSmoke;
            this.ClientSize = new System.Drawing.Size(860, 469);
            this.Controls.Add(this.statusStrip);
            this.Controls.Add(this.grpOutput);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.btnBuy);
            this.Controls.Add(this.grpPayment);
            this.Controls.Add(this.grpDestination);
            this.Controls.Add(this.lblSubtitle);
            this.Controls.Add(this.lblTitle);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Smart Ticketing System - TVM Demo";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.grpDestination.ResumeLayout(false);
            this.grpDestination.PerformLayout();
            this.grpPayment.ResumeLayout(false);
            this.grpPayment.PerformLayout();
            this.grpOutput.ResumeLayout(false);
            this.statusStrip.ResumeLayout(false);
            this.statusStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblTitle;
        private System.Windows.Forms.Label lblSubtitle;
        private System.Windows.Forms.GroupBox grpDestination;
        private System.Windows.Forms.ComboBox cmbDestination;
        private System.Windows.Forms.Label lblFareDisplay;
        private System.Windows.Forms.GroupBox grpPayment;
        private System.Windows.Forms.RadioButton rdoQR;
        private System.Windows.Forms.RadioButton rdoCard;
        private System.Windows.Forms.Button btnBuy;
        private System.Windows.Forms.Button btnCancel;
        private System.Windows.Forms.GroupBox grpOutput;
        private System.Windows.Forms.RichTextBox txtOutputReport;
        private System.Windows.Forms.StatusStrip statusStrip;
        private System.Windows.Forms.ToolStripStatusLabel lblStatus;
    }
}
