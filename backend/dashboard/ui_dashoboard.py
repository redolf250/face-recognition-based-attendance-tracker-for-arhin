# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashoboardfnXBBq.ui'
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
import asset_rc
import asset_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1500, 1000)
        dashboard.setMinimumSize(QSize(1500, 1000))
        dashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1500, 1000))
        self.centralwidget.setStyleSheet(u"")
        self.drop_shadow_layout = QFrame(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setGeometry(QRect(0, 0, 1521, 1000))
        self.drop_shadow_layout.setMinimumSize(QSize(1280, 1000))
        self.drop_shadow_layout.setStyleSheet(u"	background-color: rgb(85, 85, 85);")
        self.drop_shadow_layout.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_layout.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout.setLineWidth(0)
        self.content_layout = QVBoxLayout(self.drop_shadow_layout)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 20, 0)
        self.title_bar = QFrame(self.drop_shadow_layout)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 50))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 0, 4, 0)
        self.other_fields = QFrame(self.title_bar)
        self.other_fields.setObjectName(u"other_fields")
        self.other_fields.setFrameShape(QFrame.NoFrame)
        self.other_fields.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.other_fields)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.options = QFrame(self.other_fields)
        self.options.setObjectName(u"options")
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_19 = QHBoxLayout(self.options)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(5, -1, 5, 3)
        self.label_2 = QLabel(self.options)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(110, 16777215))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.label_2.setMargin(10)

        self.horizontalLayout_19.addWidget(self.label_2)

        self.btn_home = QPushButton(self.options)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMaximumSize(QSize(100, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_home.setFont(font1)
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_home.setIconSize(QSize(30, 30))
        self.btn_home.setFlat(True)

        self.horizontalLayout_19.addWidget(self.btn_home)

        self.btn_search = QPushButton(self.options)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMaximumSize(QSize(100, 40))
        self.btn_search.setFont(font1)
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_search.setIconSize(QSize(30, 30))
        self.btn_search.setFlat(True)

        self.horizontalLayout_19.addWidget(self.btn_search)

        self.btn_register = QPushButton(self.options)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMaximumSize(QSize(100, 40))
        self.btn_register.setFont(font1)
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_register.setIconSize(QSize(30, 30))
        self.btn_register.setFlat(True)

        self.horizontalLayout_19.addWidget(self.btn_register)

        self.btn_batch_job = QPushButton(self.options)
        self.btn_batch_job.setObjectName(u"btn_batch_job")
        self.btn_batch_job.setMaximumSize(QSize(100, 40))
        self.btn_batch_job.setFont(font1)
        self.btn_batch_job.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_batch_job.setIconSize(QSize(30, 30))
        self.btn_batch_job.setFlat(True)

        self.horizontalLayout_19.addWidget(self.btn_batch_job)

        self.btn_summary = QPushButton(self.options)
        self.btn_summary.setObjectName(u"btn_summary")
        self.btn_summary.setMaximumSize(QSize(100, 40))
        self.btn_summary.setFont(font1)
        self.btn_summary.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_summary.setFlat(True)

        self.horizontalLayout_19.addWidget(self.btn_summary)

        self.btn_send_mail = QPushButton(self.options)
        self.btn_send_mail.setObjectName(u"btn_send_mail")
        self.btn_send_mail.setMaximumSize(QSize(100, 40))
        self.btn_send_mail.setFont(font1)
        self.btn_send_mail.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_send_mail.setFlat(True)

        self.horizontalLayout_19.addWidget(self.btn_send_mail)

        self.label_4 = QLabel(self.options)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")

        self.horizontalLayout_19.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.options)


        self.horizontalLayout.addWidget(self.other_fields)

        self.controls_frame = QFrame(self.title_bar)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMinimumSize(QSize(150, 0))
        self.controls_frame.setMaximumSize(QSize(80, 16777215))
        self.controls_frame.setFrameShape(QFrame.NoFrame)
        self.controls_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.controls_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, -1, 6, 17)
        self.btn_minimize = QPushButton(self.controls_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(30, 30))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_6.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.controls_frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(30, 30))
        self.btn_maximize.setMaximumSize(QSize(30, 30))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"background-color: rgb(120, 117, 113);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon1)
        self.btn_maximize.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.controls_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(30, 30))
        self.btn_close.setMaximumSize(QSize(30, 30))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_6.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.controls_frame)


        self.content_layout.addWidget(self.title_bar)

        self.content = QFrame(self.drop_shadow_layout)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(75, 75, 75);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.content)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(40, 0))
        self.menu_frame.setMaximumSize(QSize(40, 16777215))
        self.menu_frame.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 3)
        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 550))
        self.frame.setMaximumSize(QSize(16777215, 500))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)

        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.menu_frame)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMaximumSize(QSize(1451, 950))
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.content_frame)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))
        self.stackedWidget.setMaximumSize(QSize(1442, 950))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.home)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.home)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(500, 0))
        self.left_frame.setMaximumSize(QSize(400, 16777215))
        self.left_frame.setStyleSheet(u"")
        self.left_frame.setFrameShape(QFrame.NoFrame)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.left_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.info_frame = QFrame(self.left_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 410))
        self.info_frame.setMaximumSize(QSize(16777215, 430))
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.info_frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 30, 261, 281))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.image.setFont(font3)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.image.setAlignment(Qt.AlignCenter)
        self.firstname = QLabel(self.info_frame)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(290, 90, 191, 45))
        self.firstname.setMinimumSize(QSize(0, 45))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.firstname.setFont(font4)
        self.firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.othername = QLabel(self.info_frame)
        self.othername.setObjectName(u"othername")
        self.othername.setGeometry(QRect(290, 150, 191, 45))
        self.othername.setMinimumSize(QSize(0, 45))
        self.othername.setFont(font4)
        self.othername.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.othername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lastname = QLabel(self.info_frame)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(290, 210, 191, 45))
        self.lastname.setMinimumSize(QSize(0, 45))
        self.lastname.setFont(font4)
        self.lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.reference = QLabel(self.info_frame)
        self.reference.setObjectName(u"reference")
        self.reference.setGeometry(QRect(290, 30, 191, 45))
        self.reference.setMinimumSize(QSize(45, 45))
        self.reference.setFont(font4)
        self.reference.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.reference.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.contact = QLabel(self.info_frame)
        self.contact.setObjectName(u"contact")
        self.contact.setGeometry(QRect(290, 270, 191, 45))
        self.contact.setMinimumSize(QSize(0, 45))
        self.contact.setFont(font4)
        self.contact.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.contact.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.position = QLabel(self.info_frame)
        self.position.setObjectName(u"position")
        self.position.setGeometry(QRect(20, 330, 261, 45))
        self.position.setMinimumSize(QSize(0, 45))
        self.position.setFont(font4)
        self.position.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.position.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_2 = QLabel(self.info_frame)
        self.image_2.setObjectName(u"image_2")
        self.image_2.setGeometry(QRect(10, 10, 481, 391))
        self.image_2.setFont(font3)
        self.image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"}")
        self.image_2.setAlignment(Qt.AlignCenter)
        self.status = QLabel(self.info_frame)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(290, 330, 191, 45))
        self.status.setMinimumSize(QSize(0, 45))
        self.status.setFont(font4)
        self.status.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_2.raise_()
        self.image.raise_()
        self.firstname.raise_()
        self.othername.raise_()
        self.lastname.raise_()
        self.reference.raise_()
        self.contact.raise_()
        self.position.raise_()
        self.status.raise_()

        self.verticalLayout_6.addWidget(self.info_frame)

        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 530))
        self.frame_3.setMaximumSize(QSize(16777215, 530))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_notification = QLabel(self.frame_3)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(10, 430, 481, 91))
        self.label_notification.setFont(font4)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.firstname_25 = QLabel(self.frame_3)
        self.firstname_25.setObjectName(u"firstname_25")
        self.firstname_25.setGeometry(QRect(10, 150, 481, 111))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.firstname_25.setFont(font5)
        self.firstname_25.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:10px;\n"
