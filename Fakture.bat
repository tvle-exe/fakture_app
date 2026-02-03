@echo off
REM ===============================
REM Pokreni Fakture aplikaciju
REM ===============================

REM Folder u kojem se nalazi ova batch skriptaaa
SET APP_DIR=%~dp0

REM Promijeni trenutni folder na folder aplikacije
cd /d "%APP_DIR%"

REM Pokreni app.py bez otvaranja terminala
start "" pythonw.exe "%APP_DIR%app.py"

exit
