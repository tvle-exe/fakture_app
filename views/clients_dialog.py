from PySide6.QtWidgets import QPushButton, QTableWidget, QHeaderView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from views.base_dialog import BaseDialog
from utils.resource_path import resource_path


class ClientsDialog:
    def __init__(self, parent=None):
        loader = QUiLoader()
        ui_path = resource_path("ui/clients_dialog.ui")
        file = QFile(ui_path)

        if not file.open(QFile.ReadOnly):
            raise RuntimeError(f"Ne mogu otvoriti UI file: {ui_path}")

        self.dialog = loader.load(file, parent)  # parent=main window
        file.close()

        if self.dialog is None:
            raise RuntimeError("clients_dialog.ui se nije učitao")

        self.dialog.setWindowTitle("Klijenti")

        # BaseDialog wrapper za fullscreen i resize
        self.base = BaseDialog(parent=parent, width=900, height=700, resizable=True)
        self.dialog.resize(900, 700)
        self.dialog.showMaximized()  # fullscreen

        # --- tablica ---
        self.table = self.dialog.findChild(QTableWidget, "clientsTableWidget")
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # --- gumbi ---
        self.addButton = self.dialog.findChild(QPushButton, "addClientButton")
        self.editButton = self.dialog.findChild(QPushButton, "editClientButton")
        self.deleteButton = self.dialog.findChild(QPushButton, "deleteClientButton")
        self.closeButton = self.dialog.findChild(QPushButton, "closeButton")
        self.closeButton.clicked.connect(self.dialog.close)

    def show(self):
        self.dialog.show()
