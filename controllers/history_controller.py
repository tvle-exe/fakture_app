from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QPushButton, QTableWidget, QLineEdit, QDateEdit, QCheckBox
from views.history_window import HistoryWindow
from PySide6.QtCore import QDate
import json
import os
import sys
from utils.pdf_utils import export_invoice_pdf

# ================= ROOT FOLDER APLIKACIJE =================
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# putanje za JSON i PDF
DATA_DIR = os.path.join(BASE_DIR, "data")
PDF_DIR = os.path.join(BASE_DIR, "pdf")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

INVOICES_JSON_PATH = os.path.join(DATA_DIR, "invoices.json")

class HistoryController:
    def __init__(self):
        self.window = HistoryWindow()
        self.invoices_file = INVOICES_JSON_PATH  # JSON u root/data

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
        items = []
        for r in range(self.itemsTableWidget.rowCount()):
            items.append({
                "description": self.itemsTableWidget.item(r, 0).text() if self.itemsTableWidget.item(r, 0) else "",
                "quantity": float(self.itemsTableWidget.item(r, 1).text() or 0),
                "unit": self.itemsTableWidget.item(r, 2).text() if self.itemsTableWidget.item(r, 2) else "",
                "price": float(self.itemsTableWidget.item(r, 3).text() or 0),
                "total": float(self.itemsTableWidget.item(r, 4).text() or 0)
            })

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

        self.invoices.append(invoice)

        # spremi u JSON u root/data
        with open(self.invoices_file, "w", encoding="utf-8") as f:
            json.dump(self.invoices, f, indent=4, ensure_ascii=False)

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
            # export u PDF u root/pdf
            export_invoice_pdf(invoice)
            QMessageBox.information(self.window, "Uspjeh", f"Faktura {invoice['invoice_number']} je exportana u PDF")
        except Exception as e:
            QMessageBox.critical(self.window, "Greška", f"Greška pri exportu PDF: {str(e)}")

    def open(self):
        self.window.show()
