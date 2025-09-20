import sys 

from PyQt6.QtWidgets import QApplication

from src import manage_window
from src.manage_window import ManageWindow
# from services.insert_users import create_user

def starter():
    # create_user('morteza',"aa123aa")
    # create_user('admin', "Admin321A")

    app = QApplication(sys.argv)
    # ref count if you do not a variable like window to the ref count is 0
    # so python after ending the program cleans those with ref_count=0
    # it causes the window comes up and then be broken out of the blue
    window = ManageWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    starter()

