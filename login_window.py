import db_operation
from PyQt5.QtCore import QPoint
from PyQt5 import uic
import sys
from registr_window import Registr_window
import datetime
from PyQt5.QtGui import QImage, QPixmap   
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QCheckBox,
    QPlainTextEdit,
    QFileDialog
    )


class Login_window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('qt_ui/login.ui', self)
        self.show()
        self.registr_btn.clicked.connect(self.registr_clicked)
        

    def registr_clicked(self):
        self.registr_window = Registr_window()
        self.registr_window.show()


        
