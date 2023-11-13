import db_operation
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QWidget
    )

class Registr_window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('qt_ui/registr.ui', self)
        self.setWindowTitle("Flower_manager")
        self.send_btn.clicked.connect(self.send_btn_clicked)
        self.on_start_up()


    def on_start_up(self):
        self.wrong_login_lable.hide()
        self.wrong_inputs_lable.hide()
        self.wrong_second_passsword.hide()
        self.title_lable.setText("Регистрация")


    def send_btn_clicked(self) -> None:
        self.wrong_login_lable.hide()
        self.wrong_inputs_lable.hide()
        self.wrong_second_passsword.hide()
        self.title_lable.setText("Регистрация")

        input_data = [
            self.login_input_rgstr.text(),
            self.password_input_rgstr.text(),
            self.email_input_rgstr.text(),
            self.password_input_rgstr_2.text(),
        ]
        
        input_data = tuple(map(str, input_data))

        if not all([bool(stroke) for stroke in input_data]):
            self.wrong_inputs_lable.show()
            return None 
        
        if not db_operation.is_login_uniq(input_data[0]):
            self.wrong_login_lable.show()
            return None
        
        if input_data[1] != input_data[-1]:
            self.wrong_second_passsword.show() 
            return None
        
        db_operation.insert_user(user_data=input_data[:-1])
        self.title_lable.setText(f"Вы успешно зарегистрировали пользователя\n{input_data[0]}!")
        return None
    