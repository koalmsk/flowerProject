from PyQt5.QtCore import QPoint
from PyQt5 import uic
import sys
import db_operation
import datetime
from PyQt5.QtGui import QImage, QPixmap   
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QDateEdit,
    QCalendarWidget,
    QLabel,
    QCheckBox,
    QPlainTextEdit,
    QFileDialog
    )

def is_normal_date(date: str) -> bool:
    date = tuple(map(int, date.split(".")))
    return datetime.datetime.now() > datetime.datetime(day=date[0], month=date[1], year=date[2])



class Flower_registr(QWidget):
    def __init__(self, id) -> None:
        super().__init__()
        uic.loadUi('qt_ui/flower_registr.ui', self)
        self.id = id
        self.on_start_up()
        self.photo_input_btn.clicked.connect(self.photo_input_btn_clckd)
        self.save_card_btn.clicked.connect(self.save_flower_clckd)

    def hide_wrongs(self):
        # self.flowe_title.setText("Заполните карточку ростения")
        self.wrong_date_lable_1.hide()
        self.wrong_date_lable_2.hide()
        self.wrong_inputs_lable.hide()
        self.wrong_flower_name_lable.hide()
        self.flower_photo_directory_lable.hide()

    def on_start_up(self): 
        self.hide_wrongs()       
        self.flower_photo = str()
        self.text_data = list()
        self.last_water_date = str()
        self.when_planted = str()
        self.last_water_date_input.setCalendarPopup(True)
        self.when_planted_input.setCalendarPopup(True)

    def get_data(self):
        self.text_data = (
            self.id,
            self.flower_name_input.text(),
            self.flower_photo,
            self.when_planted_input.text(),
            self.recomendation_input.toPlainText(),
            self.how_often_to_water_input.text(),
            self.last_water_date_input.text(),
        )
        
        print(self.text_data)
        return all(self.text_data)



    def photo_input_btn_clckd(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинка (*.jpg);;Картинка (*.png)')[0]
        self.flower_photo = file_name
        self.flower_photo_directory_lable.setText(file_name)
        self.flower_photo_directory_lable.show()


    def save_flower_clckd(self) -> None:
        self.hide_wrongs()
        is_all_data_input = self.get_data()

        if not is_all_data_input:
            self.wrong_inputs_lable.show()
            return None

        if not db_operation.is_flower_name_uniq(self.text_data[1], self.id):
            self.wrong_flower_name_lable.show()
            return None
        
        if not is_normal_date(self.text_data[-1]):
            self.wrong_date_lable_1.show()
            return None


        if not is_normal_date(self.text_data[3]):
            self.wrong_date_lable_2.show()
            return None

        db_operation.insert_flower(self.text_data)
        # self.flowe_title.setText("Вы успешно зарегистировали ростение")
        return None
    

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    example_window = Flower_registr(1)
    example_window.show()
    sys.exit(app.exec())
    