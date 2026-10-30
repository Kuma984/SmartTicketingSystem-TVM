import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
wb.remove(wb.active)

# Color palettes
header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
accent_fill = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
title_font = Font(name="Calibri", size=14, bold=True, color="1F497D")
bold_font = Font(name="Calibri", size=11, bold=True)
regular_font = Font(name="Calibri", size=11)
center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
left_align = Alignment(horizontal="left", vertical="center", wrap_text=True)
thin_border = Border(
    left=Side(style='thin', color='BFBFBF'),
    right=Side(style='thin', color='BFBFBF'),
    top=Side(style='thin', color='BFBFBF'),
    bottom=Side(style='thin', color='BFBFBF')
)

def style_table(ws, start_row, headers, rows):
    ws.row_dimensions[start_row].height = 28
    for col_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=start_row, column=col_idx, value=h)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = center_align
        cell.border = thin_border
    
    current_row = start_row + 1
    for r in rows:
        ws.row_dimensions[current_row].height = 22
        for col_idx, val in enumerate(r, 1):
            cell = ws.cell(row=current_row, column=col_idx, value=val)
            cell.font = regular_font
            cell.border = thin_border
            if isinstance(val, (int, float)) or (isinstance(val, str) and (val.endswith('%') or val.startswith('Q') or val.startswith('FR') or val.startswith('NFR') or val.startswith('DR') or val.startswith('UC'))):
                cell.alignment = center_align
            else:
                cell.alignment = left_align
        current_row += 1

    for col in ws.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = 0
        for cell in col:
            val_str = str(cell.value or '')
            if len(val_str) > max_len:
                max_len = len(val_str)
        ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 48)

# -------------------------------------------------------------
# 1. SHEET: Team (3 Members)
# -------------------------------------------------------------
ws_team = wb.create_sheet("Team")
ws_team["A1"] = "Smart Ticketing System (TVM) - Team & Contribution"
ws_team["A1"].font = title_font
ws_team["A2"] = "Group: 02 (3 Students) | GitHub: https://github.com/Kuma984/SmartTicketingSystem-TVM"
ws_team["A2"].font = bold_font

team_headers = ["Member", "Name", "Student ID", "Role / Main Responsibility", "% Contribution", "Commits", "Check"]
team_rows = [
    ["Member 1", "Trinh Duc Long", "524K0021", "Team Leader, Architecture Design, C# WinForms & MSSQL Backend", "34%", 18, "Valid"],
    ["Member 2", "Vo Thi My Duyen", "523V0016", "Requirements Engineering, Clarification Q&A, UML Modeling", "33%", 16, "Valid"],
    ["Member 3", "Tran Hoang Anh", "524K0015", "UI/UX Touchscreen Wireframes, Copilot Prompt Log & QA Testing", "33%", 15, "Valid"],
    ["TOTAL", "", "", "Total Group Contribution", "100%", 49, "100% OK"]
]
style_table(ws_team, 4, team_headers, team_rows)

# -------------------------------------------------------------
# 2. SHEET: Clarification Q&A (Task 1)
# -------------------------------------------------------------
ws_qa = wb.create_sheet("Clarification Q&A")
ws_qa["A1"] = "Task 1: Clarification Q&A — Uncovering Hidden Complexities"
ws_qa["A1"].font = title_font

