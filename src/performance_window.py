from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QHeaderView, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from services.users_employees_operations import employees_performance_report


class FilterWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("جست و جو")
        self.initialize_ui()
        self.setModal(True)
        self.show()

    def initialize_ui(self):
        self.setGeometry(230, 150, 1100, 500)

        self._font = QFont("B Titr", 12)

        # جدول
        self.table = QTableWidget(0, 7)
        self.table.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.table.setHorizontalHeaderLabels(
            [
                'نام',
                'نام خانوادگی',
                'سال',
                'ماه',
                'ساعات اضافه کار',
                'ساعات ماموریت',
                'مدت روز های مرخصی',
            ]
        )

        # استایل
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
        """)

        # کشیدن جدول به کل فضا
        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # پر کردن جدول
        self.fill_table()

        # لایه اصلی
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

    def fill_table(self):
        self.table.setRowCount(0)
        emps_perfs = employees_performance_report()
        for i, emp in enumerate(emps_perfs):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(emp[1]))
            self.table.setItem(i, 1, QTableWidgetItem(emp[2]))
            self.table.setItem(i, 2, QTableWidgetItem(str(emp[3])))
            self.table.setItem(i, 3, QTableWidgetItem(str(emp[4])))
            self.table.setItem(i, 4, QTableWidgetItem(str(emp[5])))
            self.table.setItem(i, 5, QTableWidgetItem(str(emp[6])))
            self.table.setItem(i, 6, QTableWidgetItem(str(emp[7])))
