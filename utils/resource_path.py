import sys
import os

def resource_path(relative_path: str) -> str:
    """
    Vrati apsolutnu putanju do resursa, kompatibilnu sa PyInstaller --onefile.
    Ako se aplikacija pokreće iz .exe, koristi privremeni _MEIPASS folder.
    Ako se pokreće iz .py, koristi trenutni folder.
    """
    try:
        # kada je exe
        base_path = sys._MEIPASS
    except AttributeError:
        # kada je normalni Python
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
