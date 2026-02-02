import sys
from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainController
from utils.resource_path import resource_path


def main():
    app = QApplication(sys.argv)

    # ================= Učitaj style.qss =================
    try:
        qss_file = resource_path("assets/style.qss")
        with open(qss_file, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except Exception as e:
        print(f"Greška pri učitavanju style.qss: {e}")


    controller = MainController()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
