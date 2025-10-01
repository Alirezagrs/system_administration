from PyQt6.QtWidgets import (QMainWindow,
                             QLabel,
                             QTableWidget,
                             QPushButton,
                             QHBoxLayout,
                             QFrame,
                             QVBoxLayout,
                             QWidget,
                             QDateEdit,
                             QTableWidgetItem,
                             QHeaderView
                             )
from PyQt6.QtCore import Qt, QDate, QLocale, QCalendar
from PyQt6.QtGui import QFont
from persiantools.jdatetime import JalaliDateTime, JalaliDate

from utils.persian_datetime import (persian_date,
                                    convert_calender_to_persian as cp
                                    )
from utils.mention_of_day import find_mention_of_the_day
from utils.persian_datetime import convert_slash_to_dash, normalize_time
from src.crud_employee_window import UserCrud
from services.users_employees_operations import (get_employees_by_date,
                                                 get_employees,
                                                 admit_table_changes,
                                                 admit_table_updates
                                                )
from services.guys_operations import (get_guys_by_date,
                                      admit_table_guys_updates,
                                      admit_table_guys_changes
                                    )


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

        # date frame for employees
        self.date_frame = QFrame()
        self.date_frame.setStyleSheet("background-color: #f5f5f5;")
        self.date_frame.setFixedHeight(30)

        # date frame for guys
        self.date_frame_guys = QFrame()
        self.date_frame_guys.setStyleSheet("background-color: #f5f5f5;")
        self.date_frame_guys.setFixedHeight(30)

        # table_employee frame
        self.table_frame = QFrame()
        self.table_frame.setStyleSheet("background-color: #f5f5f5;")

        # table_guys frame
        self.guys_table_frame = QFrame()
        self.guys_table_frame.setStyleSheet("background-color: #f5f5f5;")

        # main-frame
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #f5f5f5;")

        # __________________widgets___________________
        # create user btn
        self.create_user_btn = QPushButton()
        self.create_user_btn.clicked.connect(self.create_user_handler)
        self.create_user_btn.setFont(self._font)
        self.create_user_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.create_user_btn.setFixedHeight(25)
        self.create_user_btn.setText("ایجاد کارمند➕")
        self.create_user_btn.setStyleSheet("""
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

        # admitting employees with date ind db button
        self.admit_btn = QPushButton()
        self.admit_btn.clicked.connect(self.admit_employees)
        self.admit_btn.setFont(self._font)
        self.admit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.admit_btn.setFixedHeight(25)
        self.admit_btn.setText("ثبت کارمند")
        self.admit_btn.setStyleSheet("""
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
        
    # admitting guys with date ind db button
        self.admit_guys_btn = QPushButton()
        self.admit_guys_btn.clicked.connect(self.admit_guys_handler)
        self.admit_guys_btn.setFont(self._font)
        self.admit_guys_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.admit_guys_btn.setFixedHeight(25)
        self.admit_guys_btn.setText("ثبت شخص")
        self.admit_guys_btn.setStyleSheet("""
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

        # search date employee in db btn
        self.search_btn = QPushButton()
        self.search_btn.clicked.connect(self.search_btn_handler)
        self.search_btn.setFont(self._font)
        self.search_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.search_btn.setFixedHeight(25)
        self.search_btn.setText("جست و جو")
        self.search_btn.setStyleSheet("""
        QPushButton{
            background: #07b813;
            color: white;
            font-size: 12px;
            padding-bottom: 5px 
        }
        QPushButton:hover{
            background: #09e818;
            color: white;
            font-size: 12px;
            padding-bottom: 5px 
        }
    """)
        
        # search date guys in db btn
        self.search_btn_guys = QPushButton()
        self.search_btn_guys.clicked.connect(self.search_btn_guys_handler)
        self.search_btn_guys.setFont(self._font)
        self.search_btn_guys.setCursor(Qt.CursorShape.PointingHandCursor)
        self.search_btn_guys.setFixedHeight(25)
        self.search_btn_guys.setText("جست و جو")
        self.search_btn_guys.setStyleSheet("""
        QPushButton{
            background: #07b813;
            color: white;
            font-size: 12px;
            padding-bottom: 5px 
        }
        QPushButton:hover{
            background: #09e818;
            color: white;
            font-size: 12px;
            padding-bottom: 5px 
        }
    """)
        # date employee
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
        
        #date guys
        self.date_edit_guys = QDateEdit()
        self.date_edit_guys.setFixedHeight(20)
        self.date_edit_guys.setDate(
            QDate(
                cp().year,
                cp().month,
                cp().day,
                QCalendar(QCalendar.System.Jalali)
            )
        )
        self.date_edit_guys.setCalendar(QCalendar(QCalendar.System.Jalali))
        self.date_edit_guys.setLocale(
            QLocale(QLocale.Language.Persian, QLocale.Country.Iran))
        self.date_edit_guys.setCalendarPopup(True)
        self.date_edit_guys.setDisplayFormat("yyyy/MM/dd")
        self.date_edit_guys.setStyleSheet("""
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

        # dynamic_table_of_employees
        self.table = QTableWidget(0, 11)
        self.search_btn_handler()  # getting values dynamicly
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
        # dynamic_table_of_guys
        self.table_of_guys = QTableWidget(0,10)
        # self.table_of_guys.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)

        self.search_btn_guys_handler()
        self.table_of_guys.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.table_of_guys.setHorizontalHeaderLabels(
            [
                'نام',
                'نام خانوادگی',
                'تاریخ',
                'زمان ورود',
                'زمان خروج',
                'مراجعه به',
                'جنسیت',
                'آیا نظامی است؟',
                'درجه',
                'بخش/سازمان',
            ]
        )
        self.table_of_guys.setStyleSheet("""
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
        self.enter_e_btn.clicked.connect(self.enter_e_btn_handler)
        

        self.enter_g_btn = self.make_vsidebar_btns("ورود و خروج اشخاص", "🕘")
        self.enter_g_btn.clicked.connect(self.enter_g_btn_handler)


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

        self.date_frame.hide()
        self.table_frame.hide()
        self.guys_table_frame.hide()
        self.date_frame_guys.hide()

        # hsidebar layout for employee
        self.container_hlayout_date = QHBoxLayout()

        self.container_hlayout_date.addWidget(self.create_user_btn)
        self.container_hlayout_date.addWidget(self.admit_btn)
        self.container_hlayout_date.addStretch()
        self.container_hlayout_date.addWidget(self.search_btn)
        self.container_hlayout_date.addWidget(
            self.date_edit, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        self.date_frame.setLayout(self.container_hlayout_date)

        # hsidebar layout for guys
        self.container_hlayout_date_guys = QHBoxLayout()
        self.container_hlayout_date_guys.addWidget(self.admit_guys_btn)
        self.container_hlayout_date_guys.addStretch()
        self.container_hlayout_date_guys.addWidget(self.search_btn_guys)
        self.container_hlayout_date_guys.addWidget(
            self.date_edit_guys, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        self.date_frame_guys.setLayout(self.container_hlayout_date_guys)

        # table_of_employees layout
        self.container_hlayout_table = QHBoxLayout()
        self.container_hlayout_table.addWidget(self.table)
        self.table_frame.setLayout(self.container_hlayout_table)

        # table_of_guys layout
        self.container_hlayout_guys_table = QHBoxLayout()
        self.container_hlayout_guys_table.addWidget(self.table_of_guys)
        self.guys_table_frame.setLayout(self.container_hlayout_guys_table)

        # layout of date and table
        self.content_layout = QVBoxLayout()
        self.content_layout.addWidget(self.date_frame)
        self.content_layout.addWidget(self.date_frame_guys)
        self.content_layout.addWidget(self.table_frame, stretch=1)
        self.content_layout.addWidget(self.guys_table_frame, stretch=1)
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

        self.btn.setCheckable(True)
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
            QPushButton:checked {
                    background-color: rgba(255,255,255,0.1);
                    color: white;
            }
            QPushButton:hover{ 
                    background: rgba(255,255,255,0.1); 
            }
        """)
        return self.btn

    def create_user_handler(self):
        # bcause of ref count and memory management and being window alive
        # used self
        self.user_crud_window = UserCrud()

    def close_program(self):
        from src.login_window import LoginWindow  # for circular import
        self.login_window = LoginWindow()
        self.close()

    def search_btn_handler(self):
        # just need it once no need to use self(ref count)
        # in spite of being persian calender in window i got problem of
        # getting the value. it was gregorian(میلادی)
        selected_date = self.date_edit.date().toPyDate()  # convert string to date obj
        

        _filter = get_employees_by_date(
            selected_date.year,
            selected_date.month,
            selected_date.day
        )
        
        if _filter:
            self.table.setRowCount(0)
            for i, (empinfo, emp) in enumerate(_filter):
                self.table.insertRow(i)
                self.table.setItem(i, 0, QTableWidgetItem(emp.first_name))
                self.table.setItem(i, 1, QTableWidgetItem(emp.last_name))
                self.table.setItem(i, 2, QTableWidgetItem(emp.badge))
                self.table.setItem(i, 3, QTableWidgetItem(convert_slash_to_dash(self.date_edit.text())))
                self.table.setItem(i, 4, QTableWidgetItem(str(normalize_time(empinfo.entrance_time))))
                self.table.setItem(i, 5, QTableWidgetItem(str(normalize_time(empinfo.exit_time))))
                self.table.setItem(i, 6, QTableWidgetItem(str(empinfo.is_released)))
                self.table.setItem(i, 7, QTableWidgetItem(empinfo.reseaon_of_releasing))
                self.table.setItem(i, 8, QTableWidgetItem(empinfo.mission_kind))
                self.table.setItem(i, 9, QTableWidgetItem(str(empinfo.mission_time if empinfo.mission_time else "")))
                self.table.setItem(i, 10, QTableWidgetItem(str(empinfo.overtime_work))) # can not show in float

        else:
            _filter = get_employees()
            print(_filter)
            self.table.setRowCount(0)
            for i, emp in enumerate(_filter):
                self.table.insertRow(i)
                self.table.setItem(i, 0, QTableWidgetItem(emp[0]))
                self.table.setItem(i, 1, QTableWidgetItem(emp[1]))
                self.table.setItem(i, 2, QTableWidgetItem(emp[2]))
                self.table.setItem(i, 3, QTableWidgetItem(convert_slash_to_dash(self.date_edit.text())))
                self.table.setItem(i, 4, QTableWidgetItem(""))
                self.table.setItem(i, 5, QTableWidgetItem(""))
                self.table.setItem(i, 6, QTableWidgetItem(""))
                self.table.setItem(i, 7, QTableWidgetItem(""))
                self.table.setItem(i, 8, QTableWidgetItem(""))
                self.table.setItem(i, 9, QTableWidgetItem(""))
                self.table.setItem(i, 10, QTableWidgetItem("")) # can not show in float

    def admit_employees(self):
        selected_date = self.date_edit.date().toPyDate()
        data = {}
        for row in range(self.table.rowCount()):
            col_data = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                col_data.append(item.text() if item else "")
            data[row] = col_data
        # try:
        _filter = get_employees_by_date(
                selected_date.year,
                selected_date.month,
                selected_date.day
            )
        if _filter:    
            for _, data_ in data.items():
                print(data_[0])
                admit_table_updates(
                name=data_[0],
                lname=data_[1],
                badge=data_[2],
                date=JalaliDate.fromisoformat(data_[3]).to_gregorian(),
                entrance_time=JalaliDateTime.strptime(data_[4],"%H:%M").time(),
                exit_time=JalaliDateTime.strptime(data_[5],"%H:%M").time(),
                is_released=("" if data_[6]=="" else data_[6]),
                reseaon_of_releasing=data_[7],
                mission_kind=data_[8],
                mission_time=(None if data_[9]=="" else JalaliDateTime.strptime(data_[9],"%H:%M").time()),
                overtime_work=float(data_[10])
                )

        # I must cast types to be save in db
        # all the values of table are str
        else:
            for _, data_ in data.items():
                admit_table_changes(
                    name=data_[0],
                    lname=data_[1],
                    badge=data_[2],
                    date=JalaliDate.fromisoformat(data_[3]).to_gregorian(),
                    entrance_time=JalaliDateTime.strptime(data_[4],"%H:%M").time(),
                    exit_time=JalaliDateTime.strptime(data_[5],"%H:%M").time(),
                    is_released=("" if data_[6]=="" else data_[6]),
                    reseaon_of_releasing=data_[7],
                    mission_kind=data_[8],
                    mission_time=(None if data_[9]=="" else JalaliDateTime.strptime(data_[9],"%H:%M").time()),
                    overtime_work=float(data_[10])
                )
    def search_btn_guys_handler(self):
        selected_date = self.date_edit_guys.date().toPyDate()

        _filter = get_guys_by_date(
            selected_date.year,
            selected_date.month,
            selected_date.day
        )
        if _filter:
            self.table_of_guys.setRowCount(0)
            for i, guy in enumerate(_filter):
                self.table_of_guys.insertRow(i)
                self.table_of_guys.setItem(i, 0, QTableWidgetItem(guy.first_name))
                self.table_of_guys.setItem(i, 1, QTableWidgetItem(guy.last_name))
                self.table_of_guys.setItem(i, 2, QTableWidgetItem(convert_slash_to_dash(self.date_edit_guys.text())))
                self.table_of_guys.setItem(i, 3, QTableWidgetItem(str(normalize_time(guy.entrance_time))))
                self.table_of_guys.setItem(i, 4, QTableWidgetItem(str(normalize_time(guy.exit_time))))
                self.table_of_guys.setItem(i, 5, QTableWidgetItem(guy.work_with))
                self.table_of_guys.setItem(i, 6, QTableWidgetItem(guy.gender))
                self.table_of_guys.setItem(i, 7, QTableWidgetItem(guy.is_military))
                self.table_of_guys.setItem(i, 8, QTableWidgetItem(guy.badge))
                self.table_of_guys.setItem(i, 9, QTableWidgetItem(guy.organization))

        else:
            _filter = range(30) # default rows to be filled out
            print(_filter)
            self.table_of_guys.setRowCount(0)
            for i, guy in enumerate(_filter):
                self.table_of_guys.insertRow(i)
                self.table_of_guys.setItem(i, 0, QTableWidgetItem(""))
                self.table_of_guys.setItem(i, 1, QTableWidgetItem(""))
                self.table_of_guys.setItem(i, 2, QTableWidgetItem(convert_slash_to_dash(self.date_edit_guys.text())))
                self.table_of_guys.setItem(i, 3, QTableWidgetItem(""))
                self.table_of_guys.setItem(i, 4, QTableWidgetItem(""))
                self.table_of_guys.setItem(i, 5, QTableWidgetItem(""))
                self.table_of_guys.setItem(i, 6, QTableWidgetItem(""))
                self.table_of_guys.setItem(i, 7, QTableWidgetItem(""))
                self.table_of_guys.setItem(i, 8, QTableWidgetItem(""))
                self.table_of_guys.setItem(i, 9, QTableWidgetItem(""))


    def admit_guys_handler(self):
        data = {}
        for row in range(self.table_of_guys.rowCount()):
            col_data = []
            for col in range(self.table_of_guys.columnCount()):
                item = self.table_of_guys.item(row, col)
                col_data.append(item.text() if item else "")
            data[row] = col_data
        
        selected_date = self.date_edit_guys.date().toPyDate()

        _filter = get_guys_by_date(
            selected_date.year,
            selected_date.month,
            selected_date.day
        )

        if _filter:
            for _, _data in data.items():
                if _data[0] and _data[1] and _data[3] and _data[4] and _data[6]:
                    admit_table_guys_updates(
                        first_name=_data[0],
                        last_name=_data[1],
                        date=JalaliDate.fromisoformat(_data[2]).to_gregorian(),
                        entrance_time=JalaliDateTime.strptime(_data[3],"%H:%M").time(),
                        exit_time=JalaliDateTime.strptime(_data[4],"%H:%M").time(),
                        work_with=_data[5],
                        gender=_data[6],
                        is_military=_data[7],
                        badge=_data[8],
                        organization=_data[9]
                    )
                else:
                    continue
        else:
            for _, _data in data.items():
                if _data[0] and _data[1] and _data[3] and _data[4] and _data[6]:
                    admit_table_guys_changes(
                        first_name=_data[0],
                        last_name=_data[1],
                        date=JalaliDate.fromisoformat(_data[2]).to_gregorian(),
                        entrance_time=JalaliDateTime.strptime(_data[3],"%H:%M").time(),
                        exit_time=JalaliDateTime.strptime(_data[4],"%H:%M").time(),
                        work_with=_data[5],
                        gender=_data[6],
                        is_military=_data[7],
                        badge=_data[8],
                        organization=_data[9]
                    )
                else:
                    continue


    def enter_e_btn_handler(self):
        """ if I wanted to use:
        self.container_hlayout_date.addWidget(self.create_user_btn)
        self.container_hlayout_date.addWidget(self.admit_btn)
        self.container_hlayout_date.addStretch()
        self.container_hlayout_date.addWidget(self.search_btn)
        self.container_hlayout_date.addWidget(
            self.date_edit, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        self.date_frame.setLayout(self.container_hlayout_date)

        self.container_hlayout_table = QHBoxLayout()
        self.container_hlayout_table.addWidget(self.table)
        self.table_frame.setLayout(self.container_hlayout_table)
        ====>>>>
        after each clicking btn new widgets were added to the layout and their 
        position got wrong!!!!!
        """

        if self.enter_e_btn.isChecked():

            self.enter_g_btn.setChecked(False)
            self.info_btn.setChecked(False)
            self.settings_btn.setChecked(False) 
            self.exit_btn.setChecked(False)

            self.date_frame_guys.hide()
            self.guys_table_frame.hide()
            self.date_frame.show()
            self.table_frame.show()
        else:
            self.date_frame.hide()
            self.table_frame.hide()
    

    def enter_g_btn_handler(self):
        if self.enter_g_btn.isChecked():

            self.enter_e_btn.setChecked(False)
            self.info_btn.setChecked(False)
            self.settings_btn.setChecked(False) 
            self.exit_btn.setChecked(False)

            self.table_frame.hide()
            self.date_frame.hide()
            self.date_frame_guys.show()
            self.guys_table_frame.show()

        else:
            self.date_frame_guys.hide()
            self.guys_table_frame.hide()