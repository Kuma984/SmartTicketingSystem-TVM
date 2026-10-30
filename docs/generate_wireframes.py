from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"C:\Users\Lenovo\.gemini\antigravity\scratch\SmartTicketingSystem-TVM\docs\screenshots"
os.makedirs(output_dir, exist_ok=True)

# Common styling constants
W, H = 800, 500
BG_COLOR = (245, 247, 250)
NAVY = (26, 54, 93)
BLUE = (49, 130, 206)
WHITE = (255, 255, 255)
DARK_TEXT = (45, 55, 72)
GRAY_TEXT = (113, 128, 150)
LIGHT_GRAY = (226, 232, 240)
BORDER_COLOR = (203, 213, 225)
GREEN = (40, 167, 69)
RED = (229, 62, 62)

def draw_header(draw, title="SMART METRO TICKETING SYSTEM — TVM-01"):
    draw.rectangle([0, 0, W, 65], fill=NAVY)
    draw.text((25, 20), title, fill=WHITE)
    draw.text((W - 140, 24), "● SYSTEM ONLINE", fill=(72, 187, 120))

def draw_footer(draw, hint="Touch screen to operate | Emergency help: Dial station intercom"):
    draw.rectangle([0, H - 35, W, H], fill=(237, 242, 247))
    draw.line([0, H - 35, W, H - 35], fill=BORDER_COLOR, width=1)
    draw.text((25, H - 24), hint, fill=GRAY_TEXT)

# -------------------------------------------------------------
# SCREEN 1: S01 - Welcome & Idle Screen
# -------------------------------------------------------------
img1 = Image.new("RGB", (W, H), BG_COLOR)
d1 = ImageDraw.Draw(img1)
draw_header(d1)
draw_footer(d1)

# Center Welcome Box
d1.rounded_rectangle([150, 110, 650, 420], radius=15, fill=WHITE, outline=BORDER_COLOR, width=2)
d1.text((230, 140), "WELCOME TO SMART METRO", fill=NAVY)
d1.text((200, 175), "Fast, Automated Ticket Vending Kiosk (TVM)", fill=GRAY_TEXT)
d1.text((280, 210), "Language / Ngôn ngữ: [ Tiếng Việt | English ]", fill=BLUE)

# Big Start Button
d1.rounded_rectangle([250, 260, 550, 340], radius=12, fill=GREEN)
d1.text((310, 290), "👉 TOUCH TO START / BẮT ĐẦU", fill=WHITE)
d1.text((245, 370), "Accepted: Credit/Debit Card & Mobile Banking QR", fill=GRAY_TEXT)
img1.save(os.path.join(output_dir, "S01_Home_Welcome.png"))

# -------------------------------------------------------------
# SCREEN 2: S02 - Destination Selection Menu
# -------------------------------------------------------------
img2 = Image.new("RGB", (W, H), BG_COLOR)
d2 = ImageDraw.Draw(img2)
draw_header(d2)
draw_footer(d2)

d2.text((25, 80), "STEP 1: SELECT YOUR DESTINATION ROUTE", fill=NAVY)
stations = [
    ("Ben Thanh Market (Metro Station 1)", "Standard Fare: 7,000 VND"),
    ("Suoi Tien Theme Park (Metro Station 14)", "Standard Fare: 12,000 VND"),
    ("Tan Son Nhat International Airport", "Express Line: 20,000 VND"),
    ("Saigon Hi-Tech Park (SHTP Station)", "Standard Fare: 15,000 VND")
]

