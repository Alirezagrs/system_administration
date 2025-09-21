from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, \
    QPushButton, QMessageBox, QFrame, QCheckBox, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from sqlalchemy import select

from db.config import create_session
from db.models import Users
from src.manage_window import ManageWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()

    def initialize_ui(self):
        self.setWindowTitle("سیستم ورود و خروج")
        self.showFullScreen()
        self.setStyleSheet("background-color: #4070f4;")

        # Frame
        self.frame = QFrame()
        self.frame.setStyleSheet(
            "background-color: #fff; border: 2px solid white; border-radius: 10px"
            )

        self.frame.setFixedSize(500,400)


        # exit btn
        self.exit_btn = QPushButton()
        self.exit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.exit_btn.setText("خروج")
        self.exit_btn.setStyleSheet("""
        QPushButton{
            color: #fff;
            background-color: #c90808;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            padding: 10px;
            border-radius: 10px;
        }
        QPushButton:hover{
            background-color: #ed1818
        }
""")

        self.exit_btn.clicked.connect(self.exit_handler)
        
        # Login Label
        self.login_label = QLabel()
        self.login_label.setText("صفحه ورود")
        #  نسبت به فریم جابجا میشود بهتره تو لی اوت این کارو بکنی
        # self.login_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.login_label.setStyleSheet("""
            QLabel{
                color: #313333;
                font-size: 25px;
                font-weight: bold;
            }

    """)

        # Inputs
        self.name_input = QLineEdit()
        self.password_input = QLineEdit()
        self.name_input.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                padding: 8px;
                border: 2px solid #CACACA;
                border-radius: 6px;
                font-weight: bold;
            }
    
    """)
        self.password_input.setStyleSheet("""
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
        self.name_input.setPlaceholderText("نام")
        self.password_input.setPlaceholderText("رمز عبور")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # check box
        self.check_box = QCheckBox()
        self.check_box.setText("نمایش رمز عبور")
        self.check_box.setStyleSheet("""
            QCheckBox{
                font-size: 14px;
                color: #2c3e50;        
            }
    """)
        self.check_box.toggled.connect(self.is_checked_checkbox)

        # Login button
        self.login_btn = QPushButton(text="ورود")
        self.login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
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
                background-color: #112cf7;
                
            }
    """)
        self.login_btn.clicked.connect(self.login_btn_clicked)
    
        # layout
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.login_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.name_input)
        self.vlayout.addWidget(self.password_input)
        self.vlayout.addWidget(self.check_box, alignment=Qt.AlignmentFlag.AlignRight)
        self.vlayout.addWidget(self.login_btn)
        self.vlayout.addWidget(self.exit_btn)
        self.frame.setLayout(self.vlayout)

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addWidget(self.frame, alignment=Qt.AlignmentFlag.AlignHCenter)  
        main_layout.addStretch()

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


    def login_btn_clicked(self):
        with create_session() as session:
            user = select(Users).where(
                Users.name == self.name_input.text(),
                Users.password == self.password_input.text()
            )
            result = session.execute(user).scalar_one_or_none()

            try:
                if result:
                    self.manage_window = ManageWindow(user_name=result.name)
                    self.close()
                else:
                    QMessageBox.information(
                        self.frame, "خطا", "نام یا رمز عبور اشتباه است")
            except:
                QMessageBox.information(
                    self.frame, "خطا", "نام یا رمز عبور اشتباه است")

    def is_checked_checkbox(self, checked):
        if checked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
    
    def exit_handler(self):
        self.close()

