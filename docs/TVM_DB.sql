-- =========================================================================
-- Smart Ticketing System (Ticket Vendor Machine - TVM) Database Schema
-- Course: Software Engineering Group Assignment 1 - Sem 1_2627
-- Instructor: P.T.K.Trung (phamthaikytrung@tdtu.edu.vn)
-- =========================================================================

IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'TVM_DB')
BEGIN
    CREATE DATABASE TVM_DB;
END
GO

USE TVM_DB;
GO

-- 1. Table: Destinations
-- Stores available transit stations and fixed route fares (DR4: integer/flat currency unit)
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Destinations')
BEGIN
    CREATE TABLE Destinations (
        DestinationID INT PRIMARY KEY IDENTITY(1,1),
        Name NVARCHAR(100) NOT NULL,
        Fare DECIMAL(10,0) NOT NULL
    );
END
GO

-- 2. Table: Transactions
-- Records all initiated payment attempts (DR1: 1-year audit compliance, FR8: transaction logging)
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Transactions')
BEGIN
    CREATE TABLE Transactions (
        TransactionID INT PRIMARY KEY IDENTITY(1,1),
        DestinationID INT NOT NULL,
        PaymentMethod NVARCHAR(20) NOT NULL,   -- 'CreditCard' or 'DigitalWallet'
        Status NVARCHAR(20) NOT NULL,          -- 'Success' or 'Failed'
        Amount DECIMAL(10,0) NOT NULL,
        CreatedAt DATETIME NOT NULL DEFAULT GETDATE(),
        CONSTRAINT FK_Transactions_Destinations FOREIGN KEY (DestinationID)
            REFERENCES Destinations(DestinationID)
    );
END
GO

-- 3. Table: Tickets
-- Stores issued physical/digital tickets linked to successful transactions (DR3: Code128 barcode)
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Tickets')
BEGIN
    CREATE TABLE Tickets (
        TicketID INT PRIMARY KEY IDENTITY(1,1),
        TransactionID INT NOT NULL,
        BarcodeValue NVARCHAR(50) NOT NULL,
        IssuedAt DATETIME NOT NULL DEFAULT GETDATE(),
        CONSTRAINT FK_Tickets_Transactions FOREIGN KEY (TransactionID)
            REFERENCES Transactions(TransactionID)
    );
END
GO

-- 4. Seed Initial Station Data
IF NOT EXISTS (SELECT * FROM Destinations)
BEGIN
    INSERT INTO Destinations (Name, Fare) VALUES
    (N'Ben Thanh Market (Metro Station 1)', 7000),
    (N'Suoi Tien Theme Park (Metro Station 14)', 12000),
    (N'Tan Son Nhat International Airport', 20000),
    (N'Saigon Hi-Tech Park (SHTP Station)', 15000);
END
GO

-- Verification Query
SELECT * FROM Destinations;
SELECT * FROM Transactions;
SELECT * FROM Tickets;
GO