"}")
        self.firstname_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.database_tables = QComboBox(self.frame_3)
        self.database_tables.setObjectName(u"database_tables")
        self.database_tables.setGeometry(QRect(20, 200, 291, 45))
        self.database_tables.setMinimumSize(QSize(0, 45))
        self.database_tables.setMaximumSize(QSize(16777215, 38))
        self.database_tables.setFont(font1)
        self.database_tables.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(66, 66, 66);\n"
"	padding-left:10px;\n"
"   background-color: rgb(66, 66, 66);\n"
"border: 2px solid  rgb(66, 66, 66);\n"
"	border-radius: 5px;\n"
"}")
        self.database_tables.setFrame(False)
        self.btn_refresh = QPushButton(self.frame_3)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(330, 200, 151, 45))
        self.btn_refresh.setMinimumSize(QSize(0, 45))
        self.btn_refresh.setFont(font1)
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 background-color: rgb(66, 66, 66);\n"
"     border: 2px solid  rgb(66, 66, 66);\n"
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
        icon3.addFile(u":/icons/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon3)
        self.btn_refresh.setIconSize(QSize(30, 30))
        self.btn_refresh.setFlat(True)
        self.firstname_26 = QLabel(self.frame_3)
        self.firstname_26.setObjectName(u"firstname_26")
        self.firstname_26.setGeometry(QRect(10, 10, 481, 111))
        self.firstname_26.setFont(font5)
        self.firstname_26.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.status_2 = QLabel(self.frame_3)
        self.status_2.setObjectName(u"status_2")
        self.status_2.setGeometry(QRect(10, 20, 111, 21))
        self.status_2.setFont(font4)
        self.status_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:5px;\n"
"\n"
"}")
        self.status_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.late_hour = QSpinBox(self.frame_3)
        self.late_hour.setObjectName(u"late_hour")
        self.late_hour.setGeometry(QRect(110, 60, 51, 41))
        font6 = QFont()
        font6.setPointSize(14)
        self.late_hour.setFont(font6)
        self.late_hour.setStyleSheet(u"QSpinBox{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 66, 66);\n"
"border:none;\n"
"}\n"
"")
        self.late_hour.setReadOnly(False)
        self.late_hour.setMaximum(12)
        self.late_hour.setValue(8)
        self.late_minutes = QSpinBox(self.frame_3)
        self.late_minutes.setObjectName(u"late_minutes")
        self.late_minutes.setGeometry(QRect(330, 60, 61, 41))
        self.late_minutes.setFont(font6)
        self.late_minutes.setStyleSheet(u"QSpinBox{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 66, 66);\n"
"border:none;\n"
"}\n"
"")
        self.late_minutes.setReadOnly(False)
        self.late_minutes.setMaximum(59)
        self.late_minutes.setValue(30)
        self.contact_2 = QLabel(self.frame_3)
        self.contact_2.setObjectName(u"contact_2")
        self.contact_2.setGeometry(QRect(20, 60, 81, 41))
        self.contact_2.setFont(font4)
        self.contact_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 5px;\n"
