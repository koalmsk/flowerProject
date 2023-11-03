from PyQt5.QtWidgets import QApplication
import sys
from python_files.login_window import Login_window
from database import db_operation


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example_window = Login_window()
    db_operation.on_start_up()
    example_window.show()
    sys.exit(app.exec())

