import db_operation
from PyQt5.QtCore import QPoint
from PyQt5 import uic
import sys
from main_window import Main_window
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
        self.wrong_login_or_passsword.hide()
        self.wrong_inputs.hide()
        self.registr_btn.clicked.connect(self.registr_clicked)
        self.log_in_btn.clicked.connect(self.log_in_clckd)
        

    def registr_clicked(self):
        self.registr_window = Registr_window()
        self.registr_window.show()


    def log_in_clckd(self):
        self.wrong_login_or_passsword.hide()
        self.wrong_inputs.hide()

        login_input = self.login_input.text()
        password_input = self.password_input.text()
        try_log_in = db_operation.take_id(login_input, password_input)

        if not all((login_input, password_input)):
            self.wrong_inputs.show()
            return None
        
        if not try_log_in:
            self.wrong_login_or_passsword.show()
            return None
        
        main_window_exemplar = Main_window(try_log_in)
        main_window_exemplar.show()
        

        
        