"	padding-left:1px;\n"
"\n"
"}")
        self.contact_2.setAlignment(Qt.AlignCenter)
        self.contact_3 = QLabel(self.frame_3)
        self.contact_3.setObjectName(u"contact_3")
        self.contact_3.setGeometry(QRect(230, 60, 91, 41))
        self.contact_3.setFont(font4)
        self.contact_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 5px;\n"
"	padding-left:1px;\n"
"\n"
"}")
        self.contact_3.setAlignment(Qt.AlignCenter)
        self.contact_4 = QLabel(self.frame_3)
        self.contact_4.setObjectName(u"contact_4")
        self.contact_4.setGeometry(QRect(180, 60, 31, 41))
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.contact_4.setFont(font7)
        self.contact_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 5px;\n"
"	padding-left:1px;\n"
"\n"
"}")
        self.contact_4.setAlignment(Qt.AlignCenter)
        self.read_only_property = QRadioButton(self.frame_3)
        self.read_only_property.setObjectName(u"read_only_property")
        self.read_only_property.setGeometry(QRect(310, 20, 171, 20))
        self.read_only_property.setFont(font1)
        self.read_only_property.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 85);")
        self.read_only_property.setChecked(True)
        self.time_zone = QComboBox(self.frame_3)
        self.time_zone.addItem("")
        self.time_zone.addItem("")
        self.time_zone.setObjectName(u"time_zone")
        self.time_zone.setGeometry(QRect(410, 60, 71, 41))
        self.time_zone.setMinimumSize(QSize(0, 41))
        self.time_zone.setMaximumSize(QSize(16777215, 41))
        self.time_zone.setFont(font1)
        self.time_zone.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 66, 66);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.time_zone.setFrame(False)
        self.firstname_27 = QLabel(self.frame_3)
        self.firstname_27.setObjectName(u"firstname_27")
        self.firstname_27.setGeometry(QRect(10, 290, 481, 111))
        self.firstname_27.setFont(font5)
        self.firstname_27.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:10px;\n"
