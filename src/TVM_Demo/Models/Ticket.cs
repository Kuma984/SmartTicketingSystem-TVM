using System;

namespace TVM_Demo.Models
{
    /// <summary>
    /// Represents an issued transit ticket containing a machine-readable barcode.
    /// </summary>
    public class Ticket
    {
        public int TicketID { get; set; }
        public int TransactionID { get; set; }
        public string BarcodeValue { get; set; } = string.Empty;
        public DateTime IssuedAt { get; set; } = DateTime.Now;

        /// <summary>
        /// Manual enhancement for Backward Engineering (Code-to-Model reflection).
        /// Validates that the ticket barcode conforms to the Code128 format required by station validators.
        /// </summary>
        public bool ValidateBarcode()
        {
            return !string.IsNullOrWhiteSpace(BarcodeValue) && BarcodeValue.StartsWith("TVM");
        }
    }
}
