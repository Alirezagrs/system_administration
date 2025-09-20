from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, \
    QPushButton, QHBoxLayout, QFrame, QCheckBox, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from utils.persian_datetime import persian_date


class ManageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
        
    def initialize_ui(self):
        self.setWindowTitle("سیستم ورود و خروج")
        # self.setFixedSize(1280, 735)
        self.showFullScreen()
        self.setStyleSheet("background-color: #fff;")

        # font
        self._font = QFont("B Titr", 12)

        # hsidebar_frame
        self.hsidebar = QFrame()
        self.hsidebar.setStyleSheet("background-color: #f7f5f5;")
        self.hsidebar.setFixedHeight(50)

        #hsidebar_label
        self.hsidebar_label = QLabel(f"{persian_date()}")
        self.hsidebar_label.setFont(self._font)
        
        #hsidebar_layout
        hlayout = QHBoxLayout()
        hlayout.addStretch()
        hlayout.addWidget(self.hsidebar_label)
        self.hsidebar.setLayout(hlayout)

        # vsidebar_frame
        self.vsidebar = QFrame()
        self.vsidebar.setStyleSheet("background-color: #474141;")
        self.vsidebar.setFixedWidth(200)

        #vsidebar_btn
        enter_e_btn = self.make_vsidebar_btns("ورود و خروج کارکنان", "💼")
        enter_g_btn = self.make_vsidebar_btns("ورود و خروج اشخاص", "🕘")
        info_btn = self.make_vsidebar_btns("گزارشات", "📊")
        settings_btn = self.make_vsidebar_btns("تنظیمات", "⚙️")
        exit_btn = self.make_vsidebar_btns("خروج", "")

        #btn actions
        exit_btn.clicked.connect(self.close_program)

        #vsidebar_layout
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(enter_e_btn)
        sidebar_layout.addWidget(enter_g_btn)
        sidebar_layout.addWidget(info_btn)
        sidebar_layout.addWidget(settings_btn)
        sidebar_layout.addStretch()
        sidebar_layout.addWidget(exit_btn)
        self.vsidebar.setLayout(sidebar_layout)

        # middle_frame_right
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #f5f5f5;")

        body_layout = QHBoxLayout()
        body_layout.addWidget(self.vsidebar)   # سایدبار سمت چپ
        body_layout.addWidget(self.content)    # محتوای اصلی

        # --- لایه نهایی (header + body)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.hsidebar)
        main_layout.addLayout(body_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container) # special when using layout

    #vsidebar_btns
    def make_vsidebar_btns(self, text, icon):
        self.btn = QPushButton(f"{icon} {text}")
        self.btn.setFont(self._font)
        self.btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn.setStyleSheet("""
            QPushButton{ 
                    text-align: center;
                    min-height: 24px;
                    border: none;
                    color: white;
                    font-size: 12pt;
                    font-weight: bold;
                    background: transparent;
            }
            QPushButton:checked{
                    background: #4358f0; 
            }
            QPushButton:hover{ 
                    background: rgba(255,255,255,0.1); 
            }
        """)
        return self.btn
        
    def close_program(self):
        self.close()

        