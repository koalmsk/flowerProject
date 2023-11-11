from flower_card import Flower_card
from PyQt5 import uic
import sys
import db_operation
import datetime
from PyQt5.QtGui import QImage, QPixmap   
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog


class Flower_card_window(QWidget):
    def __init__(self, config: Flower_card) -> None:
        super().__init__()
        uic.loadUi('qt_ui/flower_card.ui', self)
        self.setWindowTitle("Flower_manager")
        self.config = config
        self.formating()
        self.add_new_photo_btn.clicked.connect(self.add_new_photo_clckd)
        self.is_water.stateChanged.connect(self.check_box_clckd)
        self.reload_btn.clicked.connect(self.reload)

    def reload(self):
        reload_name, reload_id = self.config.name, self.config.id
        self.config = Flower_card(*db_operation.load_flower_by_name(reload_name, reload_id))
        self.formating()

        

    def add_new_photo_clckd(self):
        file_name = QFileDialog.getOpenFileName(
            self, 'Выберите новую картинку', '', 'Картинка (*.jpg);;Картинка (*.png)')[0]
        if file_name:
            db_operation.update_flower_card(self.config.id, self.config.name, "photo", file_name)
            self.reload()


    def formating(self):
        # название
        self.flower_name.setText(self.config.name.lower().capitalize())

        # фото
        photo  = QImage(self.config.photo)
        pixmap = QPixmap.fromImage(photo)
        self.flower_image.setScaledContents(True)
        self.flower_image.setPixmap(pixmap)

        # рекомендации
        self.recomendation_text.setText(self.config.recomendation)

        # дата рождения цветка
        self.planted_date.setText(f"Был посажен: {self.config.planted}")

        # последняя дата
        self.when_water.setText(
            f"Полит последний раз: {self.config.last_water_date.strftime('%a %d %b %Y')}")

        # как часто поливать 
        self.how_often_water.setText(
            f"Дневной интервал поливки: {self.config.how_often_to_water.days}")

        # полить следующий раз
        self.next_date.setText(
            f"Дата следующей поливки: {self.config.next_date.strftime('%a %d %b %Y')}"
            )

        # чек бокс
        if datetime.datetime.now().date() < self.config.next_date:
            self.water_info_lable.setText("Сегодня цветок не требует поливки")
            self.is_water.setChecked(True) 
            self.is_water.setDisabled(True)

        if datetime.datetime.now().date() >= self.config.next_date:
            self.water_info_lable.setText("Не задудьте полить цветок сегодня")
            self.is_water.setEnabled(True)

    def check_box_clckd(self):
        if self.is_water.isChecked():
            next_date = str(
                datetime.datetime.now().date() + self.config.how_often_to_water
                ).replace("-", ".")
            
            new_last_water_date = str(datetime.datetime.now().date()).replace("-", ".")
            db_operation.update_flower_card(
                self.config.id, self.config.name, "next_date", next_date
                )
            db_operation.update_flower_card(
                self.config.id, self.config.name, "last_water_date", new_last_water_date
                )

