from PyQt6.QtWidgets import QDialog, QPushButton, QHBoxLayout,\
    QFrame, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class UserCrud(QDialog):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.setModal(True)
        self.show()

    def initialize_ui(self):
        self.setGeometry(100,100,200,200)

        #font
        self._font = QFont("B Titr", 12)

        #fram
        self.frame = QFrame()
        self.frame.setStyleSheet("background-color: #f7f5f5;")
        self.frame.setFixedSize(200,200)

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
            background: #09e818;
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
            background: #a39e9d;
            color: white;
            font-size: 12px;
        }
    """)

        #inputs
        self.create_input = QLineEdit()
        self.delete_input = QLineEdit()
        self.edit_input = QLineEdit()

        #layout