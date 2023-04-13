"""

Created by Colin Gelling on 01/1/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction

from core.Handlers.SessionHandlers.UserSessionHandler import UserSessionHandling


class UserView(QMainWindow, UserSessionHandling):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # load the layout
        from src.gui.ui.user.welcome_view import Ui_WelcomeUserWindow
        self.ui = Ui_WelcomeUserWindow()
        self.ui.setupUi(self)

        # import CSS file
        css_file = "src/gui/css/home.css"
        with open(css_file, "r") as fh:
            self.setStyleSheet(fh.read())

        self.content()

    def content(self):

        ui = self.ui

        window_title = 'Welcomed user'

        self.setWindowTitle(f"{window_title}: My first PyQt6 program!")

        # Navigation

        settings = self.settings
        settings.beginGroup("logged_user")

        menubar = ui.menuBar
        menu = menubar.addMenu(f'{ settings.value("user") }')

        edit = menu.addMenu("Settings")
        edit.addAction("copy")
        edit.addAction("paste")

        menu.addAction("Logout")
        menu.triggered[QAction].connect(self.processtrigger)

        settings.endGroup()

        # Navigation end

        ui.welcomeUser.setText("Welcome, user_name!")

        ui.userIntroductionLabel.setText("You're successfully logged in now, this area is all about showing you "
                                              "data coming from the database behind this program.")

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()

    def processtrigger(self):
        from PyQt6.QtCore import QSettings
        settings = QSettings("PyQt-test", "LoggedUser")
        settings.beginGroup("user_session")
        settings.remove("user_session")
        settings.endGroup()

        # if settings.allKeys():
        #     print("Session not empty")

        print(settings.allKeys())
