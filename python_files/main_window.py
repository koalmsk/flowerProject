from database import db_operation
from PyQt5.QtCore import QPoint
from PyQt5 import uic
import sys
from login_window import Login_window
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


class Main_window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('qt_ui/main_window.ui', self)
        self.add_flower_btn.clicked.connect(self.add_flower_clicked)

    def add_flower_clicked(self):
        pass