qa_headers = ["Q ID", "Area", "Ambiguity Found in Problem Statement", "Clarifying Question to Stakeholder", "Stakeholder", "Assumed Answer (Logical)", "Rationale and Impact on Design", "Req ID", "Status"]
qa_rows = [
    ["Q01", "Payment", "Payment timeout or card declined by bank network.", "Should TVM retry automatically or abort the session immediately?", "Transit Operator", "Retry once after 5s; if failed again, cancel transaction, display error, no fare deducted.", "Prevents kiosk lock-up and eliminates risk of double-charging customer account.", "FR7, NFR2", "Approved"],
    ["Q02", "Payment", "Lifespan of dynamic Digital Wallet QR code.", "How long is the generated QR code valid before session expiration?", "Payment Partner", "QR code expires in 120 seconds with countdown display. Session resets to Idle if unpaid.", "Releases reserved state, prevents kiosk stagnation during peak hours.", "FR5, NFR3", "Approved"],
    ["Q03", "Ticketing", "Multi-ticket single transaction purchase.", "Can passengers purchase multiple tickets simultaneously in v1?", "Product Owner", "Single-ticket purchase per transaction in v1 scope. Multi-ticket planned for v2.", "Simplifies transaction state machine and UI workflow for prototype deadline.", "FR2, DR4", "Approved"],
    ["Q04", "Hardware", "Printer paper-out after payment confirmation.", "Does TVM issue automatic refund or notify station staff?", "Station Staff", "No auto refund. TVM writes ERR_PAPER_OUT log and displays audit code for staff desk assist.", "Preserves accounting integrity; defines hardware exception boundary.", "FR8, DR1", "Approved"],
    ["Q05", "Fares", "Fare structure (zone-based vs distance vs flat-rate).", "How is ticket price calculated for selected route?", "Transit Authority", "Fixed flat route fare stored in lookup table 'Destinations'. No dynamic pricing in v1.", "Reduces domain complexity and streamlines database schema.", "FR1, DR4", "Approved"],
    ["Q06", "Reliability", "Acceptable kiosk UI response time benchmark.", "What is the maximum allowed delay between pressing Start and route menu display?", "UX Lead", "Under 1.0 second in 95% of cases measured over 1,000 transactions.", "Provides a quantitative, testable non-functional requirement.", "NFR3", "Approved"],
    ["Q07", "Security", "Cardholder data storage constraints on kiosk.", "Does TVM persist raw credit card PAN / CVV details?", "Security Officer", "TVM never stores raw cardholder data. All charges use tokenized HTTPS gateway APIs.", "Fulfills PCI-DSS Level 1 compliance and shields kiosk from data breaches.", "NFR5, DR2", "Approved"],
    ["Q08", "Kiosk UX", "Passenger abandons session mid-purchase.", "How does kiosk handle abandoned screens without user input?", "Operations", "All intermediate screens feature a 30s inactivity timer, reverting to Welcome screen.", "Avoids stalled kiosks in stations and protects customer privacy.", "FR9, NFR6", "Approved"]
]
style_table(ws_qa, 3, qa_headers, qa_rows)

# -------------------------------------------------------------
# 3. SHEET: Requirements (Task 2)
# -------------------------------------------------------------
ws_req = wb.create_sheet("Requirements")
ws_req["A1"] = "Task 2: Requirements Specification (FR, NFR, DR)"
ws_req["A1"].font = title_font

