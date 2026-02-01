import json
import os


class ClientRepository:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.normpath(
            os.path.join(base_dir, "..", "data", "clients.json")
        )

        if not os.path.exists(self.file_path):
            self._save([])

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_all(self):
        return self._load()

    def add(self, client):
        clients = self._load()
        clients.append(client)
        self._save(clients)

    def update(self, index, client):
        clients = self._load()
        clients[index] = client
        self._save(clients)

    def delete(self, index):
        clients = self._load()
        clients.pop(index)
        self._save(clients)
