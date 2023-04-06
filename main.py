from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtDesigner import *
from PySide6.QtWidgets import *
from ui_STS import Ui_studentMainWindow
from ui_LOGIN import Ui_loginWindow
import sys
import json
import qrcode

mainDataJson = "./mainData.json"

class loginApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.loginUI = Ui_loginWindow()
        self.loginUI.setupUi(self)
        self.initBtns()
        self.setWindowIcon(QPixmap("./ustp logo.png"))

        self.studentID = None

    def initBtns(self):
        loginBtn = self.loginUI.loginBtn

        loginBtn.clicked.connect(lambda: self.loginUser())

    def keyPressEvent(self, event):
        loginBtn = self.loginUI.loginBtn
        key = event.key()

        if key == Qt.Key_Enter:
            lambda: self.loginUser()
        else:
            super().keyPressEvent(event)

    def loginUser(self):
        userInput = self.loginUI.userInput
        passInput = self.loginUI.passInput

        alertMsgBox = QMessageBox(self)

        with open(mainDataJson, 'r') as data:
            temp = json.load(data)
            for index, values in enumerate(temp):
                if userInput.text() == "":
                    alertMsgBox.setWindowTitle("Invalid Username")
                    alertMsgBox.setText("Empty username, please enter a valid username.")
                    alertMsgBox.exec()
                elif passInput.text() == "":
                    alertMsgBox.setWindowTitle("Invalid Password")
                    alertMsgBox.setText("Empty password, please enter a valid password.")
                    alertMsgBox.exec()
                else:
                    for k, v in values.items():
                        if k == "studentIDNumber":
                            if v == int(userInput.text()):
                                if values["password"] == passInput.text():
                                    self.studentID = int(userInput.text())
                                    self.destroy()
                                    self.initializeStudentApp()
                                else:
                                    alertMsgBox.setWindowTitle("Invalid Password")
                                    alertMsgBox.setText("Wrong password.")
                                    alertMsgBox.exec()
           
    def getUser(self):
        return self.loginUI.userInput.text()
    
    def initializeStudentApp(self):
        self.studentApp = mainApp(self.studentID)
        self.studentApp.show()

