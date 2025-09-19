from PyQt6.QtWidgets import QMainWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()

    def initialize_ui(self):
        self.setWindowTitle("سیستم ورود و خروج")
        self.setFixedSize(1280,735)
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #7693d6,
                    stop:1 #d8ebe6
                );
            }
        """)
        
