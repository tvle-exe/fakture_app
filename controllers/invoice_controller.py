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
        
        # ⚡️ automatski recalc ukupnog iznosa kada se promijeni PDV
        self.dialog.pdvCheckBox.stateChanged.connect(self.dialog.recalculate_total)

    def open(self):
        self.dialog.open()

    def save_and_export(self):
        invoice = self.dialog.collect_invoice_data()
        
        if not invoice["invoice_number"]:
            QMessageBox.warning(
                self.dialog.dialog,
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

        # ⚠️ Provjera duplikata broja fakture
        for inv in data:
            if inv.get("invoice_number") == invoice["invoice_number"]:
                QMessageBox.warning(
                    self.dialog.dialog,
                    "Greška",
                    f"Faktura s brojem {invoice['invoice_number']} već postoji!"
                )
                return  # prekini spremanje

        # kreiraj JSON zapis
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

        # Spremi JSON
        with open(INVOICES_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        # ================= PDF =================
        export_invoice_pdf(json_invoice)

        QMessageBox.information(
            self.dialog.dialog,
            "Uspjeh",
            f"Faktura #{invoice['invoice_number']} je spremljena i PDF je exportan."
        )

        self.dialog.close()

