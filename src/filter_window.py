from PyQt6.QtWidgets import QDialog, QPushButton, QHBoxLayout, \
    QFrame, QVBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class FilterWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("جست و جو")
        self.initialize_ui()
        self.setModal(True)
        self.show()

    def initialize_ui(self):
        self.setGeometry(450, 175, 400, 200)

        # font
        self._font = QFont("B Titr", 12)

        # fram
        self.vframe = QFrame()
        self.vframe.setStyleSheet("background-color: #f7f5f5;")

        self.hframe = QFrame()
        self.hframe.setStyleSheet("background-color: #f7f5f5;")

        #notic_text
        self.notice_text = QLabel()
        self.setFont(self._font)
        self.notice_text.setText("""
توجه: با وارد کردن نام و نام خانوادگی نتایج دقیق تری را مشاهده میکنید و از بروز اشتباهات جلوگیری میکنید
""")
        self.notice_text.setWordWrap(True)
        self.notice_text.setStyleSheet("""
        QLabel{
            font-size: 15px;
            font-weight: bold;

        }
""")

        # btns
        self.filter_btn = QPushButton()
        self.filter_btn.setFont(self._font)
        self.filter_btn.setText("فیلتر کردن")
        self.filter_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.filter_btn.setStyleSheet("""
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

        # layout
        self.vlayout_input = QVBoxLayout()
        self.vlayout_input.addWidget(self.name_input)
        self.vlayout_input.addWidget(self.last_name_input)
        self.vlayout_input.addWidget(self.notice_text)
        self.vlayout_input.addStretch()
        self.vframe.setLayout(self.vlayout_input)

        self.hlayout_btn = QHBoxLayout()
        self.hlayout_btn.addWidget(self.filter_btn)
        self.hframe.setLayout(self.hlayout_btn)

        self.vlayout_main = QVBoxLayout()
        self.vlayout_main.addWidget(self.vframe)
        self.vlayout_main.addWidget(self.hframe)

        # different with QMainwindow we dont have setCentralWidget()
        self.setLayout(self.vlayout_main)

