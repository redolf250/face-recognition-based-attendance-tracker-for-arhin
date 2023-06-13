# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrationfiFOqv.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import asset_rc

class Ui_Registration(object):
    def setupUi(self, Registration):
        if Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(600, 720)
        Registration.setMinimumSize(QSize(600, 700))
        Registration.setMaximumSize(QSize(600, 720))
        self.verticalLayout = QVBoxLayout(Registration)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Registration)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"		background-color: rgb(85, 85, 85);\n"
"	border-radius:5px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setPixmap(QPixmap(u":/icons/asset/user-plus.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(380, 0))
        self.label_2.setMaximumSize(QSize(380, 16777215))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_minimize = QPushButton(self.frame_3)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(30, 30))
        self.btn_minimize.setMaximumSize(QSize(30, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(85, 85, 85);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(120, 117, 113);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/asset/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_3)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(30, 30))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(85, 85, 85);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"background-color: rgb(120, 117, 113);\n"
"	\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon1)
        self.btn_maximize.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(30, 30))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 85, 85);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(255, 0, 0);\n"
"	\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.firstname = QLineEdit(self.frame_4)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(300, 20, 260, 51))
        self.firstname.setMinimumSize(QSize(260, 0))
        self.firstname.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.firstname.setFont(font1)
        self.firstname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.firstname.setClearButtonEnabled(True)
        self.image = QLabel(self.frame_4)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 20, 251, 261))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.image.setFont(font2)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.image.setAlignment(Qt.AlignCenter)
        self.othername = QLineEdit(self.frame_4)
        self.othername.setObjectName(u"othername")
        self.othername.setGeometry(QRect(300, 90, 260, 51))
        self.othername.setMinimumSize(QSize(260, 0))
        self.othername.setMaximumSize(QSize(16777215, 16777215))
        self.othername.setFont(font1)
        self.othername.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.othername.setClearButtonEnabled(True)
        self.lastname = QLineEdit(self.frame_4)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(300, 160, 260, 51))
        self.lastname.setMinimumSize(QSize(260, 0))
        self.lastname.setMaximumSize(QSize(16777215, 16777215))
        self.lastname.setFont(font1)
        self.lastname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.lastname.setClearButtonEnabled(True)
        self.reference = QLineEdit(self.frame_4)
        self.reference.setObjectName(u"reference")
        self.reference.setGeometry(QRect(300, 230, 260, 51))
        self.reference.setMinimumSize(QSize(260, 0))
        self.reference.setMaximumSize(QSize(16777215, 16777215))
        self.reference.setFont(font1)
        self.reference.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reference.setClearButtonEnabled(True)
        self.contact = QLineEdit(self.frame_4)
        self.contact.setObjectName(u"contact")
        self.contact.setGeometry(QRect(359, 300, 201, 51))
        self.contact.setMinimumSize(QSize(180, 0))
        self.contact.setMaximumSize(QSize(16777215, 16777215))
        self.contact.setFont(font1)
        self.contact.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.contact.setClearButtonEnabled(True)
        self.position = QLineEdit(self.frame_4)
        self.position.setObjectName(u"position")
        self.position.setGeometry(QRect(20, 300, 321, 51))
        self.position.setMinimumSize(QSize(260, 0))
        self.position.setMaximumSize(QSize(16777215, 16777215))
        self.position.setFont(font1)
        self.position.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.position.setClearButtonEnabled(True)
        self.filename = QLineEdit(self.frame_4)
        self.filename.setObjectName(u"filename")
        self.filename.setGeometry(QRect(20, 370, 341, 51))
        self.filename.setMinimumSize(QSize(260, 0))
        self.filename.setMaximumSize(QSize(16777215, 16777215))
        self.filename.setFont(font1)
        self.filename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.filename.setClearButtonEnabled(True)
        self.btn_reg_browse = QPushButton(self.frame_4)
        self.btn_reg_browse.setObjectName(u"btn_reg_browse")
        self.btn_reg_browse.setGeometry(QRect(380, 370, 181, 51))
        self.btn_reg_browse.setFont(font1)
        self.btn_reg_browse.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_reg_browse.setIconSize(QSize(30, 30))
        self.btn_reg_browse.setFlat(True)
        self.btn_register = QPushButton(self.frame_4)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(210, 440, 161, 51))
        self.btn_register.setFont(font1)
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/asset/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_register.setIcon(icon3)
        self.btn_register.setIconSize(QSize(30, 30))
        self.btn_register.setFlat(True)
        self.btn_delete = QPushButton(self.frame_4)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(400, 440, 161, 51))
        self.btn_delete.setFont(font1)
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/asset/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon4)
        self.btn_delete.setIconSize(QSize(30, 30))
        self.btn_delete.setFlat(True)
        self.label_notification = QLabel(self.frame_4)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(20, 520, 541, 111))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.btn_search = QPushButton(self.frame_4)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(20, 440, 161, 51))
        self.btn_search.setFont(font1)
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon5)
        self.btn_search.setIconSize(QSize(30, 30))
        self.btn_search.setFlat(True)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Registration", u"Registration", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.firstname.setPlaceholderText(QCoreApplication.translate("Registration", u"Firstname", None))
        self.image.setText("")
        self.othername.setPlaceholderText(QCoreApplication.translate("Registration", u"Othername", None))
        self.lastname.setPlaceholderText(QCoreApplication.translate("Registration", u"Lastname", None))
        self.reference.setPlaceholderText(QCoreApplication.translate("Registration", u"Reference", None))
        self.contact.setPlaceholderText(QCoreApplication.translate("Registration", u"Contact", None))
        self.position.setPlaceholderText(QCoreApplication.translate("Registration", u"Position", None))
        self.filename.setPlaceholderText(QCoreApplication.translate("Registration", u"Filename", None))
        self.btn_reg_browse.setText(QCoreApplication.translate("Registration", u"Browse Images", None))
        self.btn_register.setText(QCoreApplication.translate("Registration", u"Register", None))
        self.btn_delete.setText(QCoreApplication.translate("Registration", u"Delete", None))
        self.label_notification.setText(QCoreApplication.translate("Registration", u"Notification", None))
        self.btn_search.setText(QCoreApplication.translate("Registration", u"Search", None))
    # retranslateUi

