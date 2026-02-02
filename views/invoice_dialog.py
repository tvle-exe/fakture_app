from PySide6.QtWidgets import (
    QPushButton, QComboBox, QLineEdit, QDateEdit,
    QHeaderView, QTableWidget, QTableWidgetItem, QCheckBox
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate, Qt

from utils.resource_path import resource_path
from .new_client_dialog import NewClientDialog
from repositories.client_repository import ClientRepository


def to_float(text: str) -> float:
    if not text:
        return 0.0
    text = text.replace(",", ".").replace("€", "").replace("EUR", "").strip()
    try:
        return float(text)
    except ValueError:
        return 0.0


class InvoiceDialog:
    def __init__(self):
        loader = QUiLoader()
        ui_path = resource_path("ui/invoice_dialog.ui")
        file = QFile(ui_path)

        if not file.open(QFile.ReadOnly):
            raise RuntimeError(f"Ne mogu otvoriti UI file: {ui_path}")

        self._dialog = loader.load(file)
        file.close()

        if self._dialog is None:
            raise RuntimeError("invoice_dialog.ui se nije učitao")

        # --- fullscreen i resizable ---
        self._dialog.showMaximized()
        self._dialog.setMinimumSize(900, 700)

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
        # računamo samo kad se mijenja količina ili cijena
        if column not in (1, 3):
            return

        qty_item = self.table.item(row, 1)
        price_item = self.table.item(row, 3)

        if not qty_item or not price_item:
            return

        # formatiraj cijenu po jedinici s 2 decimale i € znak
        if price_item:
            price_item.setText(f"{to_float(price_item.text()):.2f} €")

        try:
            total = to_float(qty_item.text()) * to_float(price_item.text())
        except Exception:
            total = 0.0

        # provjeri postoji li ćelija za ukupni iznos
        if not self.table.item(row, 4):
            self.table.setItem(row, 4, QTableWidgetItem())

        # blokiraj signale kako bi spriječili beskonačno rekurzivno pozivanje
        self.table.blockSignals(True)
        self.table.item(row, 4).setText(f"{total:.2f} €")
        self.table.blockSignals(False)

        # ažuriraj ukupni iznos
        self.recalculate_total()


    def recalculate_total(self):
        total = sum(
            to_float(self.table.item(r, 4).text())
            for r in range(self.table.rowCount())
            if self.table.item(r, 4)
        )
        if self.pdvCheckBox.isChecked():
            total *= 1.25
        self.totalLineEdit.setText(f"{total:.2f} €")

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

    def collect_invoice_data(self):
        items = []
        for row in range(self.table.rowCount()):
            description_item = self.table.item(row, 0)
            quantity_item = self.table.item(row, 1)
            unit_item = self.table.item(row, 2)
            price_item = self.table.item(row, 3)
            total_item = self.table.item(row, 4)

            if description_item is None:
                continue

            items.append({
                "description": description_item.text(),
                "quantity": to_float(quantity_item.text()) if quantity_item else 0,
                "unit": unit_item.text() if unit_item else "",
                "price": to_float(price_item.text()) if price_item else 0,
                "total": to_float(total_item.text()) if total_item else 0
            })

        client_data = self.clientComboBox.currentData()
        client_name = client_data["name"] if client_data else ""

        return {
            "invoice_number": self.invoiceNumberLineEdit.text(),
            "client": client_name,
            "description": self.descriptionLineEdit.text(),
            "date": self.dateEdit.date().toString("yyyy-MM-dd"),
            "items": items,
            "pdv_included": self.pdvCheckBox.isChecked(),
            "total": to_float(self.totalLineEdit.text())
        }