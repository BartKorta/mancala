# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mancalakXEErG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 850)
        MainWindow.setMinimumSize(QSize(700, 850))
        MainWindow.setMaximumSize(QSize(700, 901))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(700, 850))
        self.centralwidget.setMaximumSize(QSize(16777215, 850))
        self.centralwidget.setStyleSheet(u"background-color: rgb(190, 157, 106);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 650, 850))
        self.frame.setMinimumSize(QSize(650, 850))
        self.frame.setMaximumSize(QSize(120, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.mancala = QLabel(self.frame)
        self.mancala.setObjectName(u"mancala")
        self.mancala.setGeometry(QRect(200, -10, 291, 81))
        self.mancala.setStyleSheet(u"font: 36pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(370, 170, 201, 531))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.bt6 = QPushButton(self.frame_3)
        self.bt6.setObjectName(u"bt6")
        self.bt6.setGeometry(QRect(0, 0, 181, 81))
        self.sc6 = QLabel(self.frame_3)
        self.sc6.setObjectName(u"sc6")
        self.sc6.setGeometry(QRect(70, 20, 51, 41))
        self.sc6.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.bt5 = QPushButton(self.frame_4)
        self.bt5.setObjectName(u"bt5")
        self.bt5.setGeometry(QRect(2, 10, 171, 71))
        self.sc5 = QLabel(self.frame_4)
        self.sc5.setObjectName(u"sc5")
        self.sc5.setGeometry(QRect(70, 20, 51, 41))
        self.sc5.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.bt4 = QPushButton(self.frame_5)
        self.bt4.setObjectName(u"bt4")
        self.bt4.setGeometry(QRect(2, 10, 171, 71))
        self.sc4 = QLabel(self.frame_5)
        self.sc4.setObjectName(u"sc4")
        self.sc4.setGeometry(QRect(70, 20, 51, 41))
        self.sc4.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.bt3 = QPushButton(self.frame_6)
        self.bt3.setObjectName(u"bt3")
        self.bt3.setGeometry(QRect(2, 10, 171, 71))
        self.sc3 = QLabel(self.frame_6)
        self.sc3.setObjectName(u"sc3")
        self.sc3.setGeometry(QRect(70, 20, 51, 41))
        self.sc3.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.bt2 = QPushButton(self.frame_7)
        self.bt2.setObjectName(u"bt2")
        self.bt2.setGeometry(QRect(2, 10, 171, 71))
        self.sc2 = QLabel(self.frame_7)
        self.sc2.setObjectName(u"sc2")
        self.sc2.setGeometry(QRect(70, 20, 51, 41))
        self.sc2.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.bt1 = QPushButton(self.frame_8)
        self.bt1.setObjectName(u"bt1")
        self.bt1.setGeometry(QRect(2, 10, 171, 71))
        self.sc1 = QLabel(self.frame_8)
        self.sc1.setObjectName(u"sc1")
        self.sc1.setGeometry(QRect(70, 20, 51, 41))
        self.sc1.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(100, 170, 201, 531))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.sc7 = QLabel(self.frame_10)
        self.sc7.setObjectName(u"sc7")
        self.sc7.setGeometry(QRect(70, 20, 51, 41))
        self.sc7.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.sc8 = QLabel(self.frame_11)
        self.sc8.setObjectName(u"sc8")
        self.sc8.setGeometry(QRect(70, 20, 51, 41))
        self.sc8.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.sc9 = QLabel(self.frame_12)
        self.sc9.setObjectName(u"sc9")
        self.sc9.setGeometry(QRect(70, 20, 51, 41))
        self.sc9.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.sc10 = QLabel(self.frame_13)
        self.sc10.setObjectName(u"sc10")
        self.sc10.setGeometry(QRect(70, 20, 51, 41))
        self.sc10.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.sc11 = QLabel(self.frame_14)
        self.sc11.setObjectName(u"sc11")
        self.sc11.setGeometry(QRect(70, 20, 51, 41))
        self.sc11.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: rgb(203, 181, 149);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.sc12 = QLabel(self.frame_15)
        self.sc12.setObjectName(u"sc12")
        self.sc12.setGeometry(QRect(70, 20, 51, 41))
        self.sc12.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(160, 90, 351, 71))
        self.frame_16.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(233, 220, 211);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.label_y = QLabel(self.frame_16)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setGeometry(QRect(10, 20, 211, 31))
        self.label_y.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(190, 157, 106);")
        self.scYOU = QLabel(self.frame_16)
        self.scYOU.setObjectName(u"scYOU")
        self.scYOU.setGeometry(QRect(260, 20, 61, 31))
        self.scYOU.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(190, 157, 106);")
        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(160, 710, 351, 71))
        self.frame_17.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(233, 220, 211);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_opp = QLabel(self.frame_17)
        self.label_opp.setObjectName(u"label_opp")
        self.label_opp.setGeometry(QRect(20, 20, 211, 31))
        self.label_opp.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(190, 157, 106);")
        self.scOPP = QLabel(self.frame_17)
        self.scOPP.setObjectName(u"scOPP")
        self.scOPP.setGeometry(QRect(260, 20, 61, 31))
        self.scOPP.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(190, 157, 106);")
        self.label_turn = QLabel(self.frame)
        self.label_turn.setObjectName(u"label_turn")
        self.label_turn.setGeometry(QRect(0, 60, 101, 31))
        self.label_turn.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.turn = QLabel(self.frame)
        self.turn.setObjectName(u"turn")
        self.turn.setGeometry(QRect(10, 100, 71, 51))
        self.turn.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.frame_18 = QFrame(self.frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(300, 360, 71, 111))
        self.frame_18.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover {   \n"
"	background-color: rgb(0, 249, 183);\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.next = QPushButton(self.frame_18)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(0, 50, 71, 61))
        self.next.setStyleSheet(u"font: 17pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mancala.setText(QCoreApplication.translate("MainWindow", u"MANCALA", None))
        self.bt6.setText("")
        self.sc6.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.bt5.setText("")
        self.sc5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.bt4.setText("")
        self.sc4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.bt3.setText("")
        self.sc3.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.bt2.setText("")
        self.sc2.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.bt1.setText("")
        self.sc1.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sc7.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sc8.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sc9.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sc10.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sc11.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sc12.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"YOU:", None))
        self.scYOU.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_opp.setText(QCoreApplication.translate("MainWindow", u"OPPONENT:", None))
        self.scOPP.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_turn.setText(QCoreApplication.translate("MainWindow", u"TURN:", None))
        self.turn.setText(QCoreApplication.translate("MainWindow", u"YOU", None))
        self.next.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
    # retranslateUi

