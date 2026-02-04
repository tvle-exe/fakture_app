from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from controllers.invoice_controller import InvoiceController
from controllers.clients_controller import ClientsController
from controllers.history_controller import HistoryController
import os
import sys
import subprocess


class MainController:
    def __init__(self):
        self.window = MainWindow()
        self.connect_signals()
        self.window.show()

    def connect_signals(self):
        self.window.ui.exitButton.clicked.connect(QApplication.quit)
        self.window.ui.novaFakturaButton.clicked.connect(self.open_invoice)
        self.window.ui.clientsButton.clicked.connect(self.open_clients)
        self.window.ui.povijestFakturaButton.clicked.connect(self.open_history)
        self.window.ui.openPdfFolderButton.clicked.connect(self.open_pdf_folder)

    def open_invoice(self):
        self.invoice_controller = InvoiceController()
        self.invoice_controller.open()

    def open_clients(self):
        self.clients_controller = ClientsController()
        self.clients_controller.open()

    def open_history(self): 
        self.history_controller = HistoryController()
        self.history_controller.open()

    def open_pdf_folder(self):
        # putanja do pdf foldera u rootu
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        pdf_dir = os.path.join(base_dir, "pdf")
        os.makedirs(pdf_dir, exist_ok=True)

        if sys.platform == "win32":
            os.startfile(pdf_dir)
        elif sys.platform == "darwin":
            subprocess.run(["open", pdf_dir])
        else:  # linux
            subprocess.run(["xdg-open", pdf_dir])