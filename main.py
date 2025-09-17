import sys 

from PyQt6.QtWidgets import QApplication

from main_window.login import LoginWindow

def starter():
    app = QApplication(sys.argv)
    # ref count if you do not a variable like window to the ref count is 0
    # so python after ending the program cleans those with ref_count=0
    # it causes the window comes up and then be broken out of the blue
    window = LoginWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    starter()