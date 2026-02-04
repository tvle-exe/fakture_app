import os
import sys
import json
from PySide6.QtWidgets import (
    QTableWidgetItem, QMessageBox, QPushButton, QTableWidget,
    QLineEdit, QDateEdit, QCheckBox
)
from views.history_window import HistoryWindow
from PySide6.QtCore import QDate

# ================= ROOT FOLDER =================
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

INVOICES_JSON_PATH = os.path.join(DATA_DIR, "invoices.json")


class HistoryController:
    def __init__(self):
        self.window = HistoryWindow()
        self.invoices_file = INVOICES_JSON_PATH

        # Widgeti
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

        # Load i connect
        self.load_invoices()
        self.connect_signals()

    # ================= SIGNALI =================
    def connect_signals(self):
        self.addItemButton.clicked.connect(self.add_item)
        self.removeItemButton.clicked.connect(self.remove_item)
        self.saveButton.clicked.connect(self.save_invoice)
        self.closeButton.clicked.connect(self.window.close)
        self.invoicesTable.itemSelectionChanged.connect(self.load_selected_invoice)
        self.deleteInvoiceButton.clicked.connect(self.delete_invoice)
        self.pdvCheckBox.stateChanged.connect(self.recalculate_total)
        self.itemsTableWidget.cellChanged.connect(self.cell_changed)
        self.exportPDFButton.clicked.connect(self.export_selected_invoice_pdf)


    # ================= HELPER =================
    def to_float(self, text: str) -> float:
        if not text:
            return 0.0
        text = text.replace("€", "").replace(",", ".").strip()
        try:
            return float(text)
        except ValueError:
            return 0.0

    # ================= LOAD =================
    def load_invoices(self):
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
            self.invoicesTable.setItem(row, 3, QTableWidgetItem(f"{invoice.get('total_with_vat',0):.2f} €"))

    def load_selected_invoice(self):
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

        self.itemsTableWidget.blockSignals(True)
        self.itemsTableWidget.setRowCount(0)
        for item in invoice.get("items", []):
            row_item = self.itemsTableWidget.rowCount()
            self.itemsTableWidget.insertRow(row_item)
            self.itemsTableWidget.setItem(row_item, 0, QTableWidgetItem(item.get("description", "")))
            self.itemsTableWidget.setItem(row_item, 1, QTableWidgetItem(str(item.get("quantity", ""))))
            self.itemsTableWidget.setItem(row_item, 2, QTableWidgetItem(item.get("unit", "")))
            self.itemsTableWidget.setItem(row_item, 3, QTableWidgetItem(f"{item.get('price',0):.2f} €"))
            self.itemsTableWidget.setItem(row_item, 4, QTableWidgetItem(f"{item.get('total',0):.2f} €"))
        self.itemsTableWidget.blockSignals(False)

        self.recalculate_total()

    # ================= ITEMS =================
    def add_item(self):
        row = self.itemsTableWidget.rowCount()
        self.itemsTableWidget.insertRow(row)
        self.itemsTableWidget.setItem(row, 0, QTableWidgetItem(""))
        self.itemsTableWidget.setItem(row, 1, QTableWidgetItem("1"))
        self.itemsTableWidget.setItem(row, 2, QTableWidgetItem("kom"))
        self.itemsTableWidget.setItem(row, 3, QTableWidgetItem("0.00 €"))
        self.itemsTableWidget.setItem(row, 4, QTableWidgetItem("0.00 €"))
        self.recalculate_total()

    def remove_item(self):
        selected = self.itemsTableWidget.selectedItems()
        if selected:
            row = selected[0].row()
            self.itemsTableWidget.removeRow(row)
            self.recalculate_total()

    # ================= CELL CHANGED =================
    def cell_changed(self, row, column):
        """Automatski racuna total kada se promijeni kolicina ili cijena"""
        if column not in (1,3):
            return
        qty_item = self.itemsTableWidget.item(row,1)
        price_item = self.itemsTableWidget.item(row,3)
        if not qty_item or not price_item:
            return
        quantity = self.to_float(qty_item.text())
        price = self.to_float(price_item.text())
        total = quantity * price
        self.itemsTableWidget.blockSignals(True)
        self.itemsTableWidget.setItem(row,4,QTableWidgetItem(f"{total:.2f} €"))
        self.itemsTableWidget.blockSignals(False)
        self.recalculate_total()

    # ================= RECALCULATE TOTAL =================
    def recalculate_total(self):
        total = 0
        for r in range(self.itemsTableWidget.rowCount()):
            total += self.to_float(self.itemsTableWidget.item(r,4).text() if self.itemsTableWidget.item(r,4) else "0")
        if self.pdvCheckBox.isChecked():
            total *= 1.25
        self.totalLineEdit.setText(f"{total:.2f} €")

    # ================= SAVE =================
    def save_invoice(self):
        invoice_number = self.invoiceNumberLineEdit.text().strip()
        if not invoice_number:
            QMessageBox.warning(self.window, "Greška", "Broj fakture nije unesen!")
            return

        # Provjera duplikata
        for inv in self.invoices:
            if inv.get("invoice_number") == invoice_number:
                QMessageBox.warning(self.window, "Greška", f"Faktura s brojem {invoice_number} već postoji!")
                return

        items = []
        for r in range(self.itemsTableWidget.rowCount()):
            items.append({
                "description": self.itemsTableWidget.item(r,0).text() if self.itemsTableWidget.item(r,0) else "",
                "quantity": self.to_float(self.itemsTableWidget.item(r,1).text() if self.itemsTableWidget.item(r,1) else "0"),
                "unit": self.itemsTableWidget.item(r,2).text() if self.itemsTableWidget.item(r,2) else "",
                "price": self.to_float(self.itemsTableWidget.item(r,3).text() if self.itemsTableWidget.item(r,3) else "0"),
                "total": self.to_float(self.itemsTableWidget.item(r,4).text() if self.itemsTableWidget.item(r,4) else "0")
            })

        invoice_data = {
            "invoice_number": invoice_number,
            "client": self.clientLineEdit.text(),
            "description": self.descriptionLineEdit.text(),
            "date": self.dateEdit.date().toString("yyyy-MM-dd"),
            "items": items,
            "subtotal": sum(i["total"] for i in items),
            "pdv_included": self.pdvCheckBox.isChecked(),
            "total_with_vat": round(sum(i["total"] for i in items) * (1.25 if self.pdvCheckBox.isChecked() else 1),2)
        }

        # ⚡ Dodavanje nove fakture, nikad update
        self.invoices.append(invoice_data)

        with open(self.invoices_file,"w",encoding="utf-8") as f:
            json.dump(self.invoices,f,indent=4,ensure_ascii=False)

        self.load_invoices()
        QMessageBox.information(self.window,"Uspjeh",f"Nova faktura #{invoice_number} je spremljena.")

    # ================= DELETE =================
    def delete_invoice(self):
        selected = self.invoicesTable.selectedItems()
        if not selected:
            QMessageBox.warning(self.window, "Upozorenje","Odaberite fakturu za brisanje")
            return
        row = selected[0].row()
        invoice = self.invoices[row]
        confirm = QMessageBox.question(
            self.window,"Potvrda brisanja",
            f"Jeste li sigurni da želite obrisati fakturu {invoice['invoice_number']}?",
            QMessageBox.Yes|QMessageBox.No
        )
        if confirm==QMessageBox.Yes:
            self.invoices.pop(row)
            with open(self.invoices_file,"w",encoding="utf-8") as f:
                json.dump(self.invoices,f,indent=4,ensure_ascii=False)
            self.load_invoices()
            self.invoiceNumberLineEdit.clear()
            self.clientLineEdit.clear()
            self.descriptionLineEdit.clear()
            self.dateEdit.setDate(QDate.currentDate())
            self.pdvCheckBox.setChecked(True)
            self.totalLineEdit.clear()
            self.itemsTableWidget.setRowCount(0)
            QMessageBox.information(self.window,"Uspjeh","Faktura je obrisana.")

    # ================= EXPORT PDF =================
    def export_selected_invoice_pdf(self):
        selected = self.invoicesTable.selectedItems()
        if not selected:
            QMessageBox.warning(self.window,"Upozorenje","Odaberite fakturu za export")
            return
        row = selected[0].row()
        invoice = self.invoices[row]
        try:
            from utils.pdf_utils import export_invoice_pdf
            export_invoice_pdf(invoice)
            QMessageBox.information(self.window,"Uspjeh",f"Faktura {invoice['invoice_number']} je exportana u PDF")
        except Exception as e:
            QMessageBox.critical(self.window,"Greška",f"Greška pri exportu PDF: {str(e)}")

    # ================= OPEN =================
    def open(self):
        self.window.show()