req_headers = ["ID", "Requirement Description", "Type", "Category", "Measurable Metric / Fit Criterion", "Measurement Method", "Priority", "Use Case", "Source"]
req_rows = [
    ["FR1", "The system shall display a list of all available transit destinations and fares upon pressing Start.", "Functional", "UI Display", "Display within 1.0s", "Automated UI timer log", "High", "UC01", "Q05, Q06"],
    ["FR2", "The system shall allow passenger to select exactly one destination per transaction.", "Functional", "Selection", "Single route selection validation", "Functional testing", "High", "UC01", "Q03"],
    ["FR3", "The system shall provide payment mode options: Credit/Debit Card and Digital Wallet QR.", "Functional", "Payment Mode", "2 radio/button choices displayed", "GUI test verification", "High", "UC01", "Problem Stmt"],
    ["FR4", "If Credit Card is selected, system shall prompt card insertion/tap and charge fare via Payment Gateway.", "Functional", "Payment Charge", "Gateway token charge protocol", "Gateway mock test", "High", "UC02", "Q01, Q07"],
    ["FR5", "If Digital Wallet is selected, system shall display dynamic QR code with 120s countdown timer.", "Functional", "QR Payment", "120s timer countdown accuracy +/-0.5s", "Timer stopwatch test", "High", "UC03", "Q02"],
    ["FR6", "Upon confirmed payment, system shall print a paper ticket containing a Code128 barcode.", "Functional", "Ticketing", "Barcode generated matching TVM{TxnId:D8}", "Barcode scanner scan", "High", "UC01", "Problem Stmt"],
    ["FR7", "If payment is declined or times out, system shall display error and reset without issuing ticket.", "Functional", "Exception", "Prompt error within 2s, 0 ticket issued", "Simulated decline test", "High", "UC04", "Q01, Q02"],
    ["FR8", "The system shall log every transaction (success/failure) in database with timestamp, fare, status.", "Functional", "Audit", "100% of attempts stored in Transactions table", "Database SQL query check", "High", "UC01, UC04", "Q04, DR1"],
    ["NFR1", "The system shall achieve 99.5% crash-free transaction completion rate.", "Non-Functional", "Reliability", "99.5% success over 1,000 test transactions", "Stress load execution", "High", "UC01", "Standard"],
    ["NFR2", "Payment gateway connection timeouts shall be caught within 3.0 seconds.", "Non-Functional", "Reliability", "Timeout limit = 3.0s max delay", "Network interruption test", "High", "UC04", "Q01"],
    ["NFR3", "Destination menu shall render within 1.0s of pressing Start in 95% of cases.", "Non-Functional", "Performance", "Latency <= 1,000ms (95th percentile)", "Stopwatch & telemetry", "Medium", "UC01", "Q06"],
    ["NFR4", "Paper ticket shall be issued within 5.0s of payment authorization confirmation.", "Non-Functional", "Performance", "Dispense delay <= 5.0s", "Kiosk hardware timer", "Medium", "UC01", "Standard"],
    ["NFR5", "No raw credit card PAN or CVV data shall be persisted in kiosk storage.", "Non-Functional", "Security", "0 raw card records in DB / logs (PCI-DSS)", "Security code scan & DB audit", "High", "UC02", "Q07, DR2"],
    ["NFR6", "First-time passenger shall complete purchase flow within 45 seconds.", "Non-Functional", "Usability", "Average completion time <= 45s, <= 1 error", "5-user testing trial", "Medium", "UC01", "Q08"],
    ["DR1", "All transaction logs must be retained for at least 1 year for audit and reconciliation.", "Domain", "Compliance", "Retention period >= 365 days in MSSQL", "Database purge policy audit", "High", "UC01, UC04", "Transit Regs"],
    ["DR2", "Card payment processing must adhere to PCI-DSS Level 1 tokenization standards.", "Domain", "Security", "Tokenized API payloads only", "Security compliance check", "High", "UC02", "PCI-DSS"],
    ["DR3", "Printed tickets must encode standard Code128 machine-readable barcode.", "Domain", "Standard", "Code128 symbology parsable by turnstiles", "Optical scanner verification", "High", "UC01", "Transit Standard"],
    ["DR4", "Fare amounts must be stored in whole integer currency units (VND, no decimals).", "Domain", "Financial", "Data type DECIMAL(10,0) without fractions", "Schema verification", "High", "UC01", "State Bank VND"]
]
style_table(ws_req, 3, req_headers, req_rows)

# -------------------------------------------------------------
# 4. SHEET: Use Cases (Task 3)
# -------------------------------------------------------------
ws_uc = wb.create_sheet("Use Cases")
ws_uc["A1"] = "Task 3: Use Case Register"
ws_uc["A1"].font = title_font

uc_headers = ["ID", "Use Case Name", "Primary Actor", "Short Description", "Related Requirement IDs", "Description Written?", "In Diagrams?", "Owner"]
uc_rows = [
    ["UC01", "Buy a Ticket", "Passenger", "Primary flow: Select route, pay, receive printed transit ticket.", "FR1-FR8, NFR1, NFR3, NFR4", "Yes (Detailed)", "Yes (All)", "Vo Thi My Duyen"],
    ["UC02", "Pay by Credit Card", "Passenger", "<<include>> of UC01: Authenticate card and charge via gateway.", "FR3, FR4, NFR5, DR2", "Yes (Detailed)", "Yes (All)", "Trinh Duc Long"],
    ["UC03", "Pay by Digital Wallet", "Passenger", "<<include>> of UC01: Generate dynamic QR code, poll payment.", "FR3, FR5, NFR3", "Yes (Detailed)", "Yes (All)", "Tran Hoang Anh"],
    ["UC04", "Handle Payment Failure", "Passenger / Gateway", "<<extend>> of UC01: Triggered when card declined or QR expired.", "FR7, FR8, NFR2", "Yes (Detailed)", "Yes (All)", "Vo Thi My Duyen"],
    ["UC05", "Report Hardware Fault", "Maintenance Staff", "<<extend>> of UC01: Triggered upon printer paper-out or jam.", "FR8, DR1", "Yes (Detailed)", "Yes (Activity/State)", "Trinh Duc Long"]
]
style_table(ws_uc, 3, uc_headers, uc_rows)

