# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.novaFakturaButton = QPushButton(self.centralwidget)
        self.novaFakturaButton.setObjectName(u"novaFakturaButton")
        font1 = QFont()
        font1.setPointSize(16)
        self.novaFakturaButton.setFont(font1)

        self.verticalLayout.addWidget(self.novaFakturaButton)

        self.povijestFakturaButton = QPushButton(self.centralwidget)
        self.povijestFakturaButton.setObjectName(u"povijestFakturaButton")
        self.povijestFakturaButton.setFont(font1)

        self.verticalLayout.addWidget(self.povijestFakturaButton)

        self.clientsButton = QPushButton(self.centralwidget)
        self.clientsButton.setObjectName(u"clientsButton")
        self.clientsButton.setFont(font1)

        self.verticalLayout.addWidget(self.clientsButton)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setFont(font1)

        self.verticalLayout.addWidget(self.exitButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fakture App", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fakture App", None))
        self.novaFakturaButton.setText(QCoreApplication.translate("MainWindow", u"Nova faktura", None))
        self.povijestFakturaButton.setText(QCoreApplication.translate("MainWindow", u"Povijest faktura", None))
        self.clientsButton.setText(QCoreApplication.translate("MainWindow", u"Klijenti", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Izlaz", None))
    # retranslateUi

