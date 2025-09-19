import os
from pathlib import Path

from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, \
    QPushButton, QMessageBox
from PyQt6.QtGui import QFont
from sqlalchemy import select

from db.config import create_session
from db.models import Users


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()

    def initialize_ui(self):
        self.setWindowTitle("سیستم ورود و خروج")
        self.setFixedSize(1280, 735)
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #7693d6,
                    stop:1 #d8ebe6
                );
            }
        """)
        shabnam_font_path = os.path.join(
            Path(__file__).parent.parent, "utils\\shabnam.ttf")

        self.name = QLabel("اسم: ", self)
        self.password = QLabel("رمز عبور: ", self)
        self.name.setFont(QFont(shabnam_font_path, 15))
        self.password.setFont(QFont(shabnam_font_path, 15))
        self.name.move(750, 255)
        self.password.move(750, 355)

        self.name_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        self.name_input.resize(150, 50)
        self.password_input.resize(100, 50)
        self.name_input.move(650, 250)
        self.password_input.move(650, 350)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_btn = QPushButton(text="ورود", parent=self)
        self.login_btn.move(650, 420)
        self.login_btn.clicked.connect(self.login_btn_clicked)

    def login_btn_clicked(self):
        with create_session() as session:
            user = select(Users).where(
                Users.name==self.name_input.text(),
                Users.password==self.password_input.text()
            )
            result = session.execute(user).scalar_one_or_none()
            
            try:
                if result:
                    self.close()
                else:
                    QMessageBox.information(self, "خطا", "نام یا رمز عبور اشتباه است")
            except Exception as e:
                print(e)
                QMessageBox.information(self, "خطا", "نام یا رمز عبور اشتباه است")