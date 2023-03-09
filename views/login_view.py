"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""
from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow


class LoginView(QMainWindow):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # load the layout
        from src.gui.ui.login.login_view import Ui_LoginWindow
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # import CSS file
        css_file = "src/gui/css/login.css"
        with open(css_file, "r") as fh:
            self.setStyleSheet(fh.read())

        self.content()

    def content(self):
        window_title = 'Login'

        self.setWindowTitle(f"{window_title}: My first PyQt6 program!")

        # Navigation

        button_home = QAction("Home", self)
        button_register = QAction("Register", self)
        button_login = QAction("Login", self)

        button_home.triggered.connect(self.switch_first_window)
        button_register.triggered.connect(self.switch_second_window)
        button_login.triggered.connect(self.switch_third_window)

        menubar = self.ui.menuBar
        menubar.addAction(button_home)
        menubar.addAction(button_register)
        menubar.addAction(button_login)

        self.ui.LoginViewTitleLabel.setText("Login")
        self.ui.LoginViewTitleLabel.adjustSize()

        self.ui.LoginViewDescriptionLabel.setText("Sign in to your account")
        self.ui.LoginViewDescriptionLabel.adjustSize()

        self.ui.LoginFormUsernameLabel.setText("Username or email address")
        self.ui.LoginFormUsernameLabel.adjustSize()

        self.ui.LoginFormPasswordLabel.setText("Password")
        self.ui.LoginFormPasswordLabel.adjustSize()

        self.ui.LoginFormSubmitBtn.setText("Sign in")

    def submit(self):
        pass

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
