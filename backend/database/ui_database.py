# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'databaseyPTfpn.ui'
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

class Ui_Database(object):
    def setupUi(self, Database):
        if Database.objectName():
            Database.setObjectName(u"Database")
        Database.resize(500, 450)
        Database.setMinimumSize(QSize(500, 400))
        Database.setMaximumSize(QSize(500, 450))
        self.verticalLayout = QVBoxLayout(Database)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Database)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 400))
        self.frame.setMaximumSize(QSize(16777215, 450))
        self.frame.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(85, 85, 85);\n"
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
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.dilation_value = QLabel(self.frame_3)
        self.dilation_value.setObjectName(u"dilation_value")
        self.dilation_value.setMinimumSize(QSize(50, 0))
        self.dilation_value.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dilation_value.setFont(font)
        self.dilation_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"}")
        self.dilation_value.setPixmap(QPixmap(u":/icons/asset/database.svg"))
        self.dilation_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.dilation_value)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_minimize = QPushButton(self.frame_3)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(30, 30))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
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
"background-color: rgb(85, 85, 85);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(120, 117, 113);\n"
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
        self.add_program = QLineEdit(self.frame_4)
        self.add_program.setObjectName(u"add_program")
        self.add_program.setGeometry(QRect(20, 120, 441, 51))
        font2 = QFont()
        font2.setPointSize(10)
        self.add_program.setFont(font2)
        self.add_program.setTabletTracking(True)
        self.add_program.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	background-color:rgb(66,66,66);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.add_program.setClearButtonEnabled(True)
        self.btn_add_program = QPushButton(self.frame_4)
        self.btn_add_program.setObjectName(u"btn_add_program")
        self.btn_add_program.setGeometry(QRect(20, 200, 201, 45))
        self.btn_add_program.setMinimumSize(QSize(0, 45))
        self.btn_add_program.setFont(font2)
        self.btn_add_program.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	background-color:rgb(66,66,66);\n"
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
        icon3.addFile(u":/icons/asset/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_program.setIcon(icon3)
        self.btn_add_program.setIconSize(QSize(30, 30))
        self.btn_add_program.setFlat(True)
        self.btn_remove_program = QPushButton(self.frame_4)
        self.btn_remove_program.setObjectName(u"btn_remove_program")
        self.btn_remove_program.setGeometry(QRect(250, 200, 211, 45))
        self.btn_remove_program.setMinimumSize(QSize(0, 45))
        self.btn_remove_program.setFont(font2)
        self.btn_remove_program.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	background-color:rgb(66,66,66);\n"
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
        icon4.addFile(u":/icons/asset/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_program.setIcon(icon4)
        self.btn_remove_program.setIconSize(QSize(30, 30))
        self.btn_remove_program.setFlat(True)
        self.label_notification = QLabel(self.frame_4)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(20, 270, 441, 91))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	background-color:rgb(66,66,66);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.database_tables = QComboBox(self.frame_4)
        self.database_tables.setObjectName(u"database_tables")
        self.database_tables.setGeometry(QRect(20, 50, 291, 45))
        self.database_tables.setMinimumSize(QSize(0, 45))
        self.database_tables.setMaximumSize(QSize(16777215, 38))
        self.database_tables.setFont(font2)
        self.database_tables.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	background-color:rgb(66,66,66);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.database_tables.setFrame(False)
        self.btn_refresh = QPushButton(self.frame_4)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(330, 50, 131, 45))
        self.btn_refresh.setMinimumSize(QSize(0, 45))
        self.btn_refresh.setFont(font2)
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color:rgb(66,66,66);\n"
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
        icon5.addFile(u":/icons/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon5)
        self.btn_refresh.setIconSize(QSize(30, 30))
        self.btn_refresh.setFlat(True)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Database)

        QMetaObject.connectSlotsByName(Database)
    # setupUi

    def retranslateUi(self, Database):
        Database.setWindowTitle(QCoreApplication.translate("Database", u"Dialog", None))
        self.dilation_value.setText("")
        self.label_2.setText(QCoreApplication.translate("Database", u"Tables", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.add_program.setPlaceholderText(QCoreApplication.translate("Database", u"Table name", None))
        self.btn_add_program.setText(QCoreApplication.translate("Database", u"Create", None))
        self.btn_remove_program.setText(QCoreApplication.translate("Database", u"Drop", None))
        self.label_notification.setText(QCoreApplication.translate("Database", u"Notification", None))
        self.btn_refresh.setText(QCoreApplication.translate("Database", u"Refresh", None))
    # retranslateUi

