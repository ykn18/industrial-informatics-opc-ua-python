from PyQt5.QtWidgets import QMainWindow
from log_window import Ui_MainWindow


class LogWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
