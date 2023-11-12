from PyQt5 import uic
import db_operation
import datetime
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import (
    QWidget, 
    QFileDialog,
    QApplication
    
    )

def is_normal_date(date: str) -> bool:
    date = tuple(map(int, date.split(".")))
    return datetime.datetime.now() > datetime.datetime(day=date[2], month=date[1], year=date[0])


def correct_date(date_: str, f=True) -> str:
    if f:
       return ".".join(reversed(tuple(map(lambda x: str(int(x)), date_.split(".")))))
    return ".".join(tuple(map(lambda x: str(int(x)), date_.split("."))))


class Flower_registr(QWidget):
    def __init__(self, id) -> None:
        super().__init__()
        uic.loadUi('qt_ui/flower_registr.ui', self)
        self.id = id
        self.on_start_up()
        self.setWindowTitle("Flower_manager")
        self.photo_input_btn.clicked.connect(self.photo_input_btn_clckd)
        self.save_card_btn.clicked.connect(self.save_flower_clckd)

    def hide_wrongs(self):
        self.flowe_title.setText("Заполните карточку ростения")
        self.wrong_date_lable_1.hide()
        self.wrong_date_lable_2.hide()
        self.wrong_inputs_lable.hide()
        self.wrong_flower_name_lable.hide()
        self.wrong_timedelta.setText("(Дневной Интервал)")

    def on_start_up(self): 
        self.hide_wrongs()       
        self.flower_photo = str()
        self.text_data = list()
        self.last_water_date = str()
        self.when_planted = str()
        self.how_often_to_water_input.setText("0")
        self.last_water_date_input.setCalendarPopup(True)
        self.when_planted_input.setCalendarPopup(True)
        self.last_water_date_input.setDate(datetime.datetime.now().date())
        self.when_planted_input.setDate(datetime.datetime.now().date())


    def get_data(self):
        self.text_data = [
            self.id,
            self.flower_name_input.text(),
            self.flower_photo,
            correct_date(self.when_planted_input.text()),
            self.recomendation_input.toPlainText(),
            self.how_often_to_water_input.text(),
            correct_date(self.last_water_date_input.text())
        ]
        return all(self.text_data)



    def photo_input_btn_clckd(self):
        file_name = QFileDialog.getOpenFileName(
            self, 'Выберите картинку', '', 'Картинка (*.jpg);;Картинка (*.png)')[0]
        
        self.flower_photo = file_name
        if file_name:
            photo  = QImage(file_name)
            pixmap = QPixmap.fromImage(photo)
            self.flower_photo_preview.setScaledContents(True)
            self.flower_photo_preview.setPixmap(pixmap)


    def save_flower_clckd(self) -> None:
        self.hide_wrongs()
        is_all_data_input = self.get_data()

        if not is_all_data_input:
            self.wrong_inputs_lable.show()
            return None

        if not db_operation.is_flower_name_uniq(self.text_data[1], self.id):
            self.wrong_flower_name_lable.show()
            return None
        
        if not self.text_data[-2].isdigit():
            self.wrong_timedelta.setText("Введите числовое значение")
            return None

        if not is_normal_date(self.text_data[-1]):
            self.wrong_date_lable_1.show()
            return None


        if not is_normal_date(self.text_data[3]):
            self.wrong_date_lable_2.show()
            return None
        

        self.text_data.append(correct_date(str(
            datetime.date(
                *tuple(map(int, self.text_data[-1].split(".")))) + datetime.timedelta(days=int(self.text_data[-2]))
                    ).replace("-", "."), False))

        db_operation.insert_flower(self.text_data)
        self.flowe_title.setText(f"Вы успешно зарегистировали ростение {self.text_data[1]}")
        self.save_card_btn.setDisabled(True)
        return None
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example_window = Flower_registr(1)
    db_operation.on_start_up()
    example_window.show()
    sys.exit(app.exec())

