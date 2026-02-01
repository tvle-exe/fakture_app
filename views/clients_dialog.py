import os
from PySide6.QtWidgets import QDialog, QPushButton, QTableWidget, QVBoxLayout, QHeaderView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class ClientsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # --- učitaj UI ---
        loader = QUiLoader()
        ui_path = os.path.join("ui", "clients_dialog.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        content = loader.load(file)
        file.close()

        layout = QVBoxLayout(self)
        layout.addWidget(content)
        self.setLayout(layout)

        self.setWindowTitle("Klijenti")

        # --- tablica ---
        self.table = content.findChild(QTableWidget, "clientsTableWidget")
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # --- gumbi ---
        self.addButton = content.findChild(QPushButton, "addClientButton")
        self.editButton = content.findChild(QPushButton, "editClientButton")
        self.deleteButton = content.findChild(QPushButton, "deleteClientButton")
        self.closeButton = content.findChild(QPushButton, "closeButton")
        self.closeButton.clicked.connect(self.close)

        # --- fullscreen i resizable ---
        self.showMaximized()           # otvoreno fullscreen
        self.setMinimumSize(900, 700)  # sprječava da korisnik napravi dijalog premali