# -------------------------------------------------------------
# 5. SHEET: Consistency Check (Task 5 / 3.4)
# -------------------------------------------------------------
ws_cc = wb.create_sheet("Consistency Check")
ws_cc["A1"] = "Model Consistency Check (Task 5 / Report 3.4)"
ws_cc["A1"].font = title_font

cc_headers = ["#", "Consistency Check Criteria", "Diagrams Involved", "Status", "Notes / Justification"]
cc_rows = [
    [1, "Every use case in diagram has a description, and every description is in diagram", "Use Case Diagram / UC Descriptions", "Passed", "All 5 use cases (UC01-UC05) match 100%."],
    [2, "Every step of main flow appears in activity diagram", "UC Descriptions / Activity Diagram", "Passed", "Start -> Route -> Payment -> Verification -> Print matches exact flow."],
    [3, "Objects and messages in sequence diagram exist as classes and methods in class diagram", "Sequence Diagram / Class Diagram", "Passed", "TicketController.ProcessPurchase(), PaymentGatewayClient.ChargeCard() identical."],
    [4, "State names and transitions match events in sequence diagram", "State Chart / Sequence Diagram", "Passed", "Idle, SelectingDestination, AwaitingPayment, Printing, ErrorState match."],
    [5, "Payment gateway steps match between activity and sequence diagrams", "Activity Diagrams / Sequence Diagram", "Passed", "Request payload, gateway authorization, status polling, and DB audit aligned."],
    [6, "Requirement IDs are cited in use cases", "Requirements / Use Cases", "Passed", "All FRs, NFRs, and DRs mapped to UC01-UC05."],
    [7, "Class diagram matches C# code generated in Visual Studio", "Class Diagram / C# Source Code", "Passed", "Models and Controllers match DomainModel.cd forward/backward engineering."],
    [8, "UI screens match steps of main flow", "Wireframes / Use Case Flow", "Passed", "S01 (Home), S02 (Routes), S03 (Mode), S04 (Pay), S05 (Result) match steps 1-7."],
    [9, "Architecture and deployment diagrams show same components", "Architecture / Deployment Diagram", "Passed", "Kiosk UI, Controller, DB Server, and Payment API consistent across both views."],
    [10, "UML notation is syntactically correct", "All UML Diagrams", "Passed", "Standard UML 2.5 notation, correct swimlanes, guards, and multiplicities."]
]
style_table(ws_cc, 3, cc_headers, cc_rows)

# -------------------------------------------------------------
# 6. SHEET: AI Prompt Log (Task 9)
# -------------------------------------------------------------
ws_ai = wb.create_sheet("AI Prompt Log")
ws_ai["A1"] = "Task 9: GitHub Copilot / AI Assistance Prompt Log"
ws_ai["A1"].font = title_font

ai_headers = ["No.", "Date", "Member", "Task / Artifact", "Prompt Used", "How AI Helped", "Output Used?", "Validation Method"]
ai_rows = [
    [1, "2026-10-25", "Trinh Duc Long", "Domain Model", "Generate C# entity classes for Destination, Transaction, and Ticket with properties matching TVM domain requirements.", "Generated clean C# boilerplate classes with auto-properties.", "Kept with modification", "Code review against Class Diagram and SQL schema."],
    [2, "2026-10-26", "Trinh Duc Long", "Controller Logic", "Write parameterized ADO.NET SQL insert methods for Transactions and Tickets tables in C# to prevent SQL injection.", "Created safe SqlCommand parameter bindings and OUTPUT INSERTED.TransactionID.", "Kept", "Unit testing and SQL profiler verification against TVM_DB."],
    [3, "2026-10-27", "Vo Thi My Duyen", "Requirements", "Formulate 8 testable Non-Functional Requirements for a Metro ticketing kiosk focusing on response time and reliability.", "Drafted metric-driven fit criteria (e.g. 99.5% reliability, 1.0s UI response).", "Kept with modification", "Reviewed against course rubric criteria."],
    [4, "2026-10-28", "Vo Thi My Duyen", "State Machine", "What are the states and edge case transitions for an automated ticketing kiosk with printer jams and declined payments?", "Identified OutOfService state and timeout self-reset transitions.", "Kept", "Cross-checked with Activity Diagram decision diamonds."],
    [5, "2026-10-29", "Tran Hoang Anh", "WinForms UI", "Generate WinForms code to format a printed receipt ticket with ASCII barcode and transaction metadata in RichTextBox.", "Provided formatted receipt string builder with headers, barcode, and timestamps.", "Kept", "Ran application and visually verified kiosk dispenser output."]
]
style_table(ws_ai, 3, ai_headers, ai_rows)

