# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'STS.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_studentMainWindow(object):
    def setupUi(self, studentMainWindow):
        if not studentMainWindow.objectName():
            studentMainWindow.setObjectName(u"studentMainWindow")
        studentMainWindow.resize(960, 720)
        studentMainWindow.setMinimumSize(QSize(960, 720))
        studentMainWindow.setMaximumSize(QSize(960, 720))
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setPointSize(12)
        studentMainWindow.setFont(font)
        studentMainWindow.setStyleSheet(u"")
        self.studentMainWidget = QWidget(studentMainWindow)
        self.studentMainWidget.setObjectName(u"studentMainWidget")
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(12)
        self.studentMainWidget.setFont(font1)
        self.studentMainWidget.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}\n"
"")
        self.burgerMenu = QFrame(self.studentMainWidget)
        self.burgerMenu.setObjectName(u"burgerMenu")
        self.burgerMenu.setGeometry(QRect(0, 0, 181, 721))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.burgerMenu.setFont(font2)
        self.burgerMenu.setStyleSheet(u"QFrame#burgerMenu {\n"
"	background-color: #001D3D;\n"
"	border-right: 4px solid #FFC300;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #001D3D;\n"
"	border-left: 4px solid #fcfcfc;\n"
"	color: white;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 4px solid #FFC300;\n"
"	border-radius: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.burgerMenu.setFrameShape(QFrame.NoFrame)
        self.burgerMenu.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.burgerMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.burgerTitle = QLabel(self.burgerMenu)
        self.burgerTitle.setObjectName(u"burgerTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.burgerTitle.sizePolicy().hasHeightForWidth())
        self.burgerTitle.setSizePolicy(sizePolicy)
        self.burgerTitle.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setPointSize(37)
        font3.setBold(True)
        self.burgerTitle.setFont(font3)
        self.burgerTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.burgerTitle.setWordWrap(True)

        self.verticalLayout.addWidget(self.burgerTitle)

        self.dashboardBtn = QPushButton(self.burgerMenu)
        self.dashboardBtn.setObjectName(u"dashboardBtn")
        font4 = QFont()
        font4.setFamilies([u"Montserrat Medium"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setKerning(True)
        self.dashboardBtn.setFont(font4)
        self.dashboardBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dashboardBtn.setIconSize(QSize(16, 16))
        self.dashboardBtn.setFlat(True)

        self.verticalLayout.addWidget(self.dashboardBtn)

        self.subjectsEnrolledBtn = QPushButton(self.burgerMenu)
        self.subjectsEnrolledBtn.setObjectName(u"subjectsEnrolledBtn")
        self.subjectsEnrolledBtn.setFont(font1)
        self.subjectsEnrolledBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.subjectsEnrolledBtn.setFlat(True)

        self.verticalLayout.addWidget(self.subjectsEnrolledBtn)

        self.qrCodeBtn = QPushButton(self.burgerMenu)
        self.qrCodeBtn.setObjectName(u"qrCodeBtn")
        self.qrCodeBtn.setFont(font1)
        self.qrCodeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.qrCodeBtn.setFlat(True)

        self.verticalLayout.addWidget(self.qrCodeBtn)

        self.enrollmentBtn = QPushButton(self.burgerMenu)
        self.enrollmentBtn.setObjectName(u"enrollmentBtn")
        self.enrollmentBtn.setFont(font1)
        self.enrollmentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.enrollmentBtn.setFlat(True)

        self.verticalLayout.addWidget(self.enrollmentBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.editProfileBtn = QPushButton(self.burgerMenu)
        self.editProfileBtn.setObjectName(u"editProfileBtn")
        font5 = QFont()
        font5.setFamilies([u"Montserrat Medium"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.editProfileBtn.setFont(font5)
        self.editProfileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editProfileBtn.setFlat(True)

        self.verticalLayout.addWidget(self.editProfileBtn)

        self.helpBtn = QPushButton(self.burgerMenu)
        self.helpBtn.setObjectName(u"helpBtn")
        font6 = QFont()
        font6.setFamilies([u"Montserrat Medium"])
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setStyleStrategy(QFont.PreferDefault)
        self.helpBtn.setFont(font6)
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.helpBtn.setCheckable(False)

        self.verticalLayout.addWidget(self.helpBtn)

        self.logoutBtn = QPushButton(self.burgerMenu)
        self.logoutBtn.setObjectName(u"logoutBtn")
        self.logoutBtn.setFont(font6)
        self.logoutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutBtn.setCheckable(False)

        self.verticalLayout.addWidget(self.logoutBtn)

        self.vLayoutFrame = QFrame(self.studentMainWidget)
        self.vLayoutFrame.setObjectName(u"vLayoutFrame")
        self.vLayoutFrame.setGeometry(QRect(180, 0, 772, 721))
        font7 = QFont()
        font7.setFamilies([u"Montserrat"])
        self.vLayoutFrame.setFont(font7)
        self.vLayoutFrame.setStyleSheet(u"QFrame#vLayoutFrame {\n"
"	background-color: #fcfcfc;\n"
"	color: white;\n"
"}\n"
"QFrame#statusBarInfo {\n"
"	border: 2px solid #FFC300;\n"
"	border-radius: 4px;\n"
"}\n"
"")
        self.vLayoutFrame.setFrameShape(QFrame.NoFrame)
        self.vLayoutFrame.setFrameShadow(QFrame.Plain)
        self.vLayout = QVBoxLayout(self.vLayoutFrame)
        self.vLayout.setObjectName(u"vLayout")
        self.pagesFrame = QFrame(self.vLayoutFrame)
        self.pagesFrame.setObjectName(u"pagesFrame")
        self.pagesFrame.setFrameShape(QFrame.NoFrame)
        self.pagesFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.pagesFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pagesWidgets = QStackedWidget(self.pagesFrame)
        self.pagesWidgets.setObjectName(u"pagesWidgets")
        self.pagesWidgets.setFont(font7)
        self.pagesWidgets.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.dashboard.setStyleSheet(u"QPushButton:hover {\n"
"	border-bottom: 2px solid black;\n"
"	border-radius: 16px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.dashboard)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dashFrame = QFrame(self.dashboard)
        self.dashFrame.setObjectName(u"dashFrame")
        self.dashFrame.setMaximumSize(QSize(16777215, 96))
        self.dashFrame.setFrameShape(QFrame.NoFrame)
        self.dashFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.dashFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.welcomeLbl = QLabel(self.dashFrame)
        self.welcomeLbl.setObjectName(u"welcomeLbl")
        font8 = QFont()
        font8.setFamilies([u"Montserrat"])
        font8.setPointSize(26)
        font8.setBold(True)
        self.welcomeLbl.setFont(font8)
        self.welcomeLbl.setStyleSheet(u"color: black;")
        self.welcomeLbl.setWordWrap(True)

        self.horizontalLayout.addWidget(self.welcomeLbl)


        self.verticalLayout_5.addWidget(self.dashFrame)

        self.dashFrame_2 = QFrame(self.dashboard)
        self.dashFrame_2.setObjectName(u"dashFrame_2")
        self.dashFrame_2.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.dashFrame_2.setFrameShape(QFrame.NoFrame)
        self.dashFrame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.dashFrame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dashBtnLayout = QVBoxLayout()
        self.dashBtnLayout.setObjectName(u"dashBtnLayout")
        self.assessmentBtn = QPushButton(self.dashFrame_2)
        self.assessmentBtn.setObjectName(u"assessmentBtn")
        self.assessmentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"icons/dashboard/list-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.assessmentBtn.setIcon(icon)
        self.assessmentBtn.setIconSize(QSize(80, 80))
        self.assessmentBtn.setFlat(True)

        self.dashBtnLayout.addWidget(self.assessmentBtn)

        self.assessmentLbl = QLabel(self.dashFrame_2)
        self.assessmentLbl.setObjectName(u"assessmentLbl")
        self.assessmentLbl.setMaximumSize(QSize(16777215, 64))
        font9 = QFont()
        font9.setFamilies([u"Montserrat"])
        font9.setPointSize(14)
        font9.setBold(True)
        self.assessmentLbl.setFont(font9)
        self.assessmentLbl.setAlignment(Qt.AlignCenter)

        self.dashBtnLayout.addWidget(self.assessmentLbl)

        self.dashBtnLayout_2 = QVBoxLayout()
        self.dashBtnLayout_2.setObjectName(u"dashBtnLayout_2")
        self.corBtn = QPushButton(self.dashFrame_2)
        self.corBtn.setObjectName(u"corBtn")
        self.corBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icons/dashboard/note-sticky-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.corBtn.setIcon(icon1)
        self.corBtn.setIconSize(QSize(80, 80))
        self.corBtn.setFlat(True)

        self.dashBtnLayout_2.addWidget(self.corBtn)

        self.corLbl = QLabel(self.dashFrame_2)
        self.corLbl.setObjectName(u"corLbl")
        self.corLbl.setMaximumSize(QSize(16777215, 64))
        self.corLbl.setFont(font9)
        self.corLbl.setAlignment(Qt.AlignCenter)

        self.dashBtnLayout_2.addWidget(self.corLbl)

        self.dashBtnLayout_3 = QVBoxLayout()
        self.dashBtnLayout_3.setObjectName(u"dashBtnLayout_3")
        self.docPromissoryBtn = QPushButton(self.dashFrame_2)
        self.docPromissoryBtn.setObjectName(u"docPromissoryBtn")
        self.docPromissoryBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"icons/dashboard/paperclip-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.docPromissoryBtn.setIcon(icon2)
        self.docPromissoryBtn.setIconSize(QSize(80, 80))
        self.docPromissoryBtn.setFlat(True)

        self.dashBtnLayout_3.addWidget(self.docPromissoryBtn)

        self.docPromissoryLbl = QLabel(self.dashFrame_2)
        self.docPromissoryLbl.setObjectName(u"docPromissoryLbl")
        self.docPromissoryLbl.setMaximumSize(QSize(16777215, 64))
        self.docPromissoryLbl.setFont(font9)
        self.docPromissoryLbl.setAlignment(Qt.AlignCenter)

        self.dashBtnLayout_3.addWidget(self.docPromissoryLbl)


        self.dashBtnLayout_2.addLayout(self.dashBtnLayout_3)


        self.dashBtnLayout.addLayout(self.dashBtnLayout_2)


        self.gridLayout.addLayout(self.dashBtnLayout, 0, 0, 1, 1)

        self.dashBtnLayout_4 = QVBoxLayout()
        self.dashBtnLayout_4.setObjectName(u"dashBtnLayout_4")
        self.gradesBtn = QPushButton(self.dashFrame_2)
        self.gradesBtn.setObjectName(u"gradesBtn")
        self.gradesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"icons/dashboard/star-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gradesBtn.setIcon(icon3)
        self.gradesBtn.setIconSize(QSize(80, 80))
        self.gradesBtn.setFlat(True)

        self.dashBtnLayout_4.addWidget(self.gradesBtn)

        self.gradesLbl = QLabel(self.dashFrame_2)
        self.gradesLbl.setObjectName(u"gradesLbl")
        self.gradesLbl.setMaximumSize(QSize(16777215, 64))
        self.gradesLbl.setFont(font9)
        self.gradesLbl.setAlignment(Qt.AlignCenter)

        self.dashBtnLayout_4.addWidget(self.gradesLbl)

        self.dashBtnLayout_5 = QVBoxLayout()
        self.dashBtnLayout_5.setObjectName(u"dashBtnLayout_5")
        self.requestCardBtn = QPushButton(self.dashFrame_2)
        self.requestCardBtn.setObjectName(u"requestCardBtn")
        self.requestCardBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"icons/dashboard/newspaper-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.requestCardBtn.setIcon(icon4)
        self.requestCardBtn.setIconSize(QSize(80, 80))
        self.requestCardBtn.setFlat(True)

        self.dashBtnLayout_5.addWidget(self.requestCardBtn)

        self.requestCardLbl = QLabel(self.dashFrame_2)
        self.requestCardLbl.setObjectName(u"requestCardLbl")
        self.requestCardLbl.setMaximumSize(QSize(16777215, 64))
        self.requestCardLbl.setFont(font9)
        self.requestCardLbl.setAlignment(Qt.AlignCenter)
        self.requestCardLbl.setWordWrap(True)

        self.dashBtnLayout_5.addWidget(self.requestCardLbl)

        self.dashBtnLayout_6 = QVBoxLayout()
        self.dashBtnLayout_6.setObjectName(u"dashBtnLayout_6")
        self.balPromissory = QPushButton(self.dashFrame_2)
        self.balPromissory.setObjectName(u"balPromissory")
        self.balPromissory.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"icons/dashboard/database-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.balPromissory.setIcon(icon5)
        self.balPromissory.setIconSize(QSize(80, 80))
        self.balPromissory.setFlat(True)

        self.dashBtnLayout_6.addWidget(self.balPromissory)

        self.balPromissoryLbl = QLabel(self.dashFrame_2)
        self.balPromissoryLbl.setObjectName(u"balPromissoryLbl")
        self.balPromissoryLbl.setMaximumSize(QSize(16777215, 64))
        self.balPromissoryLbl.setFont(font9)
        self.balPromissoryLbl.setAlignment(Qt.AlignCenter)

        self.dashBtnLayout_6.addWidget(self.balPromissoryLbl)


        self.dashBtnLayout_5.addLayout(self.dashBtnLayout_6)


        self.dashBtnLayout_4.addLayout(self.dashBtnLayout_5)


        self.gridLayout.addLayout(self.dashBtnLayout_4, 0, 1, 1, 1)

        self.dashBtnLayout_7 = QVBoxLayout()
        self.dashBtnLayout_7.setObjectName(u"dashBtnLayout_7")
        self.counselingBtn = QPushButton(self.dashFrame_2)
        self.counselingBtn.setObjectName(u"counselingBtn")
        self.counselingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"icons/pen-to-square-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.counselingBtn.setIcon(icon6)
        self.counselingBtn.setIconSize(QSize(80, 80))
        self.counselingBtn.setFlat(True)

        self.dashBtnLayout_7.addWidget(self.counselingBtn)

        self.counselingLbl = QLabel(self.dashFrame_2)
        self.counselingLbl.setObjectName(u"counselingLbl")
        self.counselingLbl.setMaximumSize(QSize(16777215, 64))
        self.counselingLbl.setFont(font9)
        self.counselingLbl.setAlignment(Qt.AlignCenter)

        self.dashBtnLayout_7.addWidget(self.counselingLbl)

        self.dashBtnLayout_8 = QVBoxLayout()
        self.dashBtnLayout_8.setObjectName(u"dashBtnLayout_8")
        self.accountabilitiesBtn = QPushButton(self.dashFrame_2)
        self.accountabilitiesBtn.setObjectName(u"accountabilitiesBtn")
        self.accountabilitiesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"icons/dashboard/envelope-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountabilitiesBtn.setIcon(icon7)
        self.accountabilitiesBtn.setIconSize(QSize(80, 80))
        self.accountabilitiesBtn.setFlat(True)

        self.dashBtnLayout_8.addWidget(self.accountabilitiesBtn)

        self.accountabilitiesLbl = QLabel(self.dashFrame_2)
        self.accountabilitiesLbl.setObjectName(u"accountabilitiesLbl")
        self.accountabilitiesLbl.setMaximumSize(QSize(16777215, 64))
        self.accountabilitiesLbl.setFont(font9)
        self.accountabilitiesLbl.setAlignment(Qt.AlignCenter)

        self.dashBtnLayout_8.addWidget(self.accountabilitiesLbl)

        self.dashBtnLayout_9 = QVBoxLayout()
        self.dashBtnLayout_9.setObjectName(u"dashBtnLayout_9")
        self.leaveReqBtn = QPushButton(self.dashFrame_2)
        self.leaveReqBtn.setObjectName(u"leaveReqBtn")
        self.leaveReqBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"icons/dashboard/arrow-right-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leaveReqBtn.setIcon(icon8)
        self.leaveReqBtn.setIconSize(QSize(80, 80))
        self.leaveReqBtn.setFlat(True)

        self.dashBtnLayout_9.addWidget(self.leaveReqBtn)

        self.leaveReqLbl = QLabel(self.dashFrame_2)
        self.leaveReqLbl.setObjectName(u"leaveReqLbl")
        self.leaveReqLbl.setMaximumSize(QSize(16777215, 64))
        self.leaveReqLbl.setFont(font9)
        self.leaveReqLbl.setAlignment(Qt.AlignCenter)

        self.dashBtnLayout_9.addWidget(self.leaveReqLbl)


        self.dashBtnLayout_8.addLayout(self.dashBtnLayout_9)


        self.dashBtnLayout_7.addLayout(self.dashBtnLayout_8)


        self.gridLayout.addLayout(self.dashBtnLayout_7, 0, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.dashFrame_2)

        self.pagesWidgets.addWidget(self.dashboard)
        self.subjectsEnrolled = QWidget()
        self.subjectsEnrolled.setObjectName(u"subjectsEnrolled")
        self.subjectsEnrolledVLayout = QVBoxLayout(self.subjectsEnrolled)
        self.subjectsEnrolledVLayout.setObjectName(u"subjectsEnrolledVLayout")
        self.subjectsEnrolledFrame = QFrame(self.subjectsEnrolled)
        self.subjectsEnrolledFrame.setObjectName(u"subjectsEnrolledFrame")
        self.subjectsEnrolledFrame.setMaximumSize(QSize(16777215, 96))
        self.subjectsEnrolledFrame.setFrameShape(QFrame.NoFrame)
        self.subjectsEnrolledFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.subjectsEnrolledFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.subjectsEnrolledLbl = QLabel(self.subjectsEnrolledFrame)
        self.subjectsEnrolledLbl.setObjectName(u"subjectsEnrolledLbl")
        self.subjectsEnrolledLbl.setFont(font8)
        self.subjectsEnrolledLbl.setStyleSheet(u"color: black;")
        self.subjectsEnrolledLbl.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.subjectsEnrolledLbl)


        self.subjectsEnrolledVLayout.addWidget(self.subjectsEnrolledFrame)

        self.subjectsEnrolledFrame_2 = QFrame(self.subjectsEnrolled)
        self.subjectsEnrolledFrame_2.setObjectName(u"subjectsEnrolledFrame_2")
        self.subjectsEnrolledFrame_2.setFrameShape(QFrame.NoFrame)
        self.subjectsEnrolledFrame_2.setFrameShadow(QFrame.Plain)
        self.subjectsEnrolledGridLayout = QGridLayout(self.subjectsEnrolledFrame_2)
        self.subjectsEnrolledGridLayout.setObjectName(u"subjectsEnrolledGridLayout")
        self.subjectsTableWidget = QTableWidget(self.subjectsEnrolledFrame_2)
        if (self.subjectsTableWidget.columnCount() < 5):
            self.subjectsTableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.subjectsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.subjectsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.subjectsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.subjectsTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.subjectsTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.subjectsTableWidget.setObjectName(u"subjectsTableWidget")
        font10 = QFont()
        font10.setFamilies([u"Montserrat Medium"])
        font10.setPointSize(10)
        self.subjectsTableWidget.setFont(font10)
        self.subjectsTableWidget.setFrameShape(QFrame.NoFrame)
        self.subjectsTableWidget.setFrameShadow(QFrame.Plain)
        self.subjectsTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.subjectsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.subjectsTableWidget.setTabKeyNavigation(False)
        self.subjectsTableWidget.setProperty("showDropIndicator", False)
        self.subjectsTableWidget.setDragDropOverwriteMode(False)
        self.subjectsTableWidget.setAlternatingRowColors(True)
        self.subjectsTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.subjectsTableWidget.setTextElideMode(Qt.ElideLeft)
        self.subjectsTableWidget.setSortingEnabled(True)
        self.subjectsTableWidget.setRowCount(0)
        self.subjectsTableWidget.setColumnCount(5)
        self.subjectsTableWidget.horizontalHeader().setVisible(False)
        self.subjectsTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.subjectsTableWidget.horizontalHeader().setHighlightSections(True)
        self.subjectsTableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.subjectsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.subjectsTableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.subjectsTableWidget.verticalHeader().setHighlightSections(True)
        self.subjectsTableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.subjectsTableWidget.verticalHeader().setStretchLastSection(True)

        self.subjectsEnrolledGridLayout.addWidget(self.subjectsTableWidget, 0, 0, 1, 1)


        self.subjectsEnrolledVLayout.addWidget(self.subjectsEnrolledFrame_2)

        self.pagesWidgets.addWidget(self.subjectsEnrolled)
        self.qrCode = QWidget()
        self.qrCode.setObjectName(u"qrCode")
        self.verticalLayout_2 = QVBoxLayout(self.qrCode)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.qrCodeFrame = QFrame(self.qrCode)
        self.qrCodeFrame.setObjectName(u"qrCodeFrame")
        self.qrCodeFrame.setMaximumSize(QSize(16777215, 96))
        self.qrCodeFrame.setFrameShape(QFrame.NoFrame)
        self.qrCodeFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.qrCodeFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.qrCodeLbl = QLabel(self.qrCodeFrame)
        self.qrCodeLbl.setObjectName(u"qrCodeLbl")
        self.qrCodeLbl.setFont(font8)
        self.qrCodeLbl.setStyleSheet(u"color: black;")
        self.qrCodeLbl.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.qrCodeLbl)


        self.verticalLayout_2.addWidget(self.qrCodeFrame)

        self.qrCodeInfo = QFrame(self.qrCode)
        self.qrCodeInfo.setObjectName(u"qrCodeInfo")
        self.qrCodeInfo.setFrameShape(QFrame.StyledPanel)
        self.qrCodeInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.qrCodeInfo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.qrCodePic = QLabel(self.qrCodeInfo)
        self.qrCodePic.setObjectName(u"qrCodePic")
        self.qrCodePic.setMaximumSize(QSize(384, 384))
        self.qrCodePic.setScaledContents(True)
        self.qrCodePic.setAlignment(Qt.AlignCenter)
        self.qrCodePic.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.qrCodePic)

        self.qrInfo = QLabel(self.qrCodeInfo)
        self.qrInfo.setObjectName(u"qrInfo")
        self.qrInfo.setMaximumSize(QSize(16777215, 64))
        font11 = QFont()
        font11.setFamilies([u"Montserrat Medium"])
        font11.setPointSize(18)
        self.qrInfo.setFont(font11)

        self.verticalLayout_4.addWidget(self.qrInfo)


        self.verticalLayout_2.addWidget(self.qrCodeInfo)

        self.pagesWidgets.addWidget(self.qrCode)
        self.grades = QWidget()
        self.grades.setObjectName(u"grades")
        font12 = QFont()
        font12.setFamilies([u"Montserrat Medium"])
        self.grades.setFont(font12)
        self.verticalLayout_6 = QVBoxLayout(self.grades)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gradesFrame = QFrame(self.grades)
        self.gradesFrame.setObjectName(u"gradesFrame")
        self.gradesFrame.setMaximumSize(QSize(16777215, 96))
        self.gradesFrame.setFrameShape(QFrame.NoFrame)
        self.gradesFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.gradesFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gradesHeaderLbl = QLabel(self.gradesFrame)
        self.gradesHeaderLbl.setObjectName(u"gradesHeaderLbl")
        self.gradesHeaderLbl.setFont(font8)
        self.gradesHeaderLbl.setStyleSheet(u"color: black;")
        self.gradesHeaderLbl.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.gradesHeaderLbl)


        self.verticalLayout_6.addWidget(self.gradesFrame)

        self.gradesFrame_2 = QFrame(self.grades)
        self.gradesFrame_2.setObjectName(u"gradesFrame_2")
        self.gradesFrame_2.setFrameShape(QFrame.NoFrame)
        self.gradesFrame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.gradesFrame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gradesTableWidget = QTableWidget(self.gradesFrame_2)
        if (self.gradesTableWidget.columnCount() < 7):
            self.gradesTableWidget.setColumnCount(7)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.gradesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.gradesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.gradesTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.gradesTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.gradesTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.gradesTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        __qtablewidgetitem11.setBackground(QColor(0, 0, 0, 1));
        self.gradesTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        self.gradesTableWidget.setObjectName(u"gradesTableWidget")
        self.gradesTableWidget.setFont(font10)
        self.gradesTableWidget.setFrameShape(QFrame.NoFrame)
        self.gradesTableWidget.setFrameShadow(QFrame.Plain)
        self.gradesTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.gradesTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.gradesTableWidget.setTabKeyNavigation(False)
        self.gradesTableWidget.setProperty("showDropIndicator", False)
        self.gradesTableWidget.setDragDropOverwriteMode(False)
        self.gradesTableWidget.setAlternatingRowColors(True)
        self.gradesTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.gradesTableWidget.setTextElideMode(Qt.ElideLeft)
        self.gradesTableWidget.setSortingEnabled(True)
        self.gradesTableWidget.setRowCount(0)
        self.gradesTableWidget.setColumnCount(7)
        self.gradesTableWidget.horizontalHeader().setVisible(False)
        self.gradesTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.gradesTableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.gradesTableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.gradesTableWidget.horizontalHeader().setHighlightSections(True)
        self.gradesTableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.gradesTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gradesTableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.gradesTableWidget.verticalHeader().setMinimumSectionSize(23)
        self.gradesTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.gradesTableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.gradesTableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.gradesTableWidget, 0, 6, 1, 1)


        self.verticalLayout_6.addWidget(self.gradesFrame_2)

        self.pagesWidgets.addWidget(self.grades)
        self.assessment = QWidget()
        self.assessment.setObjectName(u"assessment")
        self.verticalLayout_7 = QVBoxLayout(self.assessment)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.assessmentFrame = QFrame(self.assessment)
        self.assessmentFrame.setObjectName(u"assessmentFrame")
        self.assessmentFrame.setMaximumSize(QSize(16777215, 96))
        self.assessmentFrame.setFrameShape(QFrame.NoFrame)
        self.assessmentFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.assessmentFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.assessmentLbl_2 = QLabel(self.assessmentFrame)
        self.assessmentLbl_2.setObjectName(u"assessmentLbl_2")
        self.assessmentLbl_2.setFont(font8)
        self.assessmentLbl_2.setStyleSheet(u"color: black;")
        self.assessmentLbl_2.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.assessmentLbl_2)

        self.semesterFrame = QFrame(self.assessmentFrame)
        self.semesterFrame.setObjectName(u"semesterFrame")
        self.semesterFrame.setFrameShape(QFrame.StyledPanel)
        self.semesterFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.semesterFrame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.semesterHeaderLbl = QLabel(self.semesterFrame)
        self.semesterHeaderLbl.setObjectName(u"semesterHeaderLbl")
        self.semesterHeaderLbl.setFont(font11)

        self.verticalLayout_20.addWidget(self.semesterHeaderLbl)

        self.semesterYearLbl = QLabel(self.semesterFrame)
        self.semesterYearLbl.setObjectName(u"semesterYearLbl")
        self.semesterYearLbl.setFont(font1)

        self.verticalLayout_20.addWidget(self.semesterYearLbl)


        self.horizontalLayout_7.addWidget(self.semesterFrame)


        self.verticalLayout_7.addWidget(self.assessmentFrame)

        self.assessmentFrame_2 = QFrame(self.assessment)
        self.assessmentFrame_2.setObjectName(u"assessmentFrame_2")
        self.assessmentFrame_2.setFrameShape(QFrame.NoFrame)
        self.assessmentFrame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.assessmentFrame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.yrLvlFrame = QFrame(self.assessmentFrame_2)
        self.yrLvlFrame.setObjectName(u"yrLvlFrame")
        self.yrLvlFrame.setFrameShape(QFrame.StyledPanel)
        self.yrLvlFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.yrLvlFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.yrLvlHeaderLbl = QLabel(self.yrLvlFrame)
        self.yrLvlHeaderLbl.setObjectName(u"yrLvlHeaderLbl")
        font13 = QFont()
        font13.setFamilies([u"Montserrat Medium"])
        font13.setPointSize(18)
        font13.setBold(True)
        self.yrLvlHeaderLbl.setFont(font13)

        self.verticalLayout_9.addWidget(self.yrLvlHeaderLbl)

        self.yrLvlInfoLbl = QLabel(self.yrLvlFrame)
        self.yrLvlInfoLbl.setObjectName(u"yrLvlInfoLbl")
        font14 = QFont()
        font14.setFamilies([u"Montserrat Medium"])
        font14.setPointSize(14)
        self.yrLvlInfoLbl.setFont(font14)

        self.verticalLayout_9.addWidget(self.yrLvlInfoLbl)


        self.gridLayout_3.addWidget(self.yrLvlFrame, 0, 3, 1, 1)

        self.downpaymentFrame = QFrame(self.assessmentFrame_2)
        self.downpaymentFrame.setObjectName(u"downpaymentFrame")
        self.downpaymentFrame.setFrameShape(QFrame.StyledPanel)
        self.downpaymentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.downpaymentFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.downpaymentHeaderLbl = QLabel(self.downpaymentFrame)
        self.downpaymentHeaderLbl.setObjectName(u"downpaymentHeaderLbl")
        self.downpaymentHeaderLbl.setFont(font13)

        self.verticalLayout_10.addWidget(self.downpaymentHeaderLbl)

        self.downpaymentInfoLbl = QLabel(self.downpaymentFrame)
        self.downpaymentInfoLbl.setObjectName(u"downpaymentInfoLbl")
        self.downpaymentInfoLbl.setFont(font14)

        self.verticalLayout_10.addWidget(self.downpaymentInfoLbl)


        self.gridLayout_3.addWidget(self.downpaymentFrame, 0, 4, 1, 1)

        self.regNoFrame = QFrame(self.assessmentFrame_2)
        self.regNoFrame.setObjectName(u"regNoFrame")
        self.regNoFrame.setFrameShape(QFrame.StyledPanel)
        self.regNoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.regNoFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.regHeaderLbl = QLabel(self.regNoFrame)
        self.regHeaderLbl.setObjectName(u"regHeaderLbl")
        self.regHeaderLbl.setFont(font13)
        self.regHeaderLbl.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.regHeaderLbl)

        self.regInfoLbl = QLabel(self.regNoFrame)
        self.regInfoLbl.setObjectName(u"regInfoLbl")
        self.regInfoLbl.setFont(font14)

        self.verticalLayout_8.addWidget(self.regInfoLbl)


        self.gridLayout_3.addWidget(self.regNoFrame, 0, 2, 1, 1)

        self.preFinalFrame = QFrame(self.assessmentFrame_2)
        self.preFinalFrame.setObjectName(u"preFinalFrame")
        self.preFinalFrame.setFrameShape(QFrame.StyledPanel)
        self.preFinalFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.preFinalFrame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.preFinalHeaderLbl = QLabel(self.preFinalFrame)
        self.preFinalHeaderLbl.setObjectName(u"preFinalHeaderLbl")
        self.preFinalHeaderLbl.setFont(font13)
        self.preFinalHeaderLbl.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.preFinalHeaderLbl)

        self.preFinalInfoLbl = QLabel(self.preFinalFrame)
        self.preFinalInfoLbl.setObjectName(u"preFinalInfoLbl")
        self.preFinalInfoLbl.setFont(font14)

        self.verticalLayout_19.addWidget(self.preFinalInfoLbl)


        self.gridLayout_3.addWidget(self.preFinalFrame, 1, 4, 1, 1)

        self.prelimsFrame = QFrame(self.assessmentFrame_2)
        self.prelimsFrame.setObjectName(u"prelimsFrame")
        self.prelimsFrame.setFrameShape(QFrame.StyledPanel)
        self.prelimsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.prelimsFrame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.prelimsHeaderLbl = QLabel(self.prelimsFrame)
        self.prelimsHeaderLbl.setObjectName(u"prelimsHeaderLbl")
        self.prelimsHeaderLbl.setFont(font13)
        self.prelimsHeaderLbl.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.prelimsHeaderLbl)

        self.prelimsInfoLbl = QLabel(self.prelimsFrame)
        self.prelimsInfoLbl.setObjectName(u"prelimsInfoLbl")
        self.prelimsInfoLbl.setFont(font14)

        self.verticalLayout_17.addWidget(self.prelimsInfoLbl)


        self.gridLayout_3.addWidget(self.prelimsFrame, 1, 2, 1, 1)

        self.midtermsFrame = QFrame(self.assessmentFrame_2)
        self.midtermsFrame.setObjectName(u"midtermsFrame")
        self.midtermsFrame.setFrameShape(QFrame.StyledPanel)
        self.midtermsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.midtermsFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.midtermsHeaderLbl = QLabel(self.midtermsFrame)
        self.midtermsHeaderLbl.setObjectName(u"midtermsHeaderLbl")
        self.midtermsHeaderLbl.setFont(font13)
        self.midtermsHeaderLbl.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.midtermsHeaderLbl)

        self.midtermsInfoLbl = QLabel(self.midtermsFrame)
        self.midtermsInfoLbl.setObjectName(u"midtermsInfoLbl")
        self.midtermsInfoLbl.setFont(font14)

        self.verticalLayout_18.addWidget(self.midtermsInfoLbl)


        self.gridLayout_3.addWidget(self.midtermsFrame, 1, 3, 1, 1)

        self.finalsFrame = QFrame(self.assessmentFrame_2)
        self.finalsFrame.setObjectName(u"finalsFrame")
        self.finalsFrame.setFrameShape(QFrame.StyledPanel)
        self.finalsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.finalsFrame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.finalsHeaderLbl = QLabel(self.finalsFrame)
        self.finalsHeaderLbl.setObjectName(u"finalsHeaderLbl")
        self.finalsHeaderLbl.setFont(font13)
        self.finalsHeaderLbl.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.finalsHeaderLbl)

        self.finalsInfoLbl = QLabel(self.finalsFrame)
        self.finalsInfoLbl.setObjectName(u"finalsInfoLbl")
        self.finalsInfoLbl.setFont(font14)

        self.verticalLayout_21.addWidget(self.finalsInfoLbl)


        self.gridLayout_3.addWidget(self.finalsFrame, 2, 2, 1, 1)

        self.totalBalanceFrame = QFrame(self.assessmentFrame_2)
        self.totalBalanceFrame.setObjectName(u"totalBalanceFrame")
        self.totalBalanceFrame.setFrameShape(QFrame.StyledPanel)
        self.totalBalanceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.totalBalanceFrame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.totalBalanceHeaderLbl = QLabel(self.totalBalanceFrame)
        self.totalBalanceHeaderLbl.setObjectName(u"totalBalanceHeaderLbl")
        self.totalBalanceHeaderLbl.setFont(font13)
        self.totalBalanceHeaderLbl.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.totalBalanceHeaderLbl)

        self.totalBalanceInfoLbl = QLabel(self.totalBalanceFrame)
        self.totalBalanceInfoLbl.setObjectName(u"totalBalanceInfoLbl")
        self.totalBalanceInfoLbl.setFont(font14)

        self.verticalLayout_22.addWidget(self.totalBalanceInfoLbl)


        self.gridLayout_3.addWidget(self.totalBalanceFrame, 2, 3, 1, 2)


        self.verticalLayout_7.addWidget(self.assessmentFrame_2)

        self.pagesWidgets.addWidget(self.assessment)
        self.assessmentSemsFrame = QWidget()
        self.assessmentSemsFrame.setObjectName(u"assessmentSemsFrame")
        self.assessmentSemsFrame.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: black;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid black;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.assessmentSemsFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.assessmentSemsFrame_3 = QFrame(self.assessmentSemsFrame)
        self.assessmentSemsFrame_3.setObjectName(u"assessmentSemsFrame_3")
        self.assessmentSemsFrame_3.setMaximumSize(QSize(16777215, 96))
        self.assessmentSemsFrame_3.setFrameShape(QFrame.NoFrame)
        self.assessmentSemsFrame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.assessmentSemsFrame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.assessmentLbl_3 = QLabel(self.assessmentSemsFrame_3)
        self.assessmentLbl_3.setObjectName(u"assessmentLbl_3")
        self.assessmentLbl_3.setFont(font8)
        self.assessmentLbl_3.setStyleSheet(u"color: black;")
        self.assessmentLbl_3.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.assessmentLbl_3)


        self.verticalLayout_11.addWidget(self.assessmentSemsFrame_3)

        self.assessmentSemsFrame_2 = QFrame(self.assessmentSemsFrame)
        self.assessmentSemsFrame_2.setObjectName(u"assessmentSemsFrame_2")
        self.assessmentSemsFrame_2.setFrameShape(QFrame.StyledPanel)
        self.assessmentSemsFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.assessmentSemsFrame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.firstYearFrame = QFrame(self.assessmentSemsFrame_2)
        self.firstYearFrame.setObjectName(u"firstYearFrame")
        self.firstYearFrame.setFrameShape(QFrame.StyledPanel)
        self.firstYearFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.firstYearFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.firstYearLbl = QLabel(self.firstYearFrame)
        self.firstYearLbl.setObjectName(u"firstYearLbl")
        self.firstYearLbl.setMaximumSize(QSize(16777215, 32))
        font15 = QFont()
        font15.setFamilies([u"Montserrat Medium"])
        font15.setPointSize(24)
        self.firstYearLbl.setFont(font15)

        self.verticalLayout_13.addWidget(self.firstYearLbl)

        self.firstYearFrame_2 = QFrame(self.firstYearFrame)
        self.firstYearFrame_2.setObjectName(u"firstYearFrame_2")
        self.firstYearFrame_2.setFrameShape(QFrame.StyledPanel)
        self.firstYearFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.firstYearFrame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.firstYear1stSemBtn = QPushButton(self.firstYearFrame_2)
        self.firstYear1stSemBtn.setObjectName(u"firstYear1stSemBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.firstYear1stSemBtn.sizePolicy().hasHeightForWidth())
        self.firstYear1stSemBtn.setSizePolicy(sizePolicy1)
        font16 = QFont()
        font16.setFamilies([u"Montserrat Medium"])
        font16.setPointSize(24)
        font16.setBold(True)
        self.firstYear1stSemBtn.setFont(font16)
        self.firstYear1stSemBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.firstYear1stSemBtn)

        self.firstYear2ndSemBtn = QPushButton(self.firstYearFrame_2)
        self.firstYear2ndSemBtn.setObjectName(u"firstYear2ndSemBtn")
        sizePolicy1.setHeightForWidth(self.firstYear2ndSemBtn.sizePolicy().hasHeightForWidth())
        self.firstYear2ndSemBtn.setSizePolicy(sizePolicy1)
        font17 = QFont()
        font17.setFamilies([u"Montserrat Medium"])
        font17.setPointSize(24)
        font17.setBold(True)
        font17.setStyleStrategy(QFont.PreferDefault)
        self.firstYear2ndSemBtn.setFont(font17)
        self.firstYear2ndSemBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.firstYear2ndSemBtn)


        self.verticalLayout_13.addWidget(self.firstYearFrame_2)


        self.verticalLayout_12.addWidget(self.firstYearFrame)


        self.verticalLayout_11.addWidget(self.assessmentSemsFrame_2)

        self.secondYearFrame = QFrame(self.assessmentSemsFrame)
        self.secondYearFrame.setObjectName(u"secondYearFrame")
        self.secondYearFrame.setFrameShape(QFrame.StyledPanel)
        self.secondYearFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.secondYearFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.secondYearLbl = QLabel(self.secondYearFrame)
        self.secondYearLbl.setObjectName(u"secondYearLbl")
        self.secondYearLbl.setMaximumSize(QSize(16777215, 32))
        self.secondYearLbl.setFont(font15)

        self.verticalLayout_14.addWidget(self.secondYearLbl)

        self.secondYearFrame_2 = QFrame(self.secondYearFrame)
        self.secondYearFrame_2.setObjectName(u"secondYearFrame_2")
        self.secondYearFrame_2.setFrameShape(QFrame.StyledPanel)
        self.secondYearFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.secondYearFrame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.secondYear1stSemBtn = QPushButton(self.secondYearFrame_2)
        self.secondYear1stSemBtn.setObjectName(u"secondYear1stSemBtn")
        sizePolicy1.setHeightForWidth(self.secondYear1stSemBtn.sizePolicy().hasHeightForWidth())
        self.secondYear1stSemBtn.setSizePolicy(sizePolicy1)
        self.secondYear1stSemBtn.setFont(font16)
        self.secondYear1stSemBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.secondYear1stSemBtn)

        self.secondYear2ndSemBtn = QPushButton(self.secondYearFrame_2)
        self.secondYear2ndSemBtn.setObjectName(u"secondYear2ndSemBtn")
        sizePolicy1.setHeightForWidth(self.secondYear2ndSemBtn.sizePolicy().hasHeightForWidth())
        self.secondYear2ndSemBtn.setSizePolicy(sizePolicy1)
        self.secondYear2ndSemBtn.setFont(font16)
        self.secondYear2ndSemBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.secondYear2ndSemBtn)


        self.verticalLayout_14.addWidget(self.secondYearFrame_2)


        self.verticalLayout_11.addWidget(self.secondYearFrame)

        self.pagesWidgets.addWidget(self.assessmentSemsFrame)

        self.verticalLayout_3.addWidget(self.pagesWidgets)


        self.vLayout.addWidget(self.pagesFrame)

        self.statusBarInfo = QFrame(self.vLayoutFrame)
        self.statusBarInfo.setObjectName(u"statusBarInfo")
        self.statusBarInfo.setMaximumSize(QSize(16777215, 82))
        self.statusBarInfo.setFont(font7)
        self.statusBarInfo.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}")
        self.statusBarInfo.setFrameShape(QFrame.NoFrame)
        self.statusBarInfo.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.statusBarInfo)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.userIcon = QLabel(self.statusBarInfo)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setMaximumSize(QSize(48, 48))
        self.userIcon.setFont(font7)
        self.userIcon.setPixmap(QPixmap(u"icons/user-solid.svg"))
        self.userIcon.setScaledContents(True)
        self.userIcon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.userIcon)

        self.userStatusLayout = QVBoxLayout()
        self.userStatusLayout.setObjectName(u"userStatusLayout")
        self.userName = QLabel(self.statusBarInfo)
        self.userName.setObjectName(u"userName")
        self.userName.setFont(font2)

        self.userStatusLayout.addWidget(self.userName)

        self.userCourseYear = QLabel(self.statusBarInfo)
        self.userCourseYear.setObjectName(u"userCourseYear")
        font18 = QFont()
        font18.setFamilies([u"Montserrat Medium"])
        font18.setPointSize(10)
        font18.setBold(False)
        font18.setItalic(True)
        self.userCourseYear.setFont(font18)
        self.userCourseYear.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.userStatusLayout.addWidget(self.userCourseYear)

        self.userStudentID = QLabel(self.statusBarInfo)
        self.userStudentID.setObjectName(u"userStudentID")
        font19 = QFont()
        font19.setFamilies([u"Montserrat Medium"])
        font19.setPointSize(10)
        font19.setItalic(True)
        self.userStudentID.setFont(font19)

        self.userStatusLayout.addWidget(self.userStudentID)


        self.horizontalLayout_3.addLayout(self.userStatusLayout)


        self.vLayout.addWidget(self.statusBarInfo)

        studentMainWindow.setCentralWidget(self.studentMainWidget)

        self.retranslateUi(studentMainWindow)

        self.pagesWidgets.setCurrentIndex(4)
        self.corBtn.setDefault(False)
        self.counselingBtn.setDefault(False)


        QMetaObject.connectSlotsByName(studentMainWindow)
    # setupUi

    def retranslateUi(self, studentMainWindow):
        studentMainWindow.setWindowTitle(QCoreApplication.translate("studentMainWindow", u"Student Information", None))
        self.burgerTitle.setText(QCoreApplication.translate("studentMainWindow", u"BSIT Info", None))
        self.dashboardBtn.setText(QCoreApplication.translate("studentMainWindow", u"Dashboard", None))
        self.subjectsEnrolledBtn.setText(QCoreApplication.translate("studentMainWindow", u"Subjects Enrolled", None))
        self.qrCodeBtn.setText(QCoreApplication.translate("studentMainWindow", u"QR Code", None))
        self.enrollmentBtn.setText(QCoreApplication.translate("studentMainWindow", u"Enrollment", None))
        self.editProfileBtn.setText(QCoreApplication.translate("studentMainWindow", u"Edit Profile Info", None))
        self.helpBtn.setText(QCoreApplication.translate("studentMainWindow", u"Help", None))
        self.logoutBtn.setText(QCoreApplication.translate("studentMainWindow", u"Log-out", None))
        self.welcomeLbl.setText(QCoreApplication.translate("studentMainWindow", u"Welcome, Jhon Lloyd Viernes", None))
        self.assessmentBtn.setText("")
        self.assessmentLbl.setText(QCoreApplication.translate("studentMainWindow", u"Assessment", None))
        self.corBtn.setText("")
        self.corLbl.setText(QCoreApplication.translate("studentMainWindow", u"COR", None))
        self.docPromissoryBtn.setText("")
        self.docPromissoryLbl.setText(QCoreApplication.translate("studentMainWindow", u"Document Promissory", None))
        self.gradesBtn.setText("")
        self.gradesLbl.setText(QCoreApplication.translate("studentMainWindow", u"Grades", None))
        self.requestCardBtn.setText("")
        self.requestCardLbl.setText(QCoreApplication.translate("studentMainWindow", u"Request for Report Card", None))
        self.balPromissory.setText("")
        self.balPromissoryLbl.setText(QCoreApplication.translate("studentMainWindow", u"Balance Promissory", None))
        self.counselingBtn.setText("")
        self.counselingLbl.setText(QCoreApplication.translate("studentMainWindow", u"Counseling", None))
        self.accountabilitiesBtn.setText("")
        self.accountabilitiesLbl.setText(QCoreApplication.translate("studentMainWindow", u"Accountabilities", None))
        self.leaveReqBtn.setText("")
        self.leaveReqLbl.setText(QCoreApplication.translate("studentMainWindow", u"Leave Request", None))
        self.subjectsEnrolledLbl.setText(QCoreApplication.translate("studentMainWindow", u"Subjects Enrolled", None))
        ___qtablewidgetitem = self.subjectsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("studentMainWindow", u"Code", None));
        ___qtablewidgetitem1 = self.subjectsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("studentMainWindow", u"Subject", None));
        ___qtablewidgetitem2 = self.subjectsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("studentMainWindow", u"Credit Unit", None));
        ___qtablewidgetitem3 = self.subjectsTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("studentMainWindow", u"Section", None));
        ___qtablewidgetitem4 = self.subjectsTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("studentMainWindow", u"Schedule", None));
        self.qrCodeLbl.setText(QCoreApplication.translate("studentMainWindow", u"QR Code", None))
        self.qrCodePic.setText("")
        self.qrInfo.setText("")
        self.gradesHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"Grades", None))
        ___qtablewidgetitem5 = self.gradesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("studentMainWindow", u"Code", None));
        ___qtablewidgetitem6 = self.gradesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("studentMainWindow", u"Subject", None));
        ___qtablewidgetitem7 = self.gradesTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("studentMainWindow", u"Credit Unit", None));
        ___qtablewidgetitem8 = self.gradesTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("studentMainWindow", u"Midterm", None));
        ___qtablewidgetitem9 = self.gradesTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("studentMainWindow", u"Final", None));
        ___qtablewidgetitem10 = self.gradesTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("studentMainWindow", u"Re-Exam", None));
        ___qtablewidgetitem11 = self.gradesTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("studentMainWindow", u"Remarks", None));
        self.assessmentLbl_2.setText(QCoreApplication.translate("studentMainWindow", u"Assessment", None))
        self.semesterHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"SEMESTER INFO", None))
        self.semesterYearLbl.setText(QCoreApplication.translate("studentMainWindow", u"YEAR", None))
        self.yrLvlHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"Year Level", None))
        self.yrLvlInfoLbl.setText(QCoreApplication.translate("studentMainWindow", u"TextLabel", None))
        self.downpaymentHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"Downpayment", None))
        self.downpaymentInfoLbl.setText(QCoreApplication.translate("studentMainWindow", u"TextLabel", None))
        self.regHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"Registration Number", None))
        self.regInfoLbl.setText(QCoreApplication.translate("studentMainWindow", u"TextLabel", None))
        self.preFinalHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"Pre-Final", None))
        self.preFinalInfoLbl.setText(QCoreApplication.translate("studentMainWindow", u"TextLabel", None))
        self.prelimsHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"Prelim", None))
        self.prelimsInfoLbl.setText(QCoreApplication.translate("studentMainWindow", u"TextLabel", None))
        self.midtermsHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"Midterm", None))
        self.midtermsInfoLbl.setText(QCoreApplication.translate("studentMainWindow", u"TextLabel", None))
        self.finalsHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"Final", None))
        self.finalsInfoLbl.setText(QCoreApplication.translate("studentMainWindow", u"TextLabel", None))
        self.totalBalanceHeaderLbl.setText(QCoreApplication.translate("studentMainWindow", u"Total Balance", None))
        self.totalBalanceInfoLbl.setText(QCoreApplication.translate("studentMainWindow", u"TextLabel", None))
        self.assessmentLbl_3.setText(QCoreApplication.translate("studentMainWindow", u"Assessments", None))
        self.firstYearLbl.setText(QCoreApplication.translate("studentMainWindow", u"1st Year", None))
        self.firstYear1stSemBtn.setText(QCoreApplication.translate("studentMainWindow", u"1st Semester", None))
        self.firstYear2ndSemBtn.setText(QCoreApplication.translate("studentMainWindow", u"2nd Semester", None))
        self.secondYearLbl.setText(QCoreApplication.translate("studentMainWindow", u"2nd Year", None))
        self.secondYear1stSemBtn.setText(QCoreApplication.translate("studentMainWindow", u"1st Semester", None))
        self.secondYear2ndSemBtn.setText(QCoreApplication.translate("studentMainWindow", u"2nd Semester", None))
        self.userName.setText(QCoreApplication.translate("studentMainWindow", u"VIERNES, JHON LLOYD D.", None))
        self.userCourseYear.setText(QCoreApplication.translate("studentMainWindow", u"1st Year - BSIT-1R13", None))
        self.userStudentID.setText(QCoreApplication.translate("studentMainWindow", u"2022301xxxx", None))
    # retranslateUi

