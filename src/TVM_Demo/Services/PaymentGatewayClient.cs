using System;
using System.Threading;

namespace TVM_Demo.Services
{
    /// <summary>
    /// Simulates external Payment Gateway interactions (Credit Card authorization and Digital Wallet QR polling).
    /// Real banking integrations communicate over HTTPS with gateways like VNPay, MoMo, or Card Networks.
    /// </summary>
    public class PaymentGatewayClient
    {
        private static readonly Random _rnd = new Random();

        /// <summary>
        /// Simulates credit/debit card authorization over network.
        /// Configured with ~85% success rate to demonstrate both happy path and failure exceptions.
        /// </summary>
        public bool ChargeCard(decimal amount)
        {
            Thread.Sleep(800); // Simulate network latency to external banking server
            return _rnd.Next(100) < 85;
        }

        /// <summary>
        /// Generates a dynamic payment payload string encoded into the QR code.
        /// </summary>
        public string GenerateQRPayload(decimal amount, int destinationId)
        {
            return $"TVM|DEST{destinationId}|AMT{amount}|{Guid.NewGuid():N}".Substring(0, 30);
        }

        /// <summary>
        /// Simulates webhook / status polling for QR payment confirmation.
        /// </summary>
        public bool CheckQRPaymentStatus(string qrPayload)
        {
            Thread.Sleep(800); // Simulate network latency
            return _rnd.Next(100) < 85;
        }
    }
}