class mainApp(QMainWindow):
    def __init__(self, studentID: int):
        super().__init__()
        self.setWindowIcon(QPixmap("./ustp logo.png"))
        
        self.userDataIndex = 0
        self.mainUI = Ui_studentMainWindow()
        self.mainUI.setupUi(self)
        self.initBtns()
        self.findUser(studentID)

    def findUser(self, idNumber):
        with open(mainDataJson, 'r') as data:
            studentData = json.load(data)
            for index, values in enumerate(studentData):
                for k, v in values.items():
                    if k == "studentIDNumber":
                        if v == idNumber:
                            self.userDataIndex = index
                            self.readSubjectsEnrolledData()
                            self.readGradesData()
                            self.changeGreetings()
                            self.makeQrCode()

    def makeQrCode(self):
        qrCodePicWidget = self.mainUI.qrCodePic
        qrName = self.mainUI.qrInfo

        with open(mainDataJson, 'r') as data:
            studentData = json.load(data)
            name = studentData[self.userDataIndex]["name"]
            idNumber = str(studentData[self.userDataIndex]["studentIDNumber"])

            tempImg = qrcode.make(f"{name} - {idNumber}")
            tempImg.save("./qr/temp.png")
            
            qrCodePicWidget.setPixmap(QPixmap("./qr/temp.png"))
            qrName.setText(f"{name}\n{idNumber}")

    def changeGreetings(self):
        welcomeLbl = self.mainUI.welcomeLbl
        userIndex = self.userDataIndex
        with open(mainDataJson, 'r') as data:
            studentData = json.load(data)
            welcomeLbl.setText(f"Welcome, " + studentData[userIndex]["name"])

    def initBtns(self):
        self.pages = self.mainUI.pagesWidgets
        dashboardBtn = self.mainUI.dashboardBtn
        subjectsEnrolledBtn = self.mainUI.subjectsEnrolledBtn
        gradesBtn = self.mainUI.gradesBtn
        qrCodeBtn = self.mainUI.qrCodeBtn
        assessmentBtn = self.mainUI.assessmentBtn

        firstYear1stSemBtn = self.mainUI.firstYear1stSemBtn
        firstYear2ndSemBtn = self.mainUI.firstYear2ndSemBtn
        secondYear1stSemBtn = self.mainUI.secondYear1stSemBtn
        secondYear2ndSemBtn = self.mainUI.secondYear2ndSemBtn

        dashboardBtn.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        subjectsEnrolledBtn.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        qrCodeBtn.clicked.connect(lambda: self.pages.setCurrentIndex(2))
        gradesBtn.clicked.connect(lambda: self.pages.setCurrentIndex(3))
        assessmentBtn.clicked.connect(lambda: self.pages.setCurrentIndex(5))

        firstYear1stSemBtn.clicked.connect(lambda: self.openAssessmentPage("1st", 0))
        firstYear2ndSemBtn.clicked.connect(lambda: self.openAssessmentPage("1st", 1))
        secondYear1stSemBtn.clicked.connect(lambda: self.openAssessmentPage("2nd", 0))
        secondYear2ndSemBtn.clicked.connect(lambda: self.openAssessmentPage("2nd", 1))

        self.pages.setCurrentIndex(0)

    def readSubjectsEnrolledData(self):
        subjectsTable = self.mainUI.subjectsTableWidget

        with open(mainDataJson, 'r') as data:
            studentData = json.load(data)
            subjectsTable.setRowCount(len(studentData[self.userDataIndex]["subjectsEnrolled"]))
            self.readData(studentData[self.userDataIndex]["subjectsEnrolled"], subjectsTable, "subjects")

    def openAssessmentPage(self, year, semester: int):
        # 1st year / 1st sem - 0
        # 1st year / 2nd sem - 1
        # 2nd year / 1st sem - 2
        # 2nd year / 2nd sem - 3

        self.readAssessmentData(year, semester)
        self.pages.setCurrentIndex(4)

    def readGradesData(self):
        gradesTable = self.mainUI.gradesTableWidget
        
        with open(mainDataJson, 'r') as data:
            studentData = json.load(data)
            gradesTable.setRowCount(len(studentData[self.userDataIndex]["subjectsEnrolled"]))
            self.readData(studentData[self.userDataIndex]["subjectsEnrolled"], gradesTable, "grades")

    def readAssessmentData(self, year, semester: int):
        # 0 - 1st semester
        # 1 - 2nd semester
        # 2 - 3rd semester
        # 3 - 4th semester

        regNo = self.mainUI.regInfoLbl
        yrLvl = self.mainUI.yrLvlInfoLbl
        downpayment = self.mainUI.downpaymentInfoLbl
        prelim = self.mainUI.prelimsInfoLbl
        midterm = self.mainUI.midtermsInfoLbl
        preFinal = self.mainUI.preFinalInfoLbl
        final = self.mainUI.finalsInfoLbl
        totalBal = self.mainUI.totalBalanceInfoLbl

        semesterHeader = self.mainUI.semesterHeaderLbl
        semesterYear = self.mainUI.semesterYearLbl

        with open(mainDataJson, 'r') as data:
            studentData = json.load(data)
            yrLvlText = str(studentData[self.userDataIndex]["semesterInfo"][year][semester]["yrLvl"])
            semesterText = str(studentData[self.userDataIndex]["semesterInfo"][year][semester]["semester"])
            totalBalText = self.calculateTotal(self.userDataIndex, year, semester)

            regNo.setText(str(studentData[self.userDataIndex]["semesterInfo"][year][semester]["regNo"]))
            yrLvl.setText(f"{yrLvlText} Year")
            downpayment.setText(str(studentData[self.userDataIndex]["semesterInfo"][year][semester]["downpayment"]).replace("_", ","))
            prelim.setText(str(studentData[self.userDataIndex]["semesterInfo"][year][semester]["prelim"]).replace("_", ","))
            midterm.setText(str(studentData[self.userDataIndex]["semesterInfo"][year][semester]["midterm"]).replace("_", ","))
            preFinal.setText(str(studentData[self.userDataIndex]["semesterInfo"][year][semester]["pre-final"]).replace("_", ","))
            final.setText(str(studentData[self.userDataIndex]["semesterInfo"][year][semester]["final"]).replace("_", ","))
            totalBal.setText(str(totalBalText))
            semesterYear.setText(f"{yrLvlText} Year - BSIT")
            semesterHeader.setText(f"{semesterText} Semester")
            
        

    def calculateTotal(self, userIndex: int, year: str, semester: int):
        # 0 - 1st semester
        # 1 - 2nd semester
        # 2 - 3rd semester
        # 3 - 4th semester

        temp = 0
        with open(mainDataJson, 'r') as data:
                studentData = json.load(data)
                for k, v in studentData[userIndex]["semesterInfo"][year][semester].items():
                    if k == "downpayment":
                        temp += int(v)
                    elif k == "prelim":
                        temp += int(v)
                    elif k == "midterm":
                        temp += int(v)
                    elif k == "pre-final":
                        temp += int(v)
                    elif k == "final":
                        temp += int(v)
        
        return temp
        

    def readData(self, data, table, type):
        index = 0
        if type == "subjects":
            for val in data:
                for k, v in val.items():
                    if k == "code":
                        table.setItem(index, 0, QTableWidgetItem(v))
                    elif k == "subject":
                        table.setItem(index, 1, QTableWidgetItem(v))
                    elif k == "credit":
                        table.setItem(index, 2, QTableWidgetItem(v))
                    elif k == "section":
                        table.setItem(index, 3, QTableWidgetItem(v))
                    elif k == "schedule":
                        table.setItem(index, 4, QTableWidgetItem(v))
                index += 1
        elif type == "grades":
            for val in data:
                for k, v in val.items():
                    if k == "code":
                        table.setItem(index, 0, QTableWidgetItem(v))
                    elif k == "subject":
                        table.setItem(index, 1, QTableWidgetItem(v))
                    elif k == "credit":
                        table.setItem(index, 2, QTableWidgetItem(v))
                    elif k == "midterm":
                        table.setItem(index, 3, QTableWidgetItem(v))
                    elif k == "final":
                        table.setItem(index, 4, QTableWidgetItem(v))
                    elif k == "re-exam":
                        table.setItem(index, 5, QTableWidgetItem(v))
                    elif k == "remarks":                            
                        table.setItem(index, 6, QTableWidgetItem(v))
                index += 1
        
        table.resizeColumnsToContents()

def main():
    app = QApplication(sys.argv)

    window = loginApp()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()