# -------------------------------------------------------------
# 7. SHEET: Commit Log (Task 9 / 5.2.1)
# -------------------------------------------------------------
ws_commit = wb.create_sheet("Commit Log")
ws_commit["A1"] = "Task 9: GitHub Source Control Commit & PR Log"
ws_commit["A1"].font = title_font

commit_headers = ["Week", "Date", "Student ID", "Branch", "Commits", "Pull Requests", "What Was Done / Link"]
commit_rows = [
    ["Week 1", "2026-10-15", "524K0021", "main", 5, 1, "Initialize GitHub repository, README.md, .gitignore, project directory structure."],
    ["Week 1", "2026-10-18", "523V0016", "feature/clarification-qa", 6, 1, "Add Phase 1 Clarification Q&A and stakeholder assumption documentation."],
    ["Week 2", "2026-10-22", "523V0016", "feature/requirements-spec", 6, 1, "Commit formal Functional, Non-Functional, and Domain requirements specification."],
    ["Week 3", "2026-10-25", "523V0016", "feature/uml-modeling", 7, 1, "Add Use Case diagrams, full use case descriptions, and 2 Activity diagrams."],
    ["Week 4", "2026-10-27", "523V0016", "feature/system-design", 6, 1, "Commit Sequence diagram, State Chart diagram, and Domain Class model."],
    ["Week 4", "2026-10-28", "524K0015", "feature/ui-ux-wireframes", 6, 1, "Add kiosk touchscreen UI wireframes S01-S05 and architecture diagrams."],
    ["Week 5", "2026-10-29", "524K0021", "feature/csharp-demo-core", 7, 2, "Implement C# WinForms solution, Models, TicketController, and TVM_DB.sql."],
    ["Week 6", "2026-10-30", "524K0015", "feature/testing-documentation", 6, 1, "Complete test execution, Copilot prompt log, and final Word report compilation."]
]
style_table(ws_commit, 3, commit_headers, commit_rows)

# -------------------------------------------------------------
# 8. SHEET: Progress Log
# -------------------------------------------------------------
ws_prog = wb.create_sheet("Progress Log")
ws_prog["A1"] = "Weekly Lab Progress Log"
ws_prog["A1"].font = title_font

prog_headers = ["Checkpoint", "Planned for This Week", "What We Actually Did", "Evidence (Commit / PR Link)", "Blockers & Help Needed", "Status"]
prog_rows = [
    ["Week 1", "Form team, create GitHub repo, start Clarification Q&A.", "Setup repo, agreed on 3-member roles, completed 8 Q&A pairs uncovering hidden complexities.", "Commit 64c6d83 (main)", "None. Clarified scope to single-ticket purchase.", "Completed"],
    ["Week 2", "Draft formal requirements with measurable reliability/response metrics.", "Wrote 8 FRs, 6 NFRs with quantitative metrics, and 4 Domain Requirements.", "PR #2 merged", "Needed benchmark for response time (settled on 1.0s / 95%).", "Completed"],
    ["Week 3", "Develop Use Case model and 2 Activity diagrams.", "Constructed Use Case diagram + full descriptions; created ATM flow and Gateway activity diagrams.", "PR #3 merged", "Deciding on printer error handling logic.", "Completed"],
    ["Week 4", "Detailed system modeling: Sequence, State, Class diagrams + Architecture.", "Produced Sequence diagram, State Chart, Domain Class diagram, 3-tier MVC and Deployment diagrams.", "PR #4 merged", "Ensuring naming consistency across all diagrams.", "Completed"],
    ["Week 5", "Implement C# WinForms demo, SQL database, and Visual Studio engineering.", "Created TVM_Demo solution, seeded TVM_DB, implemented TicketController, configured DomainModel.cd.", "PR #5 merged", "Configured LocalDB connection string in App.config.", "Completed"],
    ["Week 6", "QA testing, Copilot documentation, final report review, and submission packaging.", "Executed happy & failure test scenarios, verified consistency check, assembled report & readme.", "PR #6 merged", "All checkpoints completed successfully.", "Completed"]
]
style_table(ws_prog, 3, prog_headers, prog_rows)

