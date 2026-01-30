import json
import os

FILE_PATH = "data/invoices.json"


def save_invoice(invoice):
    os.makedirs("data", exist_ok=True)

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(invoice)

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
