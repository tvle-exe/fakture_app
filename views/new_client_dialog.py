import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QDialog, QPushButton, QLineEdit


class NewClientDialog:
    def __init__(self, parent=None):
        loader = QUiLoader()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.normpath(
            os.path.join(base_dir, "..", "ui", "new_client_dialog.ui")
        )

        file = QFile(ui_path)
        if not file.open(QFile.ReadOnly):
            raise RuntimeError(f"Ne mogu otvoriti UI file: {ui_path}")

        self._dialog: QDialog = loader.load(file, parent)
        file.close()

        # polja
        self.nameLineEdit = self._dialog.findChild(QLineEdit, "nameLineEdit")
        self.oibLineEdit = self._dialog.findChild(QLineEdit, "oibLineEdit")
        self.addressLineEdit = self._dialog.findChild(QLineEdit, "addressLineEdit")
        self.phoneLineEdit = self._dialog.findChild(QLineEdit, "phoneLineEdit")
        self.emailLineEdit = self._dialog.findChild(QLineEdit, "emailLineEdit")

        # gumbi
        self.saveButton = self._dialog.findChild(QPushButton, "saveButton")
        self.cancelButton = self._dialog.findChild(QPushButton, "cancelButton")

        # view smije samo zatvoriti dialog, bez poslovne logike
        self.cancelButton.clicked.connect(self._dialog.reject)

    def open(self):
        return self._dialog.exec()

    def accept(self):
        self._dialog.accept()

    def reject(self):
        self._dialog.reject()
