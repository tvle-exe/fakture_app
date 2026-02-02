from PySide6.QtWidgets import QPushButton, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from utils.resource_path import resource_path


class NewClientDialog:
    def __init__(self, client=None, parent=None):
        loader = QUiLoader()
        ui_path = resource_path("ui/new_client_dialog.ui")
        file = QFile(ui_path)

        if not file.open(QFile.ReadOnly):
            raise RuntimeError(f"Ne mogu otvoriti UI file: {ui_path}")

        self.dialog = loader.load(file, parent)
        file.close()

        if self.dialog is None:
            raise RuntimeError("new_client_dialog.ui se nije učitao")

        self.dialog.showMaximized()
        self.dialog.setMinimumSize(900, 700)

        # --- widgeti ---
        self.nameEdit = self.dialog.findChild(QLineEdit, "nameLineEdit")
        self.oibEdit = self.dialog.findChild(QLineEdit, "oibLineEdit")
        self.addressEdit = self.dialog.findChild(QLineEdit, "addressLineEdit")
        self.phoneEdit = self.dialog.findChild(QLineEdit, "phoneLineEdit")
        self.emailEdit = self.dialog.findChild(QLineEdit, "emailLineEdit")

        self.saveButton = self.dialog.findChild(QPushButton, "saveButton")
        self.cancelButton = self.dialog.findChild(QPushButton, "cancelButton")

        self.saveButton.clicked.connect(self.dialog.accept)
        self.cancelButton.clicked.connect(self.dialog.reject)

        # --- edit mode ---
        if client:
            self.nameEdit.setText(client["name"])
            self.oibEdit.setText(client["oib"])
            self.addressEdit.setText(client.get("address", ""))
            self.phoneEdit.setText(client.get("phone", ""))
            self.emailEdit.setText(client.get("email", ""))

    def exec(self) -> bool:
        return self.dialog.exec()

    def get_data(self):
        return {
            "name": self.nameEdit.text(),
            "oib": self.oibEdit.text(),
            "address": self.addressEdit.text() or None,
            "phone": self.phoneEdit.text() or None,
            "email": self.emailEdit.text() or None,
        }
