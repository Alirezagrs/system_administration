from PyQt6.QtWidgets import QDialog, QPushButton, QHBoxLayout,\
    QFrame, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class UserCrud(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ایجاد کاربر جدید")
        self.initialize_ui()
        self.setModal(True)
        self.show()

    def initialize_ui(self):
        self.setGeometry(360,150,800,400)

        #font
        self._font = QFont("B Titr", 12)

        #fram
        self.vframe = QFrame()
        self.vframe.setStyleSheet("background-color: #f7f5f5;")


        self.hframe = QFrame()
        self.hframe.setStyleSheet("background-color: #f7f5f5;")


        #btns
        self.create_btn = QPushButton()
        self.create_btn.setFont(self._font)
        self.create_btn.setText("ایجاد")
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
        self.edit_btn = QPushButton()
        self.edit_btn.setFont(self._font)
        self.edit_btn.setText("ویرایش")
        self.edit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.edit_btn.setStyleSheet("""
        QPushButton{
            background: #78716f;
            color: white;
            font-size: 12px;
            text-align: center;   
        }
        QPushButton:hover{
            background: #8a8280;
            color: white;
            font-size: 12px;
        }
    """)

        #inputs
        self.create_input = QLineEdit()
        self.create_input.setPlaceholderText('نام')
        self.create_input.setStyleSheet("""
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
        self.delete_input = QLineEdit()
        self.delete_input.setPlaceholderText('نام خانوادگی')
        self.delete_input.setStyleSheet("""
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
        self.edit_input = QLineEdit()
        self.edit_input.setPlaceholderText('درجه')
        self.edit_input.setStyleSheet("""
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

        #layout
        self.vlayout_input = QVBoxLayout()
        self.vlayout_input.addWidget(self.create_input)
        self.vlayout_input.addWidget(self.delete_input)
        self.vlayout_input.addWidget(self.edit_input)
        self.vframe.setLayout(self.vlayout_input)

        self.hlayout_btn = QHBoxLayout()
        self.hlayout_btn.addWidget(self.create_btn)
        self.hlayout_btn.addWidget(self.delete_btn)
        self.hlayout_btn.addWidget(self.edit_btn)
        self.hframe.setLayout(self.hlayout_btn)

        self.vlayout_main = QVBoxLayout()
        self.vlayout_main.addWidget(self.vframe)
        self.vlayout_main.addWidget(self.hframe)


        self.setLayout(self.vlayout_main)
        