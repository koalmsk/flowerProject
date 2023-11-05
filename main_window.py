import db_operation
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
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QCheckBox,
    QPlainTextEdit,
    QFileDialog
    )



class Main_window(QWidget):
    def __init__(self, id: int) -> None:
        super().__init__()
        uic.loadUi('qt_ui/main.ui', self)
        self.user_id = id
        self.flower_list = db_operation.load_flowers_for_table(self.user_id)
        self.user_login = db_operation.load_login(self.user_id)

        self.add_flower_btn.clicked.connect(self.add_card_clckd)
        self.open_flower_btn.clicked.connect(self.open_card_clckd)
        self.delete_flower_btn.clicked.connect(self.delete_card)
        self.format_window()

    def format_window(self):
        self.login_lbl.setText(f"Ваш логин: @{self.user_login}")
        self.flower_table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        self.flower_table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.flower_table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
        


    def open_card_clckd(self):
        pass


    def add_card_clckd(self):
        pass


    def delete_card(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example_window = Main_window(1)
    example_window.show()
    sys.exit(app.exec())
    