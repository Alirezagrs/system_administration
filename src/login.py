import os
from pathlib import Path

from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, \
    QPushButton, QMessageBox, QFrame
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
        self.setStyleSheet("background-color: #4070f4;")

        self.frame = QFrame(self)
        self.frame.setStyleSheet(
            "background-color: #fff; border: 2px solid white; border-radius: 10px")
        self.frame.setGeometry(400, 100, 500, 550)

        self.login_label = QLabel(self.frame)
        self.login_label.setText("صفحه ورود")
        self.login_label.move(185,20)
        self.login_label.setStyleSheet("""
            QLabel{
                color: #313333;
                font-size: 25px;
                font-weight: bold;
            }

    """)

        self.name_input = QLineEdit(self.frame)
        self.password_input = QLineEdit(self.frame)
        self.name_input.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                border: 2px solid #CACACA;
                border-radius: 6px;
                font-weight: bold;
            }
    
    """)
        self.password_input.setStyleSheet("""
            QLineEdit{
                font-size: 18px;
                border: 2px solid #CACACA;
                border-radius: 6px;
                font-weight: bold;                          
            }               
    """)
        self.name_input.setPlaceholderText("نام")
        self.password_input.setPlaceholderText("رمز عبور")
        self.name_input.resize(400, 50)
        self.password_input.resize(400, 50)
        self.name_input.move(50, 120)
        self.password_input.move(50, 223)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_btn = QPushButton(text="ورود", parent=self.frame)
        self.login_btn.setStyleSheet("""
            QPushButton{
                color: #fff;
                background-color: #0171d3;
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                padding: 10px;
                border-radius: 10px;
            }
                                     
            QPushButton:hover {
                background-color: #016dcb;
                
            }
    """)
        self.login_btn.resize(402, 50)
        self.login_btn.move(50, 330)
        self.login_btn.clicked.connect(self.login_btn_clicked)

    def login_btn_clicked(self):
        with create_session() as session:
            user = select(Users).where(
                Users.name == self.name_input.text(),
                Users.password == self.password_input.text()
            )
            result = session.execute(user).scalar_one_or_none()

            try:
                if result:
                    self.close()
                else:
                    QMessageBox.information(
                        self.frame, "خطا", "نام یا رمز عبور اشتباه است")
            except Exception as e:
                print(e)
                QMessageBox.information(
                    self.frame, "خطا", "نام یا رمز عبور اشتباه است")
