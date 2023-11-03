from PyQt5.QtCore import QPoint
from PyQt5 import uic
import sys
from database import db_operation
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


class Flower_registr(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('qt_ui/flower_registr.ui', self)
        self.flower_photo = str()
        self.text_data = list()
        self.photo_input_btn.clicked.connect(self.photo_input_btn_clckd)
        self.on_start_up()

    def on_start_up(self):
        self.flower_photo_directory_lable.hide()


    def get_text_data(self):
        self.text_data = [
            self.flower_name_input.text(),
            self.how_often_to_water_input.text(),
            self.recomendation_input.text(),
            self.flower_photo
        ]

        return all(self.text_data)


    def photo_input_btn_clckd(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинка (*.jpg);;Картинка (*.png)')[0]
        self.flower_photo = file_name
        self.flower_photo_directory_lable.setText(file_name)
        self.flower_photo_directory_lable.show()
    




    

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    example_window = Flower_registr()
    example_window.show()
    sys.exit(app.exec())
    