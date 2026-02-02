import os
import sys
import json
from PySide6.QtWidgets import QMessageBox
from views.invoice_dialog import InvoiceDialog
from utils.pdf_utils import export_invoice_pdf

# ================= ROOT FOLDER APLIKACIJE =================
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# putanje za JSON i PDF u root folderu
DATA_DIR = os.path.join(BASE_DIR, "data")
PDF_DIR = os.path.join(BASE_DIR, "pdf")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

INVOICES_JSON_PATH = os.path.join(DATA_DIR, "invoices.json")


class InvoiceController:
    def __init__(self):
        self.dialog = InvoiceDialog()
        # povezivanje gumbića
        self.dialog.closeButton.clicked.connect(self.dialog.close)
        self.dialog.saveButton.clicked.connect(self.save_and_export)
              

    def open(self):
        self.dialog.open()

    def save_and_export(self):
        invoice = self.dialog.collect_invoice_data()
        if not invoice["invoice_number"]:
            print("GREŠKA: broj fakture nije unesen!")
             # Prikaži grešku korisniku
            QMessageBox.warning(
                self.dialog.dialog,  # parent je glavni dialog
                "Greška",
                "Broj fakture nije unesen!"
            )
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

        # Spremi JSON u root/data
        with open(INVOICES_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Faktura #{invoice['invoice_number']} spremljena u JSON za klijenta: {invoice['client']}")

        # ================= PDF =================
        export_invoice_pdf(json_invoice)

        self.dialog.close()
