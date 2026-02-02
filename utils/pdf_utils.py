import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

def resource_path(relative_path):
    """Vrati apsolutnu putanju do resursa, radi i u exe i u .py"""
    try:
        base_path = sys._MEIPASS  # PyInstaller privremeni folder
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# ================= ROOT FOLDER APLIKACIJE =================
# BASE_DIR je root folder 'fakture_app', a ne utils
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# putanje za PDF folder
PDF_DIR = os.path.join(BASE_DIR, "pdf")
os.makedirs(PDF_DIR, exist_ok=True)

def export_invoice_pdf(invoice):
    """
    Generira PDF fakturu iz dictionary 'invoice'
    """
    filename = os.path.join(PDF_DIR, f"faktura_{invoice['invoice_number']}.pdf")

    width, height = A4
    
    # Registracija fontova (koristimo root folder aplikacije)
    font_path = os.path.join(BASE_DIR, "assets", "fonts", "DejaVuSans.ttf")
    pdfmetrics.registerFont(TTFont('DejaVu', font_path))

    bold_font_path = os.path.join(BASE_DIR, "assets", "fonts", "DejaVuSans-Bold.ttf")
    pdfmetrics.registerFont(TTFont('DejaVu-Bold', bold_font_path))

    c = canvas.Canvas(filename, pagesize=A4)
    y = height - 50

    # ================= HEADER =================
    c.setFont("DejaVu", 18)
    c.drawString(50, y, "Faktura")
    y -= 30
    c.setFont("DejaVu", 12)
    c.drawString(50, y, f"Broj fakture: {invoice['invoice_number']}")
    y -= 20
    c.setFont("DejaVu", 11)
    c.drawString(50, y, f"Klijent: {invoice['client']}")
    y -= 20
    c.drawString(50, y, f"Opis: {invoice['description']}")
    y -= 20
    c.drawString(50, y, f"Datum: {invoice['date']}")
    y -= 40

    # ================= TABLE HEADER =================
    c.setFont("DejaVu", 11)
    c.drawString(50, y, "Stavka")
    c.drawCentredString(350, y, "Količina")
    c.drawRightString(450, y, "Cijena")
    c.drawRightString(530, y, "Iznos")
    y -= 15
    c.setStrokeColor(colors.black)
    c.line(50, y, 530, y)
    y -= 20

    # ================= ITEMS =================
    for item in invoice["items"]:
        c.drawString(50, y, item["description"])
        qty_with_unit = f"{item['quantity']} {item['unit']}"
        c.drawCentredString(350, y, qty_with_unit)
        c.drawRightString(450, y, f"{item['price']:.2f} €")
        c.drawRightString(530, y, f"{item['total']:.2f} €")
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    # ================= TOTALS =================
    subtotal = sum(item["total"] for item in invoice["items"])
    c.setFont("DejaVu-Bold", 12)
    y -= 20
    c.drawRightString(530, y, f"UKUPNO bez PDV-a: {subtotal:.2f} €")

    if invoice.get("pdv_included"):
        total_with_vat = invoice.get("total_with_vat", subtotal * 1.25)
        y -= 20
        c.drawRightString(530, y, f"UKUPNO sa PDV-om 25%: {total_with_vat:.2f} €")

    c.save()
    return filename
