import os
from PySide6.QtWidgets import QPushButton, QComboBox, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QHeaderView, QTableWidget



class InvoiceDialog:
    def __init__(self):
        loader = QUiLoader()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(base_dir, "..", "ui", "invoice_dialog.ui")

        ui_path = os.path.normpath(ui_path)

        file = QFile(ui_path)
        if not file.open(QFile.ReadOnly):
            raise RuntimeError(f"Ne mogu otvoriti UI file: {ui_path}")

        self._dialog = loader.load(file)

        self.tableWidget = self._dialog.findChild(QTableWidget, "itemsTableWidget")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        file.close()

        
        self.saveButton = self._dialog.findChild(QPushButton, "saveButton")
        self.closeButton = self._dialog.findChild(QPushButton, "closeButton")

        self.clientComboBox = self._dialog.findChild(QComboBox, "clientComboBox")
        self.descriptionLineEdit = self._dialog.findChild(QLineEdit, "descriptionLineEdit")

    def open(self):
        self._dialog.show()

    def close(self):
        self._dialog.close()
