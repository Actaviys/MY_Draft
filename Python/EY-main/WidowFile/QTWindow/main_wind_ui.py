# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\A1\Desktop\Projects\Python\EY-main\WidowFile\QTWindow\main_wind.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 289)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\A1\\Desktop\\Projects\\Python\\EY-main\\WidowFile\\QTWindow\\../../Files/iconey.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 55, 0, 255), stop:1 rgba(0, 39, 0, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ButtonTranslate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonTranslate.setFont(font)
        self.ButtonTranslate.setMouseTracking(True)
        self.ButtonTranslate.setObjectName("ButtonTranslate")
        self.gridLayout.addWidget(self.ButtonTranslate, 4, 1, 1, 1)
        self.ButtonCreatePicture = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonCreatePicture.setFont(font)
        self.ButtonCreatePicture.setMouseTracking(True)
        self.ButtonCreatePicture.setObjectName("ButtonCreatePicture")
        self.gridLayout.addWidget(self.ButtonCreatePicture, 3, 1, 1, 1)
        self.ButtonLMS = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonLMS.setFont(font)
        self.ButtonLMS.setMouseTracking(True)
        self.ButtonLMS.setObjectName("ButtonLMS")
        self.gridLayout.addWidget(self.ButtonLMS, 6, 0, 1, 1)
        self.Button_cmdEY = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.Button_cmdEY.setFont(font)
        self.Button_cmdEY.setMouseTracking(True)
        self.Button_cmdEY.setObjectName("Button_cmdEY")
        self.gridLayout.addWidget(self.Button_cmdEY, 1, 2, 1, 1)
        self.ButtonReadQT = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonReadQT.setFont(font)
        self.ButtonReadQT.setMouseTracking(True)
        self.ButtonReadQT.setObjectName("ButtonReadQT")
        self.gridLayout.addWidget(self.ButtonReadQT, 6, 1, 1, 1)
        self.ButtonTwitch = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonTwitch.setFont(font)
        self.ButtonTwitch.setMouseTracking(True)
        self.ButtonTwitch.setObjectName("ButtonTwitch")
        self.gridLayout.addWidget(self.ButtonTwitch, 6, 2, 1, 1)
        self.ButtonYouTube = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonYouTube.setFont(font)
        self.ButtonYouTube.setMouseTracking(True)
        self.ButtonYouTube.setObjectName("ButtonYouTube")
        self.gridLayout.addWidget(self.ButtonYouTube, 3, 2, 1, 1)
        self.ButtonYouTubeMusic = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonYouTubeMusic.setFont(font)
        self.ButtonYouTubeMusic.setMouseTracking(True)
        self.ButtonYouTubeMusic.setObjectName("ButtonYouTubeMusic")
        self.gridLayout.addWidget(self.ButtonYouTubeMusic, 4, 2, 1, 1)
        self.ButtonTeaching = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonTeaching.setFont(font)
        self.ButtonTeaching.setMouseTracking(True)
        self.ButtonTeaching.setObjectName("ButtonTeaching")
        self.gridLayout.addWidget(self.ButtonTeaching, 3, 0, 1, 1)
        self.ButtonWorkingSession = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonWorkingSession.setFont(font)
        self.ButtonWorkingSession.setMouseTracking(True)
        self.ButtonWorkingSession.setObjectName("ButtonWorkingSession")
        self.gridLayout.addWidget(self.ButtonWorkingSession, 4, 0, 1, 1)
        self.ButtonProject = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonProject.setFont(font)
        self.ButtonProject.setMouseTracking(True)
        self.ButtonProject.setObjectName("ButtonProject")
        self.gridLayout.addWidget(self.ButtonProject, 1, 0, 1, 1)
        self.ButtonChatGPT = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonChatGPT.setFont(font)
        self.ButtonChatGPT.setMouseTracking(True)
        self.ButtonChatGPT.setObjectName("ButtonChatGPT")
        self.gridLayout.addWidget(self.ButtonChatGPT, 1, 1, 1, 1)
        self.ButtonPCoff = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.ButtonPCoff.setFont(font)
        self.ButtonPCoff.setMouseTracking(True)
        self.ButtonPCoff.setObjectName("ButtonPCoff")
        self.gridLayout.addWidget(self.ButtonPCoff, 7, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EY"))
        self.ButtonTranslate.setText(_translate("MainWindow", "Translate # #"))
        self.ButtonCreatePicture.setText(_translate("MainWindow", "Create a picture #"))
        self.ButtonLMS.setText(_translate("MainWindow", "LMS #"))
        self.Button_cmdEY.setText(_translate("MainWindow", "`EY` - cmd #"))
        self.ButtonReadQT.setText(_translate("MainWindow", "Read QT docs #"))
        self.ButtonTwitch.setText(_translate("MainWindow", "Twitch #"))
        self.ButtonYouTube.setText(_translate("MainWindow", "YouYube"))
        self.ButtonYouTubeMusic.setText(_translate("MainWindow", "YouTube Music"))
        self.ButtonTeaching.setText(_translate("MainWindow", "Teaching #"))
        self.ButtonWorkingSession.setText(_translate("MainWindow", "Working session #"))
        self.ButtonProject.setText(_translate("MainWindow", "Project #"))
        self.ButtonChatGPT.setText(_translate("MainWindow", "ChatGPT #"))
        self.ButtonPCoff.setText(_translate("MainWindow", "PC off"))
