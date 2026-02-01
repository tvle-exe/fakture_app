import json
from pathlib import Path

INVOICES_FILE = Path("data/invoices.json")

def save_invoice(invoice_data: dict):
    if INVOICES_FILE.exists():
        with open(INVOICES_FILE, "r", encoding="utf-8") as f:
            invoices = json.load(f)
    else:
        invoices = []

    invoices.append(invoice_data)

    with open(INVOICES_FILE, "w", encoding="utf-8") as f:
        json.dump(invoices, f, indent=2, ensure_ascii=False)