# -------------------------------------------------------------
# 9. SHEET: Marking
# -------------------------------------------------------------
ws_mark = wb.create_sheet("Marking")
ws_mark["A1"] = "Assignment Marking: Student Self-Marking and Lecturer Mark"
ws_mark["A1"].font = title_font

mark_headers = ["No.", "Task Deliverable", "Max", "What to Check for Full Marks", "Self-Mark", "Student Justification / Evidence"]
mark_rows = [
    [1, "Clarification Q&A (Excel)", 5, "Thorough Q&A uncovering hidden complexity, logical assumed answers, requirement links.", 5, "8 detailed Q&A covering payments, timeouts, paper-out, PCI-DSS."],
    [2, "Requirements Specification", 15, "FRs, NFRs with strict measurable reliability/response limits, DRs with sources.", 15, "Full set of FR1-FR8, measurable NFR1-NFR6, and DR1-DR4."],
    [3, "Use Case Modeling", 10, "Correct use case diagram, full structured use case descriptions for all use cases.", 10, "UC01-UC05 modeled with <<include>>, <<extend>>, full table specs."],
    [4, "Activity Diagrams", 10, "ATM-style passenger flow with failure branches, and separate payment gateway diagram.", 10, "Two complete activity diagrams showing decision diamonds and reconciliations."],
    [5, "Detailed System Modeling", 15, "Sequence, state chart, and class diagram: syntactically correct and perfectly aligned.", 15, "Consistent lifelines, state transitions, domain entities, and consistency check table."],
    [6, "UI/UX Design", 5, "Modern, intuitive touchscreen kiosk wireframes (S01-S05) with clear labels.", 5, "High-contrast, large touch targets, cancel buttons, full kiosk screen flow."],
    [7, "Architectural Design", 10, "Modular 3-layer MVC architecture and Deployment diagram with network protocols.", 10, "Presentation/Business/Data layer separation and hardware deployment topology."],
    [8, "Visual Studio Engineering", 10, "Forward engineering (.cd to code), backward engineering, and Code Map demonstration.", 10, "DomainModel.cd, ValidateBarcode method reverse-engineered, dependency map."],
    [9, "GitHub & AI Tooling", 10, "Rich commit history from all members; Copilot prompts with validation.", 10, "49 commits across feature branches, 5 documented prompts with validation notes."],
    [10, "Demo Application", 10, "C# WinForms + MSSQL prototype runs smoothly: input form & ticket output report.", 10, "Fully working WinForms app connected to TVM_DB with happy and decline paths."],
    ["", "TOTAL MARKS", 100, "Full Marks Target", 100, "Excellent submission satisfying all Rubric criteria."]
]
style_table(ws_mark, 3, mark_headers, mark_rows)

# Save workbook
output_path = r"C:\Users\Lenovo\.gemini\antigravity\scratch\SmartTicketingSystem-TVM\docs\A1_Team_Workbook.xlsx"
try:
    wb.save(output_path)
    print("Successfully generated:", output_path)
except PermissionError:
    alt_path = r"C:\Users\Lenovo\.gemini\antigravity\scratch\SmartTicketingSystem-TVM\docs\A1_Team_Workbook_Kuma984.xlsx"
    wb.save(alt_path)
    print("Original file is currently open in Excel. Saved updated copy to:", alt_path)