for i, (name, fare) in enumerate(stations):
    x = 25 if i % 2 == 0 else 415
    y = 120 + (i // 2) * 130
    is_sel = (i == 0)
    box_fill = (235, 248, 255) if is_sel else WHITE
    border_col = BLUE if is_sel else BORDER_COLOR
    d2.rounded_rectangle([x, y, x + 360, y + 110], radius=10, fill=box_fill, outline=border_col, width=2 if is_sel else 1)
    d2.text((x + 20, y + 25), name, fill=NAVY)
    d2.text((x + 20, y + 60), fare, fill=GREEN if is_sel else BLUE)
    if is_sel:
        d2.text((x + 280, y + 60), "✔ SELECTED", fill=BLUE)

d2.rounded_rectangle([660, 75, 775, 110], radius=6, fill=RED)
d2.text((680, 85), "✖ CANCEL", fill=WHITE)
img2.save(os.path.join(output_dir, "S02_Destination_Menu.png"))

# -------------------------------------------------------------
# SCREEN 3: S03 - Payment Mode Selection
# -------------------------------------------------------------
img3 = Image.new("RGB", (W, H), BG_COLOR)
d3 = ImageDraw.Draw(img3)
draw_header(d3)
draw_footer(d3)

d3.text((25, 80), "STEP 2: CHOOSE PAYMENT METHOD", fill=NAVY)
d3.rounded_rectangle([25, 115, 775, 175], radius=8, fill=WHITE, outline=BORDER_COLOR)
d3.text((45, 135), "Selected Route: Ben Thanh Market (Station 1) | Amount Due: 7,000 VND", fill=NAVY)

# Payment Cards
d3.rounded_rectangle([60, 200, 390, 380], radius=12, fill=WHITE, outline=BLUE, width=2)
d3.text((100, 235), "💳 CREDIT / DEBIT CARD", fill=NAVY)
d3.text((90, 275), "• Contactless NFC Tap & Chip Card", fill=DARK_TEXT)
d3.text((90, 305), "• Visa, MasterCard, JCB, Napas", fill=GRAY_TEXT)
d3.rounded_rectangle([130, 335, 320, 365], radius=6, fill=BLUE)
d3.text((155, 343), "SELECT CARD", fill=WHITE)

d3.rounded_rectangle([410, 200, 740, 380], radius=12, fill=WHITE, outline=BORDER_COLOR)
d3.text((460, 235), "📱 DIGITAL WALLET / QR", fill=NAVY)
d3.text((440, 275), "• Dynamic QR code with 120s timer", fill=DARK_TEXT)
d3.text((440, 305), "• VNPay, MoMo, ZaloPay, VietQR", fill=GRAY_TEXT)
d3.rounded_rectangle([480, 335, 670, 365], radius=6, fill=LIGHT_GRAY)
d3.text((515, 343), "SELECT QR", fill=DARK_TEXT)

d3.rounded_rectangle([660, 75, 775, 110], radius=6, fill=RED)
d3.text((680, 85), "✖ CANCEL", fill=WHITE)
img3.save(os.path.join(output_dir, "S03_Payment_Mode.png"))

# -------------------------------------------------------------
# SCREEN 4: S04 - Card / QR Processing Screen
# -------------------------------------------------------------
img4 = Image.new("RGB", (W, H), BG_COLOR)
d4 = ImageDraw.Draw(img4)
draw_header(d4)
draw_footer(d4)

d4.text((25, 80), "STEP 3: AWAITING PAYMENT AUTHORIZATION", fill=NAVY)
d4.rounded_rectangle([120, 115, 680, 420], radius=12, fill=WHITE, outline=BORDER_COLOR, width=2)
d4.text((220, 140), "PLEASE TAP OR INSERT YOUR CARD BELOW", fill=NAVY)
d4.text((180, 175), "Communicating with Bank Gateway API (HTTPS / TLS 1.3)...", fill=GRAY_TEXT)

# Card Slot Graphic
d4.rounded_rectangle([250, 220, 550, 320], radius=8, fill=(237, 242, 247), outline=BLUE, width=2)
d4.text((310, 250), "[ CARD READER SLOT ]", fill=BLUE)
d4.text((290, 280), "Insert chip or tap contactless NFC", fill=GRAY_TEXT)

d4.text((330, 350), "⏱ Timeout in: 01:45", fill=RED)
d4.rounded_rectangle([320, 380, 480, 410], radius=6, fill=RED)
d4.text((365, 388), "✖ CANCEL", fill=WHITE)
img4.save(os.path.join(output_dir, "S04_Payment_InProgress.png"))

# -------------------------------------------------------------
# SCREEN 5: S05 - Ticket Dispensed / Success Screen
# -------------------------------------------------------------
img5 = Image.new("RGB", (W, H), BG_COLOR)
d5 = ImageDraw.Draw(img5)
draw_header(d5)
draw_footer(d5)

d5.text((25, 80), "TRANSACTION COMPLETED — TICKET ISSUED", fill=GREEN)
d5.rounded_rectangle([120, 115, 680, 430], radius=12, fill=WHITE, outline=GREEN, width=2)
d5.text((260, 135), "✅ PAYMENT AUTHORIZED (7,000 VND)", fill=GREEN)

# Ticket Shape
d5.rounded_rectangle([200, 170, 600, 360], radius=6, fill=(254, 252, 232), outline=BORDER_COLOR)
d5.text((280, 185), "SMART METRO SINGLE TRIP TICKET", fill=NAVY)
d5.text((220, 215), "Ticket ID   : TKT-000006", fill=DARK_TEXT)
d5.text((220, 238), "Destination : Ben Thanh Market (Station 1)", fill=DARK_TEXT)
d5.text((220, 261), "Fare Paid   : 7,000 VND (Credit Card)", fill=DARK_TEXT)
d5.text((220, 284), "Issued At   : 2026-10-30 21:39:06", fill=GRAY_TEXT)
d5.line([220, 305, 580, 305], fill=BORDER_COLOR, width=1)
d5.text((260, 315), "||||||||||||||||||||||||||||||||||||||||||||||||||", fill=NAVY)
d5.text((320, 335), "BARCODE: TVM00000006", fill=NAVY)

d5.text((230, 380), "Please collect your ticket below. Session resets in 10s...", fill=GRAY_TEXT)
img5.save(os.path.join(output_dir, "S05_Ticket_Issued.png"))

print("All 5 wireframe images successfully generated in:", output_dir)
