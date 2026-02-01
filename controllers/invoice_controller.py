import os
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

from views.invoice_dialog import InvoiceDialog

# ================= ABSOLUTNA PUTANJA DO JSON =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INVOICES_JSON_PATH = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "invoices.json"))


class InvoiceController:
    def __init__(self):
        self.dialog = InvoiceDialog()
        self.dialog.closeButton.clicked.connect(self.dialog.close)
        self.dialog.saveButton.clicked.connect(self.save_and_export)

    def open(self):
        self.dialog.open()

    def save_and_export(self):
        """
        Sprema fakturu u JSON i PDF.
        Poziva se kad korisnik klikne 'Spremi'.
        """
        invoice = self.dialog.collect_invoice_data()
        if not invoice["invoice_number"]:
            print("GREŠKA: broj fakture nije unesen!")
            return

        # ================= JSON =================
        os.makedirs(os.path.dirname(INVOICES_JSON_PATH), exist_ok=True)
        data = []
        if os.path.exists(INVOICES_JSON_PATH):
            with open(INVOICES_JSON_PATH, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

        # Kreiraj kompletan zapis za JSON
        json_invoice = {
            "invoice_number": invoice["invoice_number"],
            "client": invoice["client"],
            "description": invoice["description"],
            "date": invoice["date"],
            "items": [
                {
                    "description": item["description"],
                    "quantity": item["quantity"],
                    "unit": item["unit"],
                    "price": item["price"],
                    "total": item["total"]
                }
                for item in invoice["items"]
            ],
            "subtotal": sum(item["total"] for item in invoice["items"]),
            "pdv_included": invoice.get("pdv_included", False),
            "total_with_vat": invoice["total"]
        }

        data.append(json_invoice)

        with open(INVOICES_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Faktura #{invoice['invoice_number']} spremljena u JSON za klijenta: {invoice['client']}")

        # ================= PDF =================
        self.export_pdf(invoice)

        self.dialog.close()

    def export_pdf(self, invoice):
        os.makedirs(os.path.join(BASE_DIR, "..", "pdf"), exist_ok=True)
        filename = os.path.normpath(os.path.join(BASE_DIR, "..", f"pdf/faktura_{invoice['invoice_number']}.pdf"))

        width, height = A4

        # Registriraj Unicode TTF font
        font_path = os.path.normpath(os.path.join(BASE_DIR, "..", "assets", "fonts", "DejaVuSans.ttf"))
        pdfmetrics.registerFont(TTFont('DejaVu', font_path))

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
        c.drawString(50, y, "Opis")
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
            c.drawRightString(450, y, f"{item['price']:.2f}")
            c.drawRightString(530, y, f"{item['total']:.2f}")
            y -= 20
            if y < 50:
                c.showPage()
                y = height - 50

        # ================= TOTALS =================
        subtotal = sum(item["total"] for item in invoice["items"])
        c.setFont("DejaVu", 12)
        y -= 20
        c.drawRightString(530, y, f"UKUPNO bez PDV-a: {subtotal:.2f} EUR")

        if invoice.get("pdv_included"):
            total_with_vat = invoice["total"]
            y -= 20
            c.drawRightString(530, y, f"UKUPNO sa PDV-om 25%: {total_with_vat:.2f} EUR")

        c.save()
