from PyQt5.QtCore import QPoint
from PyQt5 import uic
import sys
import db_operation
from flower_card_window import Flower_card_window
from flower_card import Flower_card
import datetime
from flower_registr_window import Flower_registr 
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTableWidgetItem,
    QTableWidget
    
    )



class Main_window(QWidget):
    def __init__(self, id: int) -> None:
        super().__init__()
        uic.loadUi('qt_ui/main.ui', self)
        self.user_id = id
        self.flower_name_selected = False
        self.need_water = 0
        self.flower_list = db_operation.load_flowers_for_table(self.user_id)
        
        self.user_login = db_operation.load_login(self.user_id)
        self.setWindowTitle("Flower_manager")
        self.reload_btn.clicked.connect(self.reload)
        self.add_flower_btn.clicked.connect(self.add_card_clckd)
        self.open_flower_btn.clicked.connect(self.open_card_clckd)
        self.delete_flower_btn.clicked.connect(self.delete_card_clckd)
        self.flower_table.clicked.connect(self.get_item)
        self.format_window()


    def format_window(self):
        self.login_lbl.setText(f"Ваш логин: @{self.user_login}")
        need_water_count, flower_lst = 0, list() 
        for item in self.flower_list:
            if datetime.date(*tuple(map(int, item[7].split(".")))) == datetime.datetime.now().date():
                need_water = "да"
                need_water_count += 1
            else: 
                need_water = "нет"
            flower_lst.append((item[1], need_water, item[-2], item[-1], item[3]))        
        
        self.flower_for_water.setText(f"Цветков полить сегодня: {need_water_count}") 

        self.flower_table.setRowCount(len(flower_lst))
        for flower_lst_index, flower in enumerate(flower_lst): 
            for element_index, element in enumerate(flower):
                    self.flower_table.setItem(flower_lst_index, element_index, QTableWidgetItem(element))


    def get_item(self):
        self.flower_name_selected = self.flower_table.selectedItems()[0].text()


    def open_card_clckd(self):
        if self.flower_name_selected:
            flower = Flower_card(*db_operation.load_flower_by_name(self.flower_name_selected, self.user_id))
            self.flower_card_exemplar = Flower_card_window(flower)
            self.flower_card_exemplar.show()


    def add_card_clckd(self):
        self.flower_registr_exemplar = Flower_registr(self.user_id)
        self.flower_registr_exemplar.show()
        self.reload()


    def delete_card_clckd(self):
        db_operation.delete_flower(self.user_id, self.flower_name_selected)
        self.reload()


    def reload(self):
        self.flower_list = db_operation.load_flowers_for_table(self.user_id)
        self.flower_name_selected = False
        self.format_window()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example_window = Main_window(1)
    db_operation.on_start_up()
    example_window.show()
    sys.exit(app.exec())

