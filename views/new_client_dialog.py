import os
from PySide6.QtWidgets import QDialog, QPushButton, QLineEdit, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class NewClientDialog(QDialog):
    def __init__(self, client=None, parent=None):
        super().__init__(parent)

        # --- učitaj UI ---
        loader = QUiLoader()
        ui_path = os.path.join("ui", "new_client_dialog.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.content = loader.load(file)
        file.close()

        layout = QVBoxLayout(self)
        layout.addWidget(self.content)
        self.setLayout(layout)

        # --- pronađi widgete ---
        self.nameEdit = self.content.findChild(QLineEdit, "nameLineEdit")
        self.oibEdit = self.content.findChild(QLineEdit, "oibLineEdit")
        self.addressEdit = self.content.findChild(QLineEdit, "addressLineEdit")
        self.phoneEdit = self.content.findChild(QLineEdit, "phoneLineEdit")
        self.emailEdit = self.content.findChild(QLineEdit, "emailLineEdit")

        self.saveButton = self.content.findChild(QPushButton, "saveButton")
        self.cancelButton = self.content.findChild(QPushButton, "cancelButton")

        self.saveButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

        # --- edit mode ---
        if client:
            self.nameEdit.setText(client["name"])
            self.oibEdit.setText(client["oib"])
            self.addressEdit.setText(client.get("address", ""))
            self.phoneEdit.setText(client.get("phone", ""))
            self.emailEdit.setText(client.get("email", ""))

        # --- fullscreen i resizable ---
        self.showMaximized()  # odmah full screen
        self.setMinimumSize(900, 700)  # sprječava da korisnik napravi prozor premali

    def get_data(self):
        return {
            "name": self.nameEdit.text(),
            "oib": self.oibEdit.text(),
            "address": self.addressEdit.text() or None,
            "phone": self.phoneEdit.text() or None,
            "email": self.emailEdit.text() or None,
        }
