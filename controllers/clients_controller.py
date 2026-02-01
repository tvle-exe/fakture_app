from PySide6.QtWidgets import QMessageBox
from views.clients_dialog import ClientsDialog
from views.new_client_dialog import NewClientDialog
from repositories.client_repository import ClientRepository


class ClientsController:
    def __init__(self):
        self.dialog = ClientsDialog()
        self.repo = ClientRepository()

        self.dialog.addButton.clicked.connect(self.add_client)
        self.dialog.editButton.clicked.connect(self.edit_client)
        self.dialog.deleteButton.clicked.connect(self.delete_client)

        self.load_clients()

    def open(self):
        self.dialog.show()

    def load_clients(self):
        self.dialog.table.setRowCount(0)
        clients = self.repo.get_all()

        for row, client in enumerate(clients):
            self.dialog.table.insertRow(row)
            self.dialog.table.setItem(row, 0, self._item(client["name"]))
            self.dialog.table.setItem(row, 1, self._item(client["oib"]))
            self.dialog.table.setItem(row, 2, self._item(client.get("address", "")))
            self.dialog.table.setItem(row, 3, self._item(client.get("phone", "")))
            self.dialog.table.setItem(row, 4, self._item(client.get("email", "")))

    def add_client(self):
        dialog = NewClientDialog()
        if dialog.exec():
            self.repo.add(dialog.get_data())
            self.load_clients()

    def edit_client(self):
        row = self.dialog.table.currentRow()
        if row < 0:
            return

        client = self.repo.get_all()[row]
        dialog = NewClientDialog(client)

        if dialog.exec():
            self.repo.update(row, dialog.get_data())
            self.load_clients()

    def delete_client(self):
        row = self.dialog.table.currentRow()
        if row < 0:
            return

        reply = QMessageBox.question(
            self.dialog,
            "Potvrda",
            "Sigurno želiš obrisati klijenta?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.repo.delete(row)
            self.load_clients()

    def _item(self, text):
        from PySide6.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(text)
