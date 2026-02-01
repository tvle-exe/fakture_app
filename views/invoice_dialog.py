import os
from PySide6.QtWidgets import (
    QPushButton, QComboBox, QLineEdit, QDateEdit,
    QHeaderView, QTableWidget, QTableWidgetItem, QCheckBox
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate, Qt

from .new_client_dialog import NewClientDialog
from repositories.client_repository import ClientRepository


def to_float(text: str) -> float:
    if not text:
        return 0.0
    return float(text.replace(",", "."))


class InvoiceDialog:
    def __init__(self):
        loader = QUiLoader()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.normpath(os.path.join(base_dir, "..", "ui", "invoice_dialog.ui"))
        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self._dialog = loader.load(file)
        file.close()

        # --- fullscreen i resizable ---
        self._dialog.showMaximized()
        self._dialog.setMinimumSize(900, 700)  # sprječava da dijalog postane premali

        # ================================
        # PUBLIC UI
        # ================================
        self.closeButton = self._dialog.findChild(QPushButton, "closeButton")
        self.saveButton = self._dialog.findChild(QPushButton, "saveButton")
        self.addItemButton = self._dialog.findChild(QPushButton, "addItemButton")
        self.removeItemButton = self._dialog.findChild(QPushButton, "removeItemButton")
        self.addClientButton = self._dialog.findChild(QPushButton, "addClientButton")

        self.invoiceNumberLineEdit = self._dialog.findChild(QLineEdit, "invoiceNumberLineEdit")
        self.clientComboBox = self._dialog.findChild(QComboBox, "clientComboBox")
        self.descriptionLineEdit = self._dialog.findChild(QLineEdit, "descriptionLineEdit")
        self.dateEdit = self._dialog.findChild(QDateEdit, "dateEdit")
        self.totalLineEdit = self._dialog.findChild(QLineEdit, "totalLineEdit")
        self.table = self._dialog.findChild(QTableWidget, "itemsTableWidget")
        self.pdvCheckBox = self._dialog.findChild(QCheckBox, "pdvCheckBox")

        # ================================
        # INIT
        # ================================
        self.dateEdit.setDate(QDate.currentDate())
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.cellChanged.connect(self.recalculate_row)

        self.addItemButton.clicked.connect(self.add_item)
        self.removeItemButton.clicked.connect(self.remove_item)

        self.addClientButton.clicked.connect(self.open_new_client_dialog)
        self.addClientButton.setMaximumWidth(30)  

        # ================================
        # DATA
        # ================================
        self.client_repo = ClientRepository()
        self.reload_clients()

    # ================================
    # DIALOG CONTROL
    # ================================
    def open(self):
        self._dialog.show()

    def close(self):
        self._dialog.close()

    # ================================
    # ITEMS
    # ================================
    def add_item(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(""))
        self.table.setItem(row, 1, QTableWidgetItem("1"))
        self.table.setItem(row, 2, QTableWidgetItem("kom"))
        total_item = QTableWidgetItem("0,00")
        total_item.setFlags(Qt.ItemIsEnabled)
        self.table.setItem(row, 4, total_item)

    def remove_item(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)
            self.recalculate_total()

    def recalculate_row(self, row, column):
        if column not in (1, 3):
            return
        qty_item = self.table.item(row, 1)
        price_item = self.table.item(row, 3)
        if not qty_item or not price_item:
            return
        try:
            total = to_float(qty_item.text()) * to_float(price_item.text())
        except Exception:
            total = 0.0
        if not self.table.item(row, 4):
            self.table.setItem(row, 4, QTableWidgetItem())
        self.table.blockSignals(True)
        self.table.item(row, 4).setText(f"{total:.2f}")
        self.table.blockSignals(False)
        self.recalculate_total()

    def recalculate_total(self):
        total = sum(to_float(self.table.item(r, 4).text()) for r in range(self.table.rowCount()) if self.table.item(r, 4))
        if self.pdvCheckBox.isChecked():
            total *= 1.25
        self.totalLineEdit.setText(f"{total:.2f}")

    # ================================
    # CLIENTS
    # ================================
    def open_new_client_dialog(self):
        dialog = NewClientDialog(parent=self._dialog)
        if dialog.exec():
            self.client_repo.add(dialog.get_data())
            self.reload_clients()

    def reload_clients(self):
        self.clientComboBox.clear()
        for c in self.client_repo.get_all():
            self.clientComboBox.addItem(c["name"], c)

    # ================================
    # DATA COLLECTION (for controller)
    # ================================
    def collect_invoice_data(self) -> dict:
        items = [
            {
                "description": self.table.item(r, 0).text(),
                "quantity": to_float(self.table.item(r, 1).text()),
                "unit": self.table.item(r, 2).text(),
                "price": to_float(self.table.item(r, 3).text()),
                "total": to_float(self.table.item(r, 4).text()),
            }
            for r in range(self.table.rowCount())
        ]

        total = sum(item["total"] for item in items)
        pdv_included = self.pdvCheckBox.isChecked()
        if pdv_included:
            total *= 1.25

        self.totalLineEdit.setText(f"{total:.2f}")

        return {
            "invoice_number": self.invoiceNumberLineEdit.text(),
            "client": self.clientComboBox.currentText(),
            "description": self.descriptionLineEdit.text(),
            "date": self.dateEdit.date().toString("yyyy-MM-dd"),
            "items": items,
            "total": total,
            "pdv_included": pdv_included
        }
