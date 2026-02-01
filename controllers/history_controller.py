from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QPushButton, QTableWidget, QLineEdit, QDateEdit, QCheckBox
from views.history_window import HistoryWindow
from PySide6.QtCore import QDate
import json
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class HistoryController:
    def __init__(self):
        self.window = HistoryWindow()
        self.invoices_file = "data/invoices.json"

        # Pronađi sve widgete
        ui = self.window.ui
        self.addItemButton = ui.findChild(QPushButton, "addItemButton")
        self.removeItemButton = ui.findChild(QPushButton, "removeItemButton")
        self.saveButton = ui.findChild(QPushButton, "saveButton")
        self.closeButton = ui.findChild(QPushButton, "closeButton")
        self.deleteInvoiceButton = ui.findChild(QPushButton, "deleteInvoiceButton")
        self.exportPDFButton = ui.findChild(QPushButton, "exportPDFButton")

        self.invoiceNumberLineEdit = ui.findChild(QLineEdit, "invoiceNumberLineEdit")
        self.clientLineEdit = ui.findChild(QLineEdit, "clientLineEdit")
        self.descriptionLineEdit = ui.findChild(QLineEdit, "descriptionLineEdit")
        self.dateEdit = ui.findChild(QDateEdit, "dateEdit")
        self.pdvCheckBox = ui.findChild(QCheckBox, "pdvCheckBox")
        self.totalLineEdit = ui.findChild(QLineEdit, "totalLineEdit")

        self.itemsTableWidget = ui.findChild(QTableWidget, "itemsTableWidget")
        self.invoicesTable = ui.findChild(QTableWidget, "invoicesTable")

        self.load_invoices()
        self.connect_signals()

    def connect_signals(self):
        self.addItemButton.clicked.connect(self.add_item)
        self.removeItemButton.clicked.connect(self.remove_item)
        self.saveButton.clicked.connect(self.save_invoice)
        self.closeButton.clicked.connect(self.window.close)
        self.invoicesTable.itemSelectionChanged.connect(self.load_selected_invoice)
        self.deleteInvoiceButton.clicked.connect(self.delete_invoice)
        self.exportPDFButton.clicked.connect(self.export_selected_invoice_pdf)

    def load_invoices(self):
        """Učitaj fakture iz JSON-a u tablicu faktura"""
        try:
            with open(self.invoices_file, "r", encoding="utf-8") as f:
                self.invoices = json.load(f)
        except FileNotFoundError:
            self.invoices = []

        self.invoicesTable.setRowCount(0)
        for invoice in self.invoices:
            row = self.invoicesTable.rowCount()
            self.invoicesTable.insertRow(row)
            self.invoicesTable.setItem(row, 0, QTableWidgetItem(invoice.get("invoice_number", "")))
            self.invoicesTable.setItem(row, 1, QTableWidgetItem(invoice.get("client", "")))
            self.invoicesTable.setItem(row, 2, QTableWidgetItem(invoice.get("date", "")))
            self.invoicesTable.setItem(row, 3, QTableWidgetItem(str(invoice.get("total_with_vat", ""))))

    def load_selected_invoice(self):
        """Prikaz odabrane fakture u formi i stavkama"""
        selected = self.invoicesTable.selectedItems()
        if not selected:
            return
        row = selected[0].row()
        invoice = self.invoices[row]

        self.invoiceNumberLineEdit.setText(invoice.get("invoice_number", ""))
        self.clientLineEdit.setText(invoice.get("client", ""))
        self.descriptionLineEdit.setText(invoice.get("description", ""))
        date_str = invoice.get("date", "2026-01-01")
        year, month, day = map(int, date_str.split("-"))
        self.dateEdit.setDate(QDate(year, month, day))
        self.pdvCheckBox.setChecked(invoice.get("pdv_included", True))
        self.totalLineEdit.setText(str(invoice.get("total_with_vat", "")))

        self.itemsTableWidget.setRowCount(0)
        for item in invoice.get("items", []):
            row_item = self.itemsTableWidget.rowCount()
            self.itemsTableWidget.insertRow(row_item)
            self.itemsTableWidget.setItem(row_item, 0, QTableWidgetItem(item.get("description", "")))
            self.itemsTableWidget.setItem(row_item, 1, QTableWidgetItem(str(item.get("quantity", ""))))
            self.itemsTableWidget.setItem(row_item, 2, QTableWidgetItem(item.get("unit", "")))
            self.itemsTableWidget.setItem(row_item, 3, QTableWidgetItem(str(item.get("price", ""))))
            self.itemsTableWidget.setItem(row_item, 4, QTableWidgetItem(str(item.get("total", ""))))

    def add_item(self):
        row = self.itemsTableWidget.rowCount()
        self.itemsTableWidget.insertRow(row)
        for col in range(5):
            self.itemsTableWidget.setItem(row, col, QTableWidgetItem(""))

    def remove_item(self):
        selected = self.itemsTableWidget.selectedItems()
        if selected:
            row = selected[0].row()
            self.itemsTableWidget.removeRow(row)

    def save_invoice(self):
        """Spremi fakturu kao novu, bez mijenjanja postojećih faktura"""
        # Pripremi stavke
        items = []
        for r in range(self.itemsTableWidget.rowCount()):
            items.append({
                "description": self.itemsTableWidget.item(r, 0).text() if self.itemsTableWidget.item(r, 0) else "",
                "quantity": float(self.itemsTableWidget.item(r, 1).text() or 0),
                "unit": self.itemsTableWidget.item(r, 2).text() if self.itemsTableWidget.item(r, 2) else "",
                "price": float(self.itemsTableWidget.item(r, 3).text() or 0),
                "total": float(self.itemsTableWidget.item(r, 4).text() or 0)
            })

        # Napravi novu fakturu
        invoice = {
            "invoice_number": self.invoiceNumberLineEdit.text(),
            "client": self.clientLineEdit.text(),
            "description": self.descriptionLineEdit.text(),
            "date": self.dateEdit.date().toString("yyyy-MM-dd"),
            "items": items,
            "subtotal": sum([i["total"] for i in items]),
            "pdv_included": self.pdvCheckBox.isChecked(),
            "total_with_vat": round(sum([i["total"] for i in items]) * 1.25 if self.pdvCheckBox.isChecked() else sum([i["total"] for i in items]), 2)
        }

        # Dodaj novu fakturu u listu
        self.invoices.append(invoice)

        # Spremi u JSON
        with open(self.invoices_file, "w", encoding="utf-8") as f:
            json.dump(self.invoices, f, indent=4, ensure_ascii=False)

        # Osvježi prikaz tablice
        self.load_invoices()
        QMessageBox.information(self.window, "Uspjeh", "Faktura je spremljena kao nova")


    def delete_invoice(self):
        selected = self.invoicesTable.selectedItems()
        if not selected:
            QMessageBox.warning(self.window, "Upozorenje", "Odaberite fakturu za brisanje")
            return
        row = selected[0].row()
        invoice = self.invoices[row]

        confirm = QMessageBox.question(
            self.window,
            "Potvrda brisanja",
            f"Jeste li sigurni da želite obrisati fakturu {invoice['invoice_number']}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            self.invoices.pop(row)
            with open(self.invoices_file, "w", encoding="utf-8") as f:
                json.dump(self.invoices, f, indent=4, ensure_ascii=False)
            self.load_invoices()
            self.invoiceNumberLineEdit.clear()
            self.clientLineEdit.clear()
            self.descriptionLineEdit.clear()
            self.dateEdit.setDate(QDate.currentDate())
            self.pdvCheckBox.setChecked(True)
            self.totalLineEdit.clear()
            self.itemsTableWidget.setRowCount(0)
            QMessageBox.information(self.window, "Uspjeh", "Faktura je obrisana")

    def export_selected_invoice_pdf(self):
        selected = self.invoicesTable.selectedItems()
        if not selected:
            QMessageBox.warning(self.window, "Upozorenje", "Odaberite fakturu za export")
            return
        row = selected[0].row()
        invoice = self.invoices[row]

        try:
            self.export_pdf(invoice)
            QMessageBox.information(self.window, "Uspjeh", f"Faktura {invoice['invoice_number']} je exportana u PDF")
        except Exception as e:
            QMessageBox.critical(self.window, "Greška", f"Greška pri exportu PDF: {str(e)}")

    def export_pdf(self, invoice):
        os.makedirs(os.path.join(BASE_DIR, "..", "pdf"), exist_ok=True)
        filename = os.path.normpath(os.path.join(BASE_DIR, "..", f"pdf/faktura_{invoice['invoice_number']}.pdf"))
        width, height = A4

        font_path = os.path.normpath(os.path.join(BASE_DIR, "..", "assets", "fonts", "DejaVuSans.ttf"))
        pdfmetrics.registerFont(TTFont('DejaVu', font_path))

        c = canvas.Canvas(filename, pagesize=A4)
        y = height - 50

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

        c.setFont("DejaVu", 11)
        c.drawString(50, y, "Opis")
        c.drawCentredString(350, y, "Količina")
        c.drawRightString(450, y, "Cijena")
        c.drawRightString(530, y, "Iznos")
        y -= 15
        c.setStrokeColor(colors.black)
        c.line(50, y, 530, y)
        y -= 20

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

        subtotal = sum(item["total"] for item in invoice["items"])
        c.setFont("DejaVu", 12)
        y -= 20
        c.drawRightString(530, y, f"UKUPNO bez PDV-a: {subtotal:.2f} EUR")

        if invoice.get("pdv_included"):
            total_with_vat = invoice["total_with_vat"]
            y -= 20
            c.drawRightString(530, y, f"UKUPNO sa PDV-om 25%: {total_with_vat:.2f} EUR")

        c.save()

    def open(self):
        self.window.show()
