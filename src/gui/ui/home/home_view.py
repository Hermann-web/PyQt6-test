# Form implementation generated from reading ui file '/home/colin/Python/Projects/Pycharm/Other/Learning/LearningQt/src/gui/ui/home/home_view.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(903, 678)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 901, 661))
        self.listView.setObjectName("listView")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 881, 181))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.homeIntroLongTextTab_1 = QtWidgets.QLabel(self.tab_1)
        self.homeIntroLongTextTab_1.setGeometry(QtCore.QRect(10, 60, 451, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.homeIntroLongTextTab_1.setFont(font)
        self.homeIntroLongTextTab_1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.homeIntroLongTextTab_1.setAutoFillBackground(False)
        self.homeIntroLongTextTab_1.setStyleSheet("")
        self.homeIntroLongTextTab_1.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.homeIntroLongTextTab_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.homeIntroLongTextTab_1.setObjectName("homeIntroLongTextTab_1")
        self.homeIntroTitleFrameTab_1 = QtWidgets.QFrame(self.tab_1)
        self.homeIntroTitleFrameTab_1.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.homeIntroTitleFrameTab_1.setStyleSheet("width: 100%;")
        self.homeIntroTitleFrameTab_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.homeIntroTitleFrameTab_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.homeIntroTitleFrameTab_1.setObjectName("homeIntroTitleFrameTab_1")
        self.homeIntroLabelTabTitle_1 = QtWidgets.QLabel(self.homeIntroTitleFrameTab_1)
        self.homeIntroLabelTabTitle_1.setGeometry(QtCore.QRect(0, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.homeIntroLabelTabTitle_1.setFont(font)
        self.homeIntroLabelTabTitle_1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.homeIntroLabelTabTitle_1.setObjectName("homeIntroLabelTabTitle_1")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.homeIntroTitleFrameTab_2 = QtWidgets.QFrame(self.tab_2)
        self.homeIntroTitleFrameTab_2.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.homeIntroTitleFrameTab_2.setStyleSheet("width: 100%;")
        self.homeIntroTitleFrameTab_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.homeIntroTitleFrameTab_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.homeIntroTitleFrameTab_2.setObjectName("homeIntroTitleFrameTab_2")
        self.homeIntroLabelTabTitle_2 = QtWidgets.QLabel(self.homeIntroTitleFrameTab_2)
        self.homeIntroLabelTabTitle_2.setGeometry(QtCore.QRect(0, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.homeIntroLabelTabTitle_2.setFont(font)
        self.homeIntroLabelTabTitle_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.homeIntroLabelTabTitle_2.setObjectName("homeIntroLabelTabTitle_2")
        self.homeIntroLongTextTab_2 = QtWidgets.QLabel(self.tab_2)
        self.homeIntroLongTextTab_2.setGeometry(QtCore.QRect(10, 60, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.homeIntroLongTextTab_2.setFont(font)
        self.homeIntroLongTextTab_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.homeIntroLongTextTab_2.setAutoFillBackground(False)
        self.homeIntroLongTextTab_2.setStyleSheet("")
        self.homeIntroLongTextTab_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.homeIntroLongTextTab_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.homeIntroLongTextTab_2.setObjectName("homeIntroLongTextTab_2")
        self.tabWidget.addTab(self.tab_2, "")
        HomeWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(HomeWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menuBar.setObjectName("menuBar")
        HomeWindow.setMenuBar(self.menuBar)
        self.actionLogin = QtGui.QAction(HomeWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionRegister = QtGui.QAction(HomeWindow)
        self.actionRegister.setObjectName("actionRegister")

        self.retranslateUi(HomeWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "MainWindow"))
        self.homeIntroLongTextTab_1.setText(_translate("HomeWindow", "TextLabel"))
        self.homeIntroLabelTabTitle_1.setText(_translate("HomeWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("HomeWindow", "Tab 1"))
        self.homeIntroLabelTabTitle_2.setText(_translate("HomeWindow", "TextLabel"))
        self.homeIntroLongTextTab_2.setText(_translate("HomeWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("HomeWindow", "Tab 2"))
        self.actionLogin.setText(_translate("HomeWindow", "Login"))
        self.actionRegister.setText(_translate("HomeWindow", "Register"))
