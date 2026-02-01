from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_invoice_pdf(invoice, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"Klijent: {invoice['client']}")
    y -= 30
    c.drawString(50, y, f"Datum: {invoice['date']}")
    y -= 40

    for item in invoice["items"]:
        line = f"{item['description']} | {item['quantity']} x {item['price']} = {item['total']}"
        c.drawString(50, y, line)
        y -= 20

    c.save()
