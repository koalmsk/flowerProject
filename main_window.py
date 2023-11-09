from PyQt5.QtCore import QPoint
from PyQt5 import uic
import sys
import db_operation
from flower_card_window import Flower_card_window
from flower_card import Flower_card
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
        self.flower_list = db_operation.load_flowers_for_table(self.user_id)
        
        self.user_login = db_operation.load_login(self.user_id)

        self.reload_btn.clicked.connect(self.reload)
        self.add_flower_btn.clicked.connect(self.add_card_clckd)
        self.open_flower_btn.clicked.connect(self.open_card_clckd)
        self.delete_flower_btn.clicked.connect(self.delete_card_clckd)
        self.flower_table.clicked.connect(self.get_item)
        self.format_window()



    def format_window(self):
        flower_lst = list(map(lambda x: (x[1], x[3], x[6], x[7]), self.flower_list))
        self.login_lbl.setText(f"Ваш логин: @{self.user_login}")
        self.flower_table.setRowCount(len(flower_lst))

        for flower_lst_index, flower in enumerate(flower_lst): 
            for element_index, element in enumerate(flower):
                    self.flower_table.setItem(flower_lst_index, element_index, QTableWidgetItem(element))
        self.flower_table.setColumnWidth(2, 230)


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
    example_window = Main_window(6)
    db_operation.on_start_up()
    example_window.show()
    sys.exit(app.exec())

