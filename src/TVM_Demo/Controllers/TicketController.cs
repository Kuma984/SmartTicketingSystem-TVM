using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using Microsoft.Data.SqlClient;
using TVM_Demo.Models;
using TVM_Demo.Services;

namespace TVM_Demo.Controllers
{
    /// <summary>
    /// Core Business Logic & Orchestration Controller for the Ticket Vendor Machine (TVM).
    /// Coordinates between Presentation Layer (UI), Domain Models, Database, and Payment Gateways.
    /// </summary>
    public class TicketController
    {
        private readonly string _connectionString;
        private readonly PaymentGatewayClient _gateway;

        public TicketController()
        {
            var configSetting = ConfigurationManager.ConnectionStrings["TVMConnectionString"];
            _connectionString = configSetting != null
                ? configSetting.ConnectionString
                : @"Data Source=(localdb)\MSSQLLocalDB;Initial Catalog=TVM_DB;Integrated Security=True;Encrypt=False;";

            _gateway = new PaymentGatewayClient();
        }

        /// <summary>
        /// Retrieves the list of active transit destinations from the database.
        /// Falls back to default station list if database is not yet initialized.
        /// </summary>
        public List<Destination> GetDestinations()
        {
            var list = new List<Destination>();

            try
            {
                using (var conn = new SqlConnection(_connectionString))
                {
                    conn.Open();
                    string query = "SELECT DestinationID, Name, Fare FROM Destinations ORDER BY DestinationID ASC";
                    using (var cmd = new SqlCommand(query, conn))
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            list.Add(new Destination
                            {
                                DestinationID = reader.GetInt32(0),
                                Name = reader.GetString(1),
                                Fare = reader.GetDecimal(2)
                            });
                        }
                    }
                }
            }
            catch (Exception)
            {
                // Fallback default destinations for demo robustness
                list = new List<Destination>
                {
                    new Destination { DestinationID = 1, Name = "Ben Thanh Market (Metro Station 1)", Fare = 7000 },
                    new Destination { DestinationID = 2, Name = "Suoi Tien Theme Park (Metro Station 14)", Fare = 12000 },
                    new Destination { DestinationID = 3, Name = "Tan Son Nhat International Airport", Fare = 20000 },
                    new Destination { DestinationID = 4, Name = "Saigon Hi-Tech Park (SHTP)", Fare = 15000 }
                };
            }

            return list;
        }

        /// <summary>
        /// Orchestrates the entire ticket purchase transaction.
        /// 1. Authorizes payment via PaymentGatewayClient
        /// 2. Records transaction in database table 'Transactions'
        /// 3. Upon success, generates barcode and records ticket in 'Tickets'
        /// </summary>
        public (bool success, string message, string? barcode, int transactionId) ProcessPurchase(
            int destinationId, decimal fare, string paymentMethod)
        {
            // Step 1: Execute simulated payment authorization
            bool paid = paymentMethod == "CreditCard"
                ? _gateway.ChargeCard(fare)
                : _gateway.CheckQRPaymentStatus(_gateway.GenerateQRPayload(fare, destinationId));

            int transactionId = 0;
            string? barcode = null;

            try
            {
                using (var conn = new SqlConnection(_connectionString))
                {
                    conn.Open();

                    // Step 2: Insert into Transactions table with parameterized query
                    string insertTxnSql = @"
                        INSERT INTO Transactions (DestinationID, PaymentMethod, Status, Amount, CreatedAt)
                        OUTPUT INSERTED.TransactionID
                        VALUES (@DestId, @Method, @Status, @Amount, GETDATE());";

                    using (var cmd = new SqlCommand(insertTxnSql, conn))
                    {
                        cmd.Parameters.Add("@DestId", SqlDbType.Int).Value = destinationId;
                        cmd.Parameters.Add("@Method", SqlDbType.NVarChar, 20).Value = paymentMethod;
                        cmd.Parameters.Add("@Status", SqlDbType.NVarChar, 20).Value = paid ? "Success" : "Failed";
                        cmd.Parameters.Add("@Amount", SqlDbType.Decimal).Value = fare;

                        object result = cmd.ExecuteScalar();
                        if (result != null && int.TryParse(result.ToString(), out int id))
                        {
                            transactionId = id;
                        }
                    }

                    // Step 3: If payment succeeded, issue Ticket and print barcode
                    if (paid && transactionId > 0)
                    {
                        barcode = $"TVM{transactionId:D8}";
                        string insertTicketSql = @"
                            INSERT INTO Tickets (TransactionID, BarcodeValue, IssuedAt)
                            VALUES (@TxnId, @Barcode, GETDATE());";

                        using (var ticketCmd = new SqlCommand(insertTicketSql, conn))
                        {
                            ticketCmd.Parameters.Add("@TxnId", SqlDbType.Int).Value = transactionId;
                            ticketCmd.Parameters.Add("@Barcode", SqlDbType.NVarChar, 50).Value = barcode;
                            ticketCmd.ExecuteNonQuery();
                        }
                    }
                }
            }
            catch (Exception)
            {
                // If DB connection fails, generate demo transaction ID for presentation
                if (transactionId == 0)
                {
                    transactionId = new Random().Next(1000, 9999);
                }
                if (paid && barcode == null)
                {
                    barcode = $"TVM{transactionId:D8}";
                }
            }

            if (!paid)
            {
                return (false, "Payment was declined by bank or timed out. Transaction cancelled.", null, transactionId);
            }

            return (true, "Payment authorized successfully! Ticket issued.", barcode, transactionId);
        }
    }
}
