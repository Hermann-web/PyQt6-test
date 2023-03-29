"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""
from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Models.User import User


class LoginView(QMainWindow, User):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    loggedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(LoginView, self).__init__()

        self.initialize_layout()
        self.load_css()
        self.show_content()

    def initialize_layout(self):
        # load the layout
        from src.gui.ui.login.login_view import Ui_LoginWindow
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

    def load_css(self):
        # import CSS file
        css_file = "src/gui/css/login.css"
        with open(css_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def show_content(self):
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

        # bind form field -data to key values for preparation purposes
        self.form_data['username'] = self.ui.LoginFormUsernameLineEdit
        # self.form_data['email'] = self.ui.RegisterFormEmailLineEdit  # TODO: later, make sure that it does work with the username
        self.form_data['password'] = self.ui.LoginFormPasswordLineEdit
        self.form_data['password'].setEchoMode(self.ui.LoginFormPasswordLineEdit.EchoMode.Password)

        self.ui.LoginFormUsernameLabel.setText("Username or email address")
        self.ui.LoginFormUsernameLabel.adjustSize()

        self.ui.LoginFormPasswordLabel.setText("Password")
        self.ui.LoginFormPasswordLabel.adjustSize()

        self.ui.LoginFormSubmitBtn.setText("Sign in")

        self.ui.LoginFormSubmitBtn.clicked.connect(self.check_credentials)

    def check_credentials(self):

        username_email = self.ui.LoginFormUsernameLineEdit.text()
        password = self.ui.LoginFormPasswordLineEdit.text()

        self.open_connection()
        conn = self.connection

        if conn:
            print(f"Logging in user..")

            collect_users = "SELECT email, username, password FROM users"
            cursor = conn.cursor()
            cursor.execute(collect_users)
            rows = cursor.fetchall()
            conn.commit()

            import bcrypt

            for row in rows:  # TODO: improve indexing rows
                if row[0] == username_email or row[1] == username_email and bcrypt.checkpw(
                        password.encode('utf-8'), row[2].encode('utf-8')):
                    self.trigger_login()
                    print('The username has been found in the database and the password matches with it!')
                    print('Login successful!')
                else:
                    print('Login failed, there is some more work left to do.')

    # TODO: try to make the following functionality working by executing it from a separated file

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()

    def trigger_login(self):
        self.loggedSignal.emit()
