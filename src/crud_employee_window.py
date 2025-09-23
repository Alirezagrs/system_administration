from PyQt6.QtWidgets import QDialog, QPushButton, QHBoxLayout, \
    QFrame, QVBoxLayout, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from services.users_employees_operations import create_employee, delete_employee


class UserCrud(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ایجاد کاربر جدید")
        self.initialize_ui()
        self.setModal(True)
        self.show()

    def initialize_ui(self):
        self.setGeometry(360, 150, 800, 400)

        # font
        self._font = QFont("B Titr", 12)

        # fram
        self.vframe = QFrame()
        self.vframe.setStyleSheet("background-color: #f7f5f5;")

        self.hframe = QFrame()
        self.hframe.setStyleSheet("background-color: #f7f5f5;")

        # btns
        self.create_btn = QPushButton()
        self.create_btn.setFont(self._font)
        self.create_btn.setText("ایجاد")
        self.create_btn.clicked.connect(self.create_employee)
        self.create_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.create_btn.setStyleSheet("""
        QPushButton{
            background: #07b813;
            color: white;
            font-size: 12px;
            text-align: center;   
        }
        QPushButton:hover{
            background: #0ecc1b;
            color: white;
            font-size: 12px;
        }
    """)

        self.delete_btn = QPushButton()
        self.delete_btn.setFont(self._font)
        self.delete_btn.setText("حذف")
        self.delete_btn.clicked.connect(self.delete_employee)
        self.delete_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.delete_btn.setStyleSheet("""
        QPushButton{
            background: #d41d08;
            color: white;
            font-size: 12px;
            text-align: center;   
        }
        QPushButton:hover{
            background: #f0260e;
            color: white;
            font-size: 12px;
        }
    """)

        # inputs
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('نام')
        self.name_input.setStyleSheet("""
            QLineEdit{
                font-size: 18px;
                padding: 8px;
                margin-bottom: 50px;
                margin-top: 20px;
                border: 2px solid #CACACA;
                border-radius: 6px;
                font-weight: bold;
            }        
    """)
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText('نام خانوادگی')
        self.last_name_input.setStyleSheet("""
            QLineEdit{
                font-size: 18px;
                padding: 8px;
                margin-bottom: 50px;
                margin-top: 20px;
                border: 2px solid #CACACA;
                border-radius: 6px;
                font-weight: bold;
            }        
    """)
        self.badge_input = QLineEdit()
        self.badge_input.setPlaceholderText('درجه')
        self.badge_input.setStyleSheet("""
            QLineEdit{
                font-size: 18px;
                padding: 8px;
                margin-bottom: 50px;
                margin-top: 20px;
                border: 2px solid #CACACA;
                border-radius: 6px;
                font-weight: bold;
            }        
    """)

        # layout
        self.vlayout_input = QVBoxLayout()
        self.vlayout_input.addWidget(self.name_input)
        self.vlayout_input.addWidget(self.last_name_input)
        self.vlayout_input.addWidget(self.badge_input)
        self.vframe.setLayout(self.vlayout_input)

        self.hlayout_btn = QHBoxLayout()
        self.hlayout_btn.addWidget(self.create_btn)
        self.hlayout_btn.addWidget(self.delete_btn)
        self.hframe.setLayout(self.hlayout_btn)

        self.vlayout_main = QVBoxLayout()
        self.vlayout_main.addWidget(self.vframe)
        self.vlayout_main.addWidget(self.hframe)

        # different with QMainwindow we dont have setCentralWidget()
        self.setLayout(self.vlayout_main)

    def create_employee(self):
        self.name_input_value = self.name_input.text()
        self.last_name_input_value = self.last_name_input.text()
        self.badge_input_value = self.badge_input.text()

        create_employee(
            self.name_input_value,
            self.last_name_input_value,
            self.badge_input_value
        )

        QMessageBox.information(
            self,
            "ثبت موفق",
            "کارمند با موفقیت ثبت شد."
        )

    def delete_employee(self):
        delete_employee(
            self.name_input_value,
            self.last_name_input_value,
            self.badge_input_value
        )
        QMessageBox.information(
            self,
            "حذف موفق",
            "کارمند با موفقیت حذف شد."
        )
