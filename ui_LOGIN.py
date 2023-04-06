# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LOGIN.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        if not loginWindow.objectName():
            loginWindow.setObjectName(u"loginWindow")
        loginWindow.setWindowModality(Qt.NonModal)
        loginWindow.resize(480, 450)
        loginWindow.setMaximumSize(QSize(480, 450))
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(12)
        loginWindow.setFont(font)
        loginWindow.setStyleSheet(u"background-color: white;\n"
"")
        self.mainWidget = QWidget(loginWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setStyleSheet(u"QWidget#mainWidget {\n"
"	background-color: #001D3D;\n"
"	color: white;\n"
"}\n"
"QFrame#formFrame {\n"
"	border-radius: 8px;\n"
"}\n"
"QFrame#headerFrame {\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: black;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 2px solid black;\n"
"	border-radius: 6px;\n"
"	padding: 0px 8px 0px 8px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerFrame = QFrame(self.mainWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMaximumSize(QSize(16777215, 151))
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo = QLabel(self.headerFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(128, 128))
        self.logo.setPixmap(QPixmap(u"ustp logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setWordWrap(True)

        self.horizontalLayout.addWidget(self.logo)

        self.header = QLabel(self.headerFrame)
        self.header.setObjectName(u"header")
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(48)
        font1.setBold(True)
        self.header.setFont(font1)
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setWordWrap(True)

        self.horizontalLayout.addWidget(self.header)


        self.verticalLayout.addWidget(self.headerFrame)

        self.formFrame = QFrame(self.mainWidget)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setFrameShape(QFrame.NoFrame)
        self.formFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.formFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.passFrame = QFrame(self.formFrame)
        self.passFrame.setObjectName(u"passFrame")
        self.passFrame.setFrameShape(QFrame.NoFrame)
        self.passFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.passFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.passLbl = QLabel(self.passFrame)
        self.passLbl.setObjectName(u"passLbl")
        font2 = QFont()
        font2.setFamilies([u"Montserrat Medium"])
        font2.setPointSize(16)
        self.passLbl.setFont(font2)

        self.verticalLayout_3.addWidget(self.passLbl)

        self.passInput = QLineEdit(self.passFrame)
        self.passInput.setObjectName(u"passInput")
        self.passInput.setFont(font)
        self.passInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.passInput)


        self.gridLayout.addWidget(self.passFrame, 2, 0, 1, 1)

        self.userFrame = QFrame(self.formFrame)
        self.userFrame.setObjectName(u"userFrame")
        self.userFrame.setFrameShape(QFrame.NoFrame)
        self.userFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.userFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.userLbl = QLabel(self.userFrame)
        self.userLbl.setObjectName(u"userLbl")
        self.userLbl.setFont(font2)

        self.verticalLayout_2.addWidget(self.userLbl)

        self.userInput = QLineEdit(self.userFrame)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setFont(font)
        self.userInput.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.userInput)


        self.gridLayout.addWidget(self.userFrame, 1, 0, 1, 1)

        self.loginFrame = QFrame(self.formFrame)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setFrameShape(QFrame.NoFrame)
        self.loginFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.loginFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loginBtn = QPushButton(self.loginFrame)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(60, 60))
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.loginBtn.setFont(font3)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.loginBtn)


        self.gridLayout.addWidget(self.loginFrame, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.formFrame)

        loginWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(loginWindow)

        QMetaObject.connectSlotsByName(loginWindow)
    # setupUi

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(QCoreApplication.translate("loginWindow", u"PRISMS Login", None))
        self.logo.setText("")
        self.header.setText(QCoreApplication.translate("loginWindow", u"PRISMS", None))
        self.passLbl.setText(QCoreApplication.translate("loginWindow", u"Password", None))
        self.passInput.setPlaceholderText("")
        self.userLbl.setText(QCoreApplication.translate("loginWindow", u"Username", None))
        self.userInput.setPlaceholderText(QCoreApplication.translate("loginWindow", u"(ID Number Only)", None))
        self.loginBtn.setText(QCoreApplication.translate("loginWindow", u"Log-in", None))
    # retranslateUi

