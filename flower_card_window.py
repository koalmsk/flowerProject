from flower_card import Flower_card
from PyQt5.QtCore import QPoint
from PyQt5 import uic
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

class Flower_card_window(QWidget):
    def __init__(self, config: Flower_card) -> None:
        super().__init__()
        uic.loadUi('qt_ui/flowerCard.ui', self)
        self.formating(config)


    def formating(self, config: Flower_card):
        # название
        self.flower_name.setText(config.name)

        # фото
        self.photo_viewer = QImage(config.photo)
        self.flower_image.setPixmap(QPixmap.fromImage(self.photo_viewer))

        # рекомендации
        self.recomendation_text.setText(config.recomendation)

        # дата рождения цветка
        self.born_date.setText(config.planted)

        # последняя дата
        self.when_water.setText(f"Полит последний раз: {str(config.last_water_date)}")

        # как часто поливать 
        self.how_often_water.setText(f"Дневной интервал поливки: {str(config.how_often_to_water.days)}")

        # чек бокс

        if config.is_water:
            self.is_water.setChecked(bool(config.is_water))
            self.is_water.setDisabled(True)
        else:
            self.is_water.setChecked(bool(config.is_water))
            self.is_water.setEnabled(True)