"}")
        self.firstname_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_clear_label = QPushButton(self.frame_3)
        self.btn_clear_label.setObjectName(u"btn_clear_label")
        self.btn_clear_label.setGeometry(QRect(260, 340, 221, 45))
        self.btn_clear_label.setMinimumSize(QSize(0, 45))
        self.btn_clear_label.setFont(font1)
        self.btn_clear_label.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        icon4.addFile(u":/icons/asset/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_label.setIcon(icon4)
        self.btn_clear_label.setIconSize(QSize(30, 30))
        self.btn_clear_label.setFlat(True)
        self.btn_open_database = QPushButton(self.frame_3)
        self.btn_open_database.setObjectName(u"btn_open_database")
        self.btn_open_database.setGeometry(QRect(20, 340, 221, 45))
        self.btn_open_database.setMinimumSize(QSize(0, 45))
        self.btn_open_database.setFont(font1)
        self.btn_open_database.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        icon5.addFile(u":/icons/asset/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_database.setIcon(icon5)
        self.btn_open_database.setIconSize(QSize(30, 30))
        self.btn_open_database.setFlat(True)

        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.left_frame)

        self.right_frame = QFrame(self.home)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(0, 700))
        self.right_frame.setFrameShape(QFrame.NoFrame)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.right_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 5, 0)
        self.camera_frame = QFrame(self.right_frame)
        self.camera_frame.setObjectName(u"camera_frame")
        self.camera_frame.setMinimumSize(QSize(0, 700))
        self.camera_frame.setMaximumSize(QSize(16777215, 700))
        self.camera_frame.setFrameShape(QFrame.NoFrame)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.camera_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.camera_view = QLabel(self.camera_frame)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setMinimumSize(QSize(0, 680))
        self.camera_view.setMaximumSize(QSize(16777215, 680))
        self.camera_view.setFont(font3)
        self.camera_view.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"}")
        self.camera_view.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_view.setAlignment(Qt.AlignCenter)
        self.camera_view.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.camera_view)


        self.verticalLayout_7.addWidget(self.camera_frame)

        self.properties_frame = QFrame(self.right_frame)
        self.properties_frame.setObjectName(u"properties_frame")
        self.properties_frame.setFrameShape(QFrame.NoFrame)
        self.properties_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.properties_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.properties_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(450, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(140, 20, 146, 20))
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(10)
        self.label_14.setFont(font8)
        self.label_14.setStyleSheet(u"")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(350, 80, 81, 51))
        self.comboBox.setMinimumSize(QSize(0, 51))
        self.comboBox.setMaximumSize(QSize(16777215, 38))
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.comboBox.setFrame(False)
        self.btn_connect_detect = QPushButton(self.frame_4)
        self.btn_connect_detect.setObjectName(u"btn_connect_detect")
        self.btn_connect_detect.setGeometry(QRect(20, 160, 191, 51))
        self.btn_connect_detect.setMinimumSize(QSize(0, 51))
        self.btn_connect_detect.setMaximumSize(QSize(16777215, 40))
        self.btn_connect_detect.setFont(font1)
        self.btn_connect_detect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_connect_detect.setIcon(icon6)
        self.btn_connect_detect.setIconSize(QSize(30, 30))
        self.btn_connect_detect.setFlat(True)
        self.btn_disconnect = QPushButton(self.frame_4)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setGeometry(QRect(240, 160, 191, 51))
        self.btn_disconnect.setMinimumSize(QSize(0, 51))
        self.btn_disconnect.setFont(font1)
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_disconnect.setIcon(icon7)
        self.btn_disconnect.setIconSize(QSize(30, 30))
        self.btn_disconnect.setFlat(True)
        self.camera_ip = QLineEdit(self.frame_4)
        self.camera_ip.setObjectName(u"camera_ip")
        self.camera_ip.setGeometry(QRect(20, 80, 321, 51))
        self.camera_ip.setFont(font1)
        self.camera_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"background-color: rgb(66, 66, 66);\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid  rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_ip.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 20, 150, 20))
        self.label_18.setMinimumSize(QSize(0, 20))
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.scan_range_label = QLabel(self.frame_5)
        self.scan_range_label.setObjectName(u"scan_range_label")
        self.scan_range_label.setGeometry(QRect(20, 160, 421, 51))
        self.scan_range_label.setFont(font4)
        self.scan_range_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:45px;\n"
"\n"
"}")
        self.scan_range_label.setAlignment(Qt.AlignCenter)
        self.label_42 = QLabel(self.frame_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 170, 31, 31))
        self.label_42.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.label_42.setPixmap(QPixmap(u":/icons/asset/camera.svg"))
        self.btn_scan_range = QPushButton(self.frame_5)
        self.btn_scan_range.setObjectName(u"btn_scan_range")
        self.btn_scan_range.setGeometry(QRect(300, 80, 141, 51))
        self.btn_scan_range.setFont(font1)
        self.btn_scan_range.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_scan_range.setIcon(icon8)
        self.btn_scan_range.setIconSize(QSize(30, 30))
        self.btn_scan_range.setFlat(True)
        self.scan_range = QLineEdit(self.frame_5)
        self.scan_range.setObjectName(u"scan_range")
        self.scan_range.setGeometry(QRect(20, 80, 271, 51))
        self.scan_range.setFont(font1)
        self.scan_range.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        self.scan_range.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_7.addWidget(self.properties_frame)


        self.horizontalLayout_4.addWidget(self.right_frame)

        self.stackedWidget.addWidget(self.home)
        self.batch = QWidget()
        self.batch.setObjectName(u"batch")
        self.verticalLayout_13 = QVBoxLayout(self.batch)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 9, 0)
        self.frame_9 = QFrame(self.batch)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 110))
        self.frame_9.setMaximumSize(QSize(1433, 100))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_32 = QLabel(self.frame_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 10, 1071, 91))
        font9 = QFont()
        font9.setFamily(u"Arial")
        font9.setPointSize(11)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_32.setFont(font9)
        self.label_32.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.batch_notification = QLabel(self.frame_9)
        self.batch_notification.setObjectName(u"batch_notification")
        self.batch_notification.setGeometry(QRect(1100, 10, 331, 91))
        self.batch_notification.setFont(font4)
        self.batch_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.batch_notification.setAlignment(Qt.AlignCenter)
        self.batch_notification.setWordWrap(True)
        self.btn_batch_browse = QPushButton(self.frame_9)
        self.btn_batch_browse.setObjectName(u"btn_batch_browse")
        self.btn_batch_browse.setGeometry(QRect(760, 30, 141, 51))
        self.btn_batch_browse.setFont(font1)
        self.btn_batch_browse.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/asset/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_batch_browse.setIcon(icon9)
        self.btn_batch_browse.setIconSize(QSize(30, 30))
        self.btn_batch_browse.setFlat(True)
        self.batch_filename = QLineEdit(self.frame_9)
        self.batch_filename.setObjectName(u"batch_filename")
        self.batch_filename.setGeometry(QRect(310, 30, 431, 51))
        self.batch_filename.setFont(font1)
        self.batch_filename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid  rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.batch_filename.setClearButtonEnabled(True)
        self.btn_start_job = QPushButton(self.frame_9)
        self.btn_start_job.setObjectName(u"btn_start_job")
        self.btn_start_job.setGeometry(QRect(920, 30, 141, 51))
        self.btn_start_job.setFont(font1)
        self.btn_start_job.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        icon10 = QIcon()
        icon10.addFile(u":/icons/asset/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start_job.setIcon(icon10)
        self.btn_start_job.setIconSize(QSize(30, 30))
        self.btn_start_job.setFlat(True)
        self.batch_table = QComboBox(self.frame_9)
        self.batch_table.setObjectName(u"batch_table")
        self.batch_table.setGeometry(QRect(30, 30, 261, 51))
        self.batch_table.setMinimumSize(QSize(0, 51))
        self.batch_table.setMaximumSize(QSize(16777215, 38))
        self.batch_table.setFont(font1)
        self.batch_table.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.batch_table.setFrame(False)

        self.verticalLayout_13.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.batch)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 0, 0, 9)
        self.batch_tableWidget = QTableWidget(self.frame_10)
        if (self.batch_tableWidget.columnCount() < 7):
            self.batch_tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.batch_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.batch_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font10 = QFont()
        font10.setPointSize(10)
        font10.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font10);
        self.batch_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.batch_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.batch_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.batch_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.batch_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.batch_tableWidget.setObjectName(u"batch_tableWidget")
        font11 = QFont()
        font11.setPointSize(11)
        self.batch_tableWidget.setFont(font11)
        self.batch_tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(66, 66, 66);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.batch_tableWidget.setFrameShape(QFrame.NoFrame)
        self.batch_tableWidget.setFrameShadow(QFrame.Plain)
        self.batch_tableWidget.setSortingEnabled(True)
        self.batch_tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.batch_tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.batch_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.batch_tableWidget)


        self.verticalLayout_13.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.batch)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.horizontalLayout_5 = QHBoxLayout(self.search)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_frame_2 = QFrame(self.search)
        self.left_frame_2.setObjectName(u"left_frame_2")
        self.left_frame_2.setMinimumSize(QSize(500, 0))
        self.left_frame_2.setMaximumSize(QSize(500, 16777215))
        self.left_frame_2.setFrameShape(QFrame.NoFrame)
        self.left_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.left_frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.left_frame_2)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 500))
        self.top.setMaximumSize(QSize(500, 500))
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.db_image_data = QLabel(self.top)
        self.db_image_data.setObjectName(u"db_image_data")
        self.db_image_data.setGeometry(QRect(20, 130, 261, 281))
        self.db_image_data.setFont(font3)
        self.db_image_data.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"}")
        self.db_image_data.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.db_image_data.setAlignment(Qt.AlignCenter)
        self.db_lastname = QLabel(self.top)
        self.db_lastname.setObjectName(u"db_lastname")
        self.db_lastname.setGeometry(QRect(290, 310, 191, 41))
        self.db_lastname.setFont(font4)
        self.db_lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_middlename = QLabel(self.top)
        self.db_middlename.setObjectName(u"db_middlename")
        self.db_middlename.setGeometry(QRect(290, 250, 191, 41))
        self.db_middlename.setFont(font4)
        self.db_middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_firstname = QLabel(self.top)
        self.db_firstname.setObjectName(u"db_firstname")
        self.db_firstname.setGeometry(QRect(290, 190, 191, 41))
        self.db_firstname.setFont(font4)
        self.db_firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_contact = QLabel(self.top)
        self.db_contact.setObjectName(u"db_contact")
        self.db_contact.setGeometry(QRect(290, 370, 191, 41))
        self.db_contact.setFont(font4)
        self.db_contact.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_contact.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_incharge = QLabel(self.top)
        self.db_incharge.setObjectName(u"db_incharge")
        self.db_incharge.setGeometry(QRect(20, 430, 261, 41))
        self.db_incharge.setFont(font4)
        self.db_incharge.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_incharge.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_incharge.setWordWrap(True)
        self.search_box = QLineEdit(self.top)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(20, 30, 321, 41))
        self.search_box.setFont(font1)
        self.search_box.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid  rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.search_box.setClearButtonEnabled(True)
        self.btn_search_page = QPushButton(self.top)
        self.btn_search_page.setObjectName(u"btn_search_page")
        self.btn_search_page.setGeometry(QRect(350, 30, 131, 41))
        self.btn_search_page.setFont(font1)
        self.btn_search_page.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
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
        self.btn_search_page.setIcon(icon8)
        self.btn_search_page.setIconSize(QSize(30, 30))
        self.btn_search_page.setFlat(True)
        self.label_29 = QLabel(self.top)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 10, 481, 81))
        self.label_29.setFont(font9)
        self.label_29.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_3 = QLabel(self.top)
        self.image_3.setObjectName(u"image_3")
        self.image_3.setGeometry(QRect(10, 110, 481, 381))
        self.image_3.setFont(font3)
        self.image_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"}")
        self.image_3.setAlignment(Qt.AlignCenter)
        self.db_status = QLabel(self.top)
        self.db_status.setObjectName(u"db_status")
        self.db_status.setGeometry(QRect(290, 430, 191, 41))
        self.db_status.setFont(font4)
        self.db_status.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_status.setWordWrap(True)
        self.db_refrence = QLabel(self.top)
        self.db_refrence.setObjectName(u"db_refrence")
        self.db_refrence.setGeometry(QRect(290, 130, 191, 41))
        self.db_refrence.setFont(font4)
        self.db_refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_3.raise_()
        self.label_29.raise_()
        self.db_image_data.raise_()
        self.db_lastname.raise_()
        self.db_middlename.raise_()
        self.db_firstname.raise_()
        self.db_contact.raise_()
        self.db_incharge.raise_()
        self.search_box.raise_()
        self.btn_search_page.raise_()
        self.db_status.raise_()
        self.db_refrence.raise_()

        self.verticalLayout_9.addWidget(self.top)

        self.bottom = QFrame(self.left_frame_2)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 450))
        self.bottom.setMaximumSize(QSize(16777215, 450))
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.frame_6 = QFrame(self.bottom)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(20, 190, 461, 240))
        self.frame_6.setMinimumSize(QSize(0, 240))
        self.frame_6.setMaximumSize(QSize(16777215, 240))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.calendarWidget = QCalendarWidget(self.frame_6)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)

        self.verticalLayout_12.addWidget(self.calendarWidget)

        self.db_start_date = QLineEdit(self.bottom)
        self.db_start_date.setObjectName(u"db_start_date")
        self.db_start_date.setGeometry(QRect(20, 130, 171, 51))
        self.db_start_date.setFont(font1)
        self.db_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid   rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.db_start_date.setInputMethodHints(Qt.ImhPreferNumbers)
        self.db_start_date.setClearButtonEnabled(True)
        self.label_25 = QLabel(self.bottom)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 140, 31, 31))
        self.label_25.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.label_25.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_30 = QLabel(self.bottom)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 110, 481, 331))
        self.label_30.setMinimumSize(QSize(0, 300))
        self.label_30.setFont(font9)
        self.label_30.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_csv = QPushButton(self.bottom)
        self.btn_csv.setObjectName(u"btn_csv")
        self.btn_csv.setGeometry(QRect(20, 30, 131, 41))
        self.btn_csv.setFont(font1)
        self.btn_csv.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
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
        self.btn_csv.setIcon(icon9)
        self.btn_csv.setIconSize(QSize(30, 30))
        self.btn_csv.setFlat(True)
        self.label_40 = QLabel(self.bottom)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 10, 481, 81))
        self.label_40.setFont(font9)
        self.label_40.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.filename = QLineEdit(self.bottom)
        self.filename.setObjectName(u"filename")
        self.filename.setGeometry(QRect(200, 130, 281, 51))
        self.filename.setFont(font1)
        self.filename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid   rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.filename.setInputMethodHints(Qt.ImhPreferNumbers)
        self.filename.setClearButtonEnabled(True)
        self.btn_backup = QPushButton(self.bottom)
        self.btn_backup.setObjectName(u"btn_backup")
        self.btn_backup.setGeometry(QRect(350, 30, 131, 41))
        self.btn_backup.setFont(font1)
        self.btn_backup.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"		background-color: rgb(66, 66, 66);\n"
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
        self.btn_backup.setIcon(icon5)
        self.btn_backup.setIconSize(QSize(30, 30))
        self.btn_backup.setFlat(True)
        self.search_page_tables = QComboBox(self.bottom)
        self.search_page_tables.setObjectName(u"search_page_tables")
        self.search_page_tables.setGeometry(QRect(160, 30, 181, 40))
        self.search_page_tables.setMinimumSize(QSize(0, 40))
        self.search_page_tables.setMaximumSize(QSize(16777215, 38))
        self.search_page_tables.setFont(font1)
        self.search_page_tables.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.search_page_tables.setFrame(False)
        self.label_40.raise_()
        self.label_30.raise_()
        self.frame_6.raise_()
        self.db_start_date.raise_()
        self.label_25.raise_()
        self.btn_csv.raise_()
        self.filename.raise_()
        self.btn_backup.raise_()
        self.search_page_tables.raise_()

        self.verticalLayout_9.addWidget(self.bottom)


        self.horizontalLayout_5.addWidget(self.left_frame_2)

        self.rigth_frame = QFrame(self.search)
        self.rigth_frame.setObjectName(u"rigth_frame")
        self.rigth_frame.setStyleSheet(u"")
        self.rigth_frame.setFrameShape(QFrame.NoFrame)
        self.rigth_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.rigth_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, 9, 12)
        self.tableWidget = QTableWidget(self.rigth_frame)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        __qtablewidgetitem7.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font11)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"		background-color: rgb(66, 66, 66);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.tableWidget)


        self.horizontalLayout_5.addWidget(self.rigth_frame)

        self.stackedWidget.addWidget(self.search)
        self.summary = QWidget()
        self.summary.setObjectName(u"summary")
        self.summary.setMaximumSize(QSize(1442, 950))
        self.verticalLayout_4 = QVBoxLayout(self.summary)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.summary)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(0, 0, 1421, 91))
        self.label_31.setFont(font9)
        self.label_31.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.summary_filename = QLineEdit(self.frame_7)
        self.summary_filename.setObjectName(u"summary_filename")
        self.summary_filename.setGeometry(QRect(470, 20, 261, 51))
        self.summary_filename.setFont(font1)
        self.summary_filename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        self.summary_filename.setClearButtonEnabled(True)
        self.btn_summary_save = QPushButton(self.frame_7)
        self.btn_summary_save.setObjectName(u"btn_summary_save")
        self.btn_summary_save.setGeometry(QRect(740, 20, 141, 51))
        self.btn_summary_save.setFont(font1)
        self.btn_summary_save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        icon11 = QIcon()
        icon11.addFile(u":/icons/asset/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_summary_save.setIcon(icon11)
        self.btn_summary_save.setIconSize(QSize(30, 30))
        self.btn_summary_save.setFlat(True)
        self.database_summary = QComboBox(self.frame_7)
        self.database_summary.setObjectName(u"database_summary")
        self.database_summary.setGeometry(QRect(20, 20, 281, 51))
        self.database_summary.setMinimumSize(QSize(0, 51))
        self.database_summary.setMaximumSize(QSize(16777215, 38))
        self.database_summary.setFont(font1)
        self.database_summary.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.database_summary.setFrame(False)
        self.btn_summary_load = QPushButton(self.frame_7)
        self.btn_summary_load.setObjectName(u"btn_summary_load")
        self.btn_summary_load.setGeometry(QRect(310, 20, 141, 51))
        self.btn_summary_load.setFont(font1)
        self.btn_summary_load.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        icon12 = QIcon()
        icon12.addFile(u":/icons/asset/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_summary_load.setIcon(icon12)
        self.btn_summary_load.setIconSize(QSize(30, 30))
        self.btn_summary_load.setFlat(True)
        self.summary_browse = QLineEdit(self.frame_7)
        self.summary_browse.setObjectName(u"summary_browse")
        self.summary_browse.setGeometry(QRect(910, 20, 341, 51))
        self.summary_browse.setFont(font1)
        self.summary_browse.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid  rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.summary_browse.setClearButtonEnabled(True)
        self.btn_summary_browse = QPushButton(self.frame_7)
        self.btn_summary_browse.setObjectName(u"btn_summary_browse")
        self.btn_summary_browse.setGeometry(QRect(1270, 20, 141, 51))
        self.btn_summary_browse.setFont(font1)
        self.btn_summary_browse.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
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
        self.btn_summary_browse.setIcon(icon9)
        self.btn_summary_browse.setIconSize(QSize(30, 30))
        self.btn_summary_browse.setFlat(True)

        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.summary)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_summary = QTableWidget(self.frame_8)
        if (self.tableWidget_summary.columnCount() < 9):
            self.tableWidget_summary.setColumnCount(9)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.tableWidget_summary.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font1);
        self.tableWidget_summary.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font1);
        self.tableWidget_summary.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font1);
        self.tableWidget_summary.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font1);
        self.tableWidget_summary.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font1);
        self.tableWidget_summary.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font1);
        self.tableWidget_summary.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font1);
        self.tableWidget_summary.setHorizontalHeaderItem(7, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font1);
        self.tableWidget_summary.setHorizontalHeaderItem(8, __qtablewidgetitem22)
        self.tableWidget_summary.setObjectName(u"tableWidget_summary")
        self.tableWidget_summary.setFont(font11)
        self.tableWidget_summary.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(66, 66, 66);;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget_summary.setFrameShape(QFrame.NoFrame)
        self.tableWidget_summary.setFrameShadow(QFrame.Plain)
        self.tableWidget_summary.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_summary.setSortingEnabled(True)
        self.tableWidget_summary.horizontalHeader().setDefaultSectionSize(155)
        self.tableWidget_summary.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_summary.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_summary.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_summary.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_10.addWidget(self.tableWidget_summary)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.summary)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.content_frame)


        self.content_layout.addWidget(self.content)

        dashboard.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(dashboard)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("dashboard", u"weTrack", None))
        self.btn_home.setText(QCoreApplication.translate("dashboard", u"Home", None))
        self.btn_search.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.btn_register.setText(QCoreApplication.translate("dashboard", u"Register", None))
        self.btn_batch_job.setText(QCoreApplication.translate("dashboard", u"Batch", None))
        self.btn_summary.setText(QCoreApplication.translate("dashboard", u"Summary", None))
        self.btn_send_mail.setText(QCoreApplication.translate("dashboard", u"Mail", None))
        self.label_4.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.image.setText("")
        self.firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.othername.setText(QCoreApplication.translate("dashboard", u"Othername", None))
        self.lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.reference.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.contact.setText(QCoreApplication.translate("dashboard", u"Contact", None))
        self.position.setText(QCoreApplication.translate("dashboard", u"Position", None))
        self.image_2.setText("")
        self.status.setText(QCoreApplication.translate("dashboard", u"Status", None))
        self.label_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.firstname_25.setText(QCoreApplication.translate("dashboard", u"Current Table", None))
        self.btn_refresh.setText(QCoreApplication.translate("dashboard", u"Refresh", None))
        self.firstname_26.setText("")
        self.status_2.setText(QCoreApplication.translate("dashboard", u"Status check", None))
        self.contact_2.setText(QCoreApplication.translate("dashboard", u"Hour(s)", None))
        self.contact_3.setText(QCoreApplication.translate("dashboard", u"Minute(s)", None))
        self.contact_4.setText(QCoreApplication.translate("dashboard", u":", None))
        self.read_only_property.setText(QCoreApplication.translate("dashboard", u"Read Only Property", None))
        self.time_zone.setItemText(0, QCoreApplication.translate("dashboard", u"AM", None))
        self.time_zone.setItemText(1, QCoreApplication.translate("dashboard", u"PM", None))

        self.firstname_27.setText(QCoreApplication.translate("dashboard", u"Operations", None))
        self.btn_clear_label.setText(QCoreApplication.translate("dashboard", u"Reset", None))
        self.btn_open_database.setText(QCoreApplication.translate("dashboard", u"Table", None))
        self.camera_view.setText("")
        self.label_14.setText(QCoreApplication.translate("dashboard", u"Camera Connection", None))
        self.btn_connect_detect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.btn_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera URL/IP?", None))
        self.label_18.setText(QCoreApplication.translate("dashboard", u"Camera Scan", None))
        self.scan_range_label.setText("")
        self.label_42.setText("")
        self.btn_scan_range.setText(QCoreApplication.translate("dashboard", u"Scan", None))
        self.scan_range.setPlaceholderText(QCoreApplication.translate("dashboard", u"Scan range ?", None))
        self.label_32.setText("")
        self.batch_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.btn_batch_browse.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.batch_filename.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.btn_start_job.setText(QCoreApplication.translate("dashboard", u"Insert", None))
        ___qtablewidgetitem = self.batch_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem1 = self.batch_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dashboard", u"Name", None));
        ___qtablewidgetitem2 = self.batch_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("dashboard", u"Contact", None));
        ___qtablewidgetitem3 = self.batch_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("dashboard", u"Position", None));
        ___qtablewidgetitem4 = self.batch_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("dashboard", u"Date stamp", None));
        ___qtablewidgetitem5 = self.batch_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("dashboard", u"Time stamp", None));
        ___qtablewidgetitem6 = self.batch_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("dashboard", u"Status", None));
        self.db_image_data.setText("")
        self.db_lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.db_middlename.setText(QCoreApplication.translate("dashboard", u"Othername", None))
        self.db_firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.db_contact.setText(QCoreApplication.translate("dashboard", u"Contact", None))
        self.db_incharge.setText(QCoreApplication.translate("dashboard", u"Incharge", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.btn_search_page.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_29.setText("")
        self.image_3.setText("")
        self.db_status.setText(QCoreApplication.translate("dashboard", u"Status", None))
        self.db_refrence.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.db_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Date", None))
        self.label_25.setText("")
        self.label_30.setText("")
        self.btn_csv.setText(QCoreApplication.translate("dashboard", u"Export ", None))
        self.label_40.setText("")
        self.filename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Filename?", None))
        self.btn_backup.setText(QCoreApplication.translate("dashboard", u"Backup", None))
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("dashboard", u"Name", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("dashboard", u"Contact", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("dashboard", u"Date Stamp", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("dashboard", u"Time Stamp", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("dashboard", u"Status", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("dashboard", u"Position", None));
        self.label_31.setText("")
        self.summary_filename.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.btn_summary_save.setText(QCoreApplication.translate("dashboard", u"Save", None))
        self.btn_summary_load.setText(QCoreApplication.translate("dashboard", u"Load", None))
        self.summary_browse.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.btn_summary_browse.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        ___qtablewidgetitem14 = self.tableWidget_summary.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("dashboard", u"Name", None));
        ___qtablewidgetitem15 = self.tableWidget_summary.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("dashboard", u"Contact", None));
        ___qtablewidgetitem16 = self.tableWidget_summary.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("dashboard", u"Date Stamp (ME)", None));
        ___qtablewidgetitem17 = self.tableWidget_summary.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("dashboard", u"Time Stamp (ME)", None));
        ___qtablewidgetitem18 = self.tableWidget_summary.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("dashboard", u"Date Stamp (ML)", None));
        ___qtablewidgetitem19 = self.tableWidget_summary.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("dashboard", u"Time Stamp (ML)", None));
        ___qtablewidgetitem20 = self.tableWidget_summary.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("dashboard", u"Early Count", None));
        ___qtablewidgetitem21 = self.tableWidget_summary.horizontalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("dashboard", u"Late Count", None));
        ___qtablewidgetitem22 = self.tableWidget_summary.horizontalHeaderItem(8)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("dashboard", u"Total Count", None));
    # retranslateUi

