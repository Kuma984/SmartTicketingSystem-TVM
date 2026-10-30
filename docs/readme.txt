================================================================================
SOFTWARE ENGINEERING GROUP ASSIGNMENT 1: SMART TICKETING SYSTEM (TVM)
Course: Software Engineering - Sem 1_2627
Instructor: P.T.K.Trung (phamthaikytrung@tdtu.edu.vn)
Team: Group 02 (3 Members)
================================================================================

1. PROJECT LINKS
--------------------------------------------------------------------------------
- GitHub Repository : https://github.com/Kuma984/SmartTicketingSystem-TVM
- UI/UX Wireframes  : Detailed Kiosk Specifications (S01-S05) documented in Report Section 4.1
- Demo Application  : Executable C# WinForms Prototype in /src/SmartTicketingSystem.sln

2. REPOSITORY & PROJECT STRUCTURE
--------------------------------------------------------------------------------
/SmartTicketingSystem-TVM
  |-- /docs
  |     |-- 524K0021_TrinhDucLong.docx     <- Comprehensive Final Report
  |     |-- A1_Team_Workbook.xlsx           <- Process & Tracking Workbook
  |     |-- TVM_DB.sql                      <- Database Setup & Seed Script
  |     |-- readme.txt                      <- Submission Metadata & Contribution
  |-- /src
        |-- SmartTicketingSystem.sln        <- Visual Studio Solution
        |-- /TVM_Demo                       <- C# WinForms Application Project
              |-- App.config                <- Connection Strings Configuration
              |-- Program.cs                <- Application Entry Point
              |-- MainForm.cs               <- Kiosk Presentation Layer
              |-- DomainModel.cd            <- VS Class Designer Model
              |-- /Models                   <- Domain Entities (Destination, Transaction, Ticket)
              |-- /Services                 <- External Gateway Client Simulation
              |-- /Controllers              <- Business Logic Controller

3. DATABASE SETUP INSTRUCTIONS
--------------------------------------------------------------------------------
Requirements: Microsoft SQL Server or SQL Server LocalDB (installed with Visual Studio).
Steps:
1. Open SQL Server Management Studio (SSMS) or Visual Studio SQL Server Object Explorer.
2. Connect to your instance:
   - For LocalDB: (localdb)\MSSQLLocalDB
   - For SQL Server: localhost or .\SQLEXPRESS
3. Open and execute the script:
   /docs/TVM_DB.sql
4. Verify that database 'TVM_DB' is created with 3 tables (Destinations, Transactions, Tickets).
5. If using a custom SQL Server instance name or SQL authentication, update the connection
   string inside /src/TVM_Demo/App.config accordingly.

4. APPLICATION EXECUTION INSTRUCTIONS
--------------------------------------------------------------------------------
1. Open /src/SmartTicketingSystem.sln in Visual Studio (2022 / 2026).
2. Set 'TVM_Demo' as the Startup Project.
3. Build the solution (Ctrl + Shift + B).
4. Run the application (F5 or Debug -> Start Without Debugging).
5. Purchase Flow:
   - Select a destination from the dropdown.
   - Choose payment mode: 'Credit / Debit Card' or 'Digital Wallet QR'.
   - Click '[ CONFIRM & PAY ]'.
   - The Dispenser panel displays the formatted ticket with unique Barcode and logs the record.

5. TEAM MEMBERS & PERCENT CONTRIBUTION
--------------------------------------------------------------------------------
| No. | Student ID | Full Name        | Role & Main Tasks                          | % Contribution |
|-----|------------|------------------|--------------------------------------------|----------------|
| 1   | 524K0021   | Trinh Duc Long   | Team Leader, Architecture, C# Backend & DB | 34%            |
| 2   | 523V0016   | Vo Thi My Duyen  | Requirements Engineering & UML Modeling    | 33%            |
| 3   | 524K0015   | Tran Hoang Anh   | UI/UX Wireframes, Testing & Documentation   | 33%            |
--------------------------------------------------------------------------------
TOTAL CONTRIBUTION: 100%
================================================================================
