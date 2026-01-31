import os
from PySide6.QtWidgets import QPushButton, QComboBox, QLineEdit, QDateEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from PySide6.QtWidgets import QHeaderView, QTableWidget
from .new_client_dialog import NewClientDialog





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

        # postavi današnji datum
        self.dateEdit = self._dialog.findChild(QDateEdit, "dateEdit")
        self.dateEdit.setDate(QDate.currentDate())


        self.tableWidget = self._dialog.findChild(QTableWidget, "itemsTableWidget")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        file.close()

        
        self.saveButton = self._dialog.findChild(QPushButton, "saveButton")
        self.closeButton = self._dialog.findChild(QPushButton, "closeButton")

        self.clientComboBox = self._dialog.findChild(QComboBox, "clientComboBox")
        self.addClientButton = self._dialog.findChild(QPushButton, "addClientButton")
        self.addClientButton.clicked.connect(self.open_new_client_dialog)
        self.descriptionLineEdit = self._dialog.findChild(QLineEdit, "descriptionLineEdit")

    def open(self):
        self._dialog.show()

    def close(self):
        self._dialog.close()

    def open_new_client_dialog(self):
        dialog = NewClientDialog(parent=self._dialog)
        result = dialog.open()

        if result:
            print("Novi klijent spremljen (TODO: refresh ComboBox)")

