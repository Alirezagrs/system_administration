from poplib import LF
from PyQt6.QtWidgets import QMainWindow, QLabel, QTableWidget, \
    QPushButton, QHBoxLayout, QFrame, QVBoxLayout, QWidget, QDateEdit
from PyQt6.QtCore import Qt, QDate, QLocale, QCalendar
from PyQt6.QtGui import QFont

from utils.persian_datetime import persian_date, convert_calender_to_persian as cp
from utils.mention_of_day import find_mention_of_the_day


class ManageWindow(QMainWindow):
    def __init__(self, user_name):
        super().__init__()
        self.user_name = user_name
        self.initialize_ui()
        self.show()

    def initialize_ui(self):
        self.setWindowTitle("سیستم ورود و خروج")
        # self.setFixedSize(1280, 735)
        self.showFullScreen()
        self.setStyleSheet("background-color: #fff;")

        # font
        self._font = QFont("B Titr", 12)

        # __________________frames____________________
        # hsidebar_frame
        self.hsidebar = QFrame()
        self.hsidebar.setStyleSheet("background-color: #f7f5f5;")
        self.hsidebar.setFixedHeight(50)

        # vsidebar_frame
        self.vsidebar = QFrame()
        self.vsidebar.setStyleSheet("background-color: #474141;")
        self.vsidebar.setFixedWidth(200)

        # date frame
        self.date_frame = QFrame()
        self.date_frame.setStyleSheet("background-color: #f5f5f5;")
        self.date_frame.setFixedHeight(30)

        # table frame
        self.table_frame = QFrame()
        self.table_frame.setStyleSheet("background-color: #f5f5f5;")

        # main-frame
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #f5f5f5;")

        # __________________widgets___________________
        # search date in db btn
        self.search_btn = QPushButton()
        self.search_btn.setFont(self._font)
        self.search_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.search_btn.setFixedHeight(25)
        self.search_btn.setText("جست و جو")
        self.search_btn.setStyleSheet("""
        QPushButton{
            background: #07b813;
            color: white;
            font-size: 12px;
        }
        QPushButton:hover{
            background: #09e818;
            color: white;
            font-size: 12px;
        }
    """)
        # date
        self.date_edit = QDateEdit()
        self.date_edit.setFixedHeight(20)
        self.date_edit.setDate(
            QDate(
                cp().year,
                cp().month,
                cp().day,
                QCalendar(QCalendar.System.Jalali)
            )
        )
        self.date_edit.setCalendar(QCalendar(QCalendar.System.Jalali))
        self.date_edit.setLocale(
            QLocale(QLocale.Language.Persian, QLocale.Country.Iran))
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("yyyy/MM/dd")
        self.date_edit.setStyleSheet("""
            QDateEdit {
                background-color: white;
                border: 1px solid #ccc;
                padding: 2px 4px;
            }
            QCalendarWidget QWidget {
                alternate-background-color: #f5f5f5;
            }
            QCalendarWidget QToolButton{
                color: #fff;
                background-color: #090a0f;
                font-weight: bold;
                border: none;
                border-radius: 4px;
                padding: 2px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #454647;
            }
            QCalendarWidget QSpinBox{
                color: black;
                background: white;
                selection-background-color: #03040a;
            }
            QCalendarWidget QAbstractItemView:enabled{
                color: black;
                selection-background-color: #cce5ff;
                selection-color: black;
            }
            QCalendarWidget QMenu {
                background-color: #fff;
                color: black;   
                border: 1px solid #ccc;
            }
            QCalendarWidget QMenu::item:selected {
                background-color: #e0e0e0;   
                color: black;
            }
    """)

        # table
        self.table = QTableWidget(6, 11)
        self.table.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.table.setHorizontalHeaderLabels(
            [
                'نام',
                'نام خانوادگی',
                'درجه',
                'تاریخ',
                'زمان ورود',
                'زمان خروج',
                'مرخصی',
                'دلیل مرخصی',
                'نوع ماموریت',
                'زمان ماموریت',
                'اضافه کاری',
            ]
        )
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #faf5f5;
                alternate-background-color: #f9f9f9;
                gridline-color: #080707;       
                font-size: 14px;
                font-weight: bold;
                border: 2px solid #fff;
            }
            QHeaderView::section {
                background-color: #474141;       
                color: white;                   
                font-weight: bold;
                font-size: 13px;
                padding: 5px;
                border: none;
            }
            QTableWidget::item {
                padding: 4px;
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: #cce5ff;   
                color: #000;
                font-weight: bold;
            }
    """)

        # hsidebar_label
        self.hsidebar_label = QLabel(f"امروز {persian_date()}")
        self.hsidebar_label.setFont(self._font)

        self.hsidebar_mention = QLabel(
            f"ذکر امروز {find_mention_of_the_day()}"
        )
        self.hsidebar_mention.setFont(self._font)

        self.hsidebar_title = QLabel("سیستم ورود و خروج 👮")
        self.hsidebar_title.setFont(self._font)
        self.hsidebar_title.setStyleSheet("""
            color: #171212;
            font-weight: bold;
            font-size: 20px
        """)

        # vsidebar_btn
        self.enter_e_btn = self.make_vsidebar_btns("ورود و خروج کارکنان", "💼")
        self.enter_e_btn.setEnabled(True)
        self.enter_g_btn = self.make_vsidebar_btns("ورود و خروج اشخاص", "🕘")
        self.info_btn = self.make_vsidebar_btns("گزارشات", "📊")
        self.settings_btn = self.make_vsidebar_btns("تنظیمات", "⚙️")
        self.exit_btn = self.make_vsidebar_btns("خروج", "")

        # __________________layout____________________
        # hsidebar_layout
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.hsidebar_mention)
        hlayout.addStretch()
        hlayout.addWidget(self.hsidebar_title)
        hlayout.addStretch()
        hlayout.addWidget(self.hsidebar_label)
        self.hsidebar.setLayout(hlayout)

        # vsidebar_layout
        sidebar_layout = QVBoxLayout()
        if self.user_name == "admin":
            boss_btn = self.make_vsidebar_btns(
                f"{self.user_name} :مدیر سیستم", "👨‍💼")
            sidebar_layout.addWidget(boss_btn)

        elif self.user_name == "soldier":
            soldier_btn = self.make_vsidebar_btns(
                f"{self.user_name} :کاربر سیستم", "👨‍💼")
            sidebar_layout.addWidget(soldier_btn)

        sidebar_layout.addWidget(self.enter_e_btn)
        sidebar_layout.addWidget(self.enter_g_btn)
        sidebar_layout.addWidget(self.info_btn)
        sidebar_layout.addWidget(self.settings_btn)
        sidebar_layout.addStretch()
        sidebar_layout.addWidget(self.exit_btn)
        self.vsidebar.setLayout(sidebar_layout)

        # date layout
        self.container_hlayout_date = QHBoxLayout()
        self.container_hlayout_date.addStretch()
        self.container_hlayout_date.addWidget(self.search_btn)
        self.container_hlayout_date.addWidget(
            self.date_edit, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        self.date_frame.setLayout(self.container_hlayout_date)

        # table layout
        self.container_hlayout_table = QHBoxLayout()
        self.container_hlayout_table.addWidget(self.table)
        self.table_frame.setLayout(self.container_hlayout_table)

        # layout of date and table
        self.content_layout = QVBoxLayout()
        self.content_layout.addWidget(self.date_frame)
        self.content_layout.addWidget(self.table_frame, stretch=1)
        self.content_layout.addStretch()
        self.content.setLayout(self.content_layout)

        body_layout = QHBoxLayout()
        body_layout.addWidget(self.vsidebar)   # سایدبار سمت چپ
        body_layout.addWidget(self.content)  # محتوای اصلی

        # --- لایه نهایی (header + body)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.hsidebar)
        main_layout.addLayout(body_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)  # special when using layout

        # __________________actions__________________
        self.exit_btn.clicked.connect(self.close_program)

    # __________________utils__________________
    def make_vsidebar_btns(self, text, icon):
        self.btn = QPushButton(f"{icon} {text}")
        if "admin" in text or "soldier" in text:
            self.btn.setDisabled(True)
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
            QPushButton:selected{
                    background: #4358f0; 
            }
            QPushButton:hover{ 
                    background: rgba(255,255,255,0.1); 
            }
        """)
        return self.btn

    def close_program(self):
        from src.login_window import LoginWindow  # for circular import
        self.login_window = LoginWindow()
        self.close()
