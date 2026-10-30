# Smart Ticketing System (Ticket Vendor Machine - TVM)

## Course: Software Engineering Group Assignment 1 (Sem 1_2627)
- **Instructor:** P.T.K.Trung (`phamthaikytrung@tdtu.edu.vn`)
- **GitHub Repository:** https://github.com/Kuma984/SmartTicketingSystem-TVM
- **Team Members (3 Students):**
  - **524K0021 - Trinh Duc Long** (Team Leader, Architecture & C# Backend)
  - **523V0016 - Vo Thi My Duyen** (Requirements Engineering & UML Modeling)
  - **524K0015 - Tran Hoang Anh** (UI/UX Kiosk Wireframes & QA Testing)

---

## 1. Project Overview
This repository contains the complete engineering deliverables for the automated **Ticket Vendor Machine (TVM)**, a subsystem of the city-wide Smart Ticketing System for public transit (Bus, MRT, Metro).

The system allows passengers to:
1. Select their destination station from a list of fixed routes.
2. Select preferred payment mode: **Credit/Debit Card** or **Digital Wallet (Dynamic QR Code)**.
3. Automatically charge the account via Payment Gateway authorization.
4. Issue a physical ticket with a Code128 machine-readable barcode.

---

## 2. Repository Structure
```
/SmartTicketingSystem-TVM
├── docs/
│   ├── 524K0021_TrinhDucLong.docx     # Comprehensive Word Report
│   ├── A1_Team_Workbook.xlsx          # Requirements, Q&A, and Tracking Workbook
│   ├── TVM_DB.sql                     # MSSQL Database Schema and Seed Data
│   └── readme.txt                     # Submission details and contribution
└── src/
    ├── SmartTicketingSystem.sln       # Visual Studio Solution
    └── TVM_Demo/                      # C# Windows Forms Application
        ├── Models/                    # Domain Model (Destination, Transaction, Ticket)
        ├── Services/                  # Simulated Banking Gateway Client
        ├── Controllers/               # TicketController Orchestration
        ├── MainForm.cs                # Kiosk Touchscreen Presentation
        └── DomainModel.cd             # Visual Studio Class Designer Diagram
```

---

## 3. Quick Start
1. **Database:** Open `docs/TVM_DB.sql` in SQL Server Management Studio (SSMS) or Visual Studio SQL Object Explorer and run against `(localdb)\MSSQLLocalDB` or your SQL Server instance.
2. **Application:** Open `src/SmartTicketingSystem.sln` in Visual Studio, build the solution, and press `F5` to run.
