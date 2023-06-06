import sys
import pyglet
import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QComboBox, QListWidget
from pytube import YouTube
from config import host, user, password, db_name
from PyQt5 import QtCore, QtGui, QtWidgets


player = pyglet.media.Player()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 60, 543, 445))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Reg_entr_btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Reg_entr_btn_2.setFont(font)
        self.Reg_entr_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reg_entr_btn_2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Reg_entr_btn_2.setObjectName("Reg_entr_btn_2")
        self.gridLayout_2.addWidget(self.Reg_entr_btn_2, 10, 0, 1, 1)
        self.Log_login_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Log_login_textbox.setFont(font)
        self.Log_login_textbox.setObjectName("Log_login_textbox")
        self.gridLayout_2.addWidget(self.Log_login_textbox, 4, 0, 1, 1)
        self.Password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Password_label.setFont(font)
        self.Password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Password_label.setObjectName("Password_label")
        self.gridLayout_2.addWidget(self.Password_label, 6, 0, 1, 1)
        self.MB_label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(60)
        self.MB_label_2.setFont(font)
        self.MB_label_2.setStyleSheet("color: rgb(255, 170, 127);")
        self.MB_label_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.MB_label_2.setObjectName("MB_label_2")
        self.gridLayout_2.addWidget(self.MB_label_2, 0, 0, 1, 1)
        self.Log_password_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Log_password_textbox.setFont(font)
        self.Log_password_textbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Log_password_textbox.setObjectName("Log_password_textbox")
        self.gridLayout_2.addWidget(self.Log_password_textbox, 8, 0, 1, 1)
        self.empty_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.empty_4.setText("")
        self.empty_4.setObjectName("empty_4")
        self.gridLayout_2.addWidget(self.empty_4, 7, 0, 1, 1)
        self.Login_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Login_label.setFont(font)
        self.Login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_label.setObjectName("Login_label")
        self.gridLayout_2.addWidget(self.Login_label, 2, 0, 1, 1)
        self.empty_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.empty_3.setText("")
        self.empty_3.setObjectName("empty_3")
        self.gridLayout_2.addWidget(self.empty_3, 5, 0, 1, 1)
        self.empty_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.empty_5.setText("")
        self.empty_5.setObjectName("empty_5")
        self.gridLayout_2.addWidget(self.empty_5, 9, 0, 1, 1)
        self.empty_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.empty_2.setText("")
        self.empty_2.setObjectName("empty_2")
        self.gridLayout_2.addWidget(self.empty_2, 3, 0, 1, 1)
        self.empty_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.empty_1.setText("")
        self.empty_1.setObjectName("empty_1")
        self.gridLayout_2.addWidget(self.empty_1, 1, 0, 1, 1)
        self.Log_registration_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Log_registration_btn.setFont(font)
        self.Log_registration_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Log_registration_btn.setStyleSheet("background-color: rgb(170, 85, 127);")
        self.Log_registration_btn.setObjectName("Log_registration_btn")
        self.gridLayout_2.addWidget(self.Log_registration_btn, 12, 0, 1, 1)
        self.empty_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.empty_6.setText("")
        self.empty_6.setObjectName("empty_6")
        self.gridLayout_2.addWidget(self.empty_6, 11, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(130, 60, 543, 415))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Reg_emai_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Reg_emai_textbox.setFont(font)
        self.Reg_emai_textbox.setObjectName("Reg_emai_textbox")
        self.gridLayout_3.addWidget(self.Reg_emai_textbox, 4, 1, 1, 1)
        self.Login_label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Login_label_9.setFont(font)
        self.Login_label_9.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Login_label_9.setObjectName("Login_label_9")
        self.gridLayout_3.addWidget(self.Login_label_9, 3, 0, 1, 1)
        self.Login_label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(20)
        self.Login_label_8.setFont(font)
        self.Login_label_8.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Login_label_8.setObjectName("Login_label_8")
        self.gridLayout_3.addWidget(self.Login_label_8, 4, 0, 1, 1)
        self.Password_textbox_7 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Password_textbox_7.setFont(font)
        self.Password_textbox_7.setObjectName("Password_textbox_7")
        self.gridLayout_3.addWidget(self.Password_textbox_7, 6, 1, 1, 1)
        self.Reg_login_textbox_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Reg_login_textbox_3.setEnabled(True)
        self.Reg_login_textbox_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Reg_login_textbox_3.setFont(font)
        self.Reg_login_textbox_3.setObjectName("Reg_login_textbox_3")
        self.gridLayout_3.addWidget(self.Reg_login_textbox_3, 3, 1, 1, 1)
        self.Login_label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Login_label_11.setFont(font)
        self.Login_label_11.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Login_label_11.setObjectName("Login_label_11")
        self.gridLayout_3.addWidget(self.Login_label_11, 8, 0, 1, 1)
        self.Password_textbox_8 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Password_textbox_8.setFont(font)
        self.Password_textbox_8.setObjectName("Password_textbox_8")
        self.gridLayout_3.addWidget(self.Password_textbox_8, 8, 1, 1, 1)
        self.Password_textbox_9 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Password_textbox_9.setFont(font)
        self.Password_textbox_9.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_textbox_9.setObjectName("Password_textbox_9")
        self.gridLayout_3.addWidget(self.Password_textbox_9, 9, 1, 1, 1)
        self.Login_label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Login_label_12.setFont(font)
        self.Login_label_12.setStyleSheet("")
        self.Login_label_12.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Login_label_12.setObjectName("Login_label_12")
        self.gridLayout_3.addWidget(self.Login_label_12, 9, 0, 1, 1)
        self.Login_label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.Login_label_13.setFont(font)
        self.Login_label_13.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Login_label_13.setObjectName("Login_label_13")
        self.gridLayout_3.addWidget(self.Login_label_13, 1, 1, 1, 1)
        self.MB_label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(60)
        self.MB_label_3.setFont(font)
        self.MB_label_3.setStyleSheet("color: rgb(255, 170, 127);")
        self.MB_label_3.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.MB_label_3.setObjectName("MB_label_3")
        self.gridLayout_3.addWidget(self.MB_label_3, 0, 1, 1, 1)
        self.Login_label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Login_label_10.setFont(font)
        self.Login_label_10.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Login_label_10.setObjectName("Login_label_10")
        self.gridLayout_3.addWidget(self.Login_label_10, 6, 0, 1, 1)
        self.Reg_entr_btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Reg_entr_btn_4.setFont(font)
        self.Reg_entr_btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reg_entr_btn_4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Reg_entr_btn_4.setObjectName("Reg_entr_btn_4")
        self.gridLayout_3.addWidget(self.Reg_entr_btn_4, 11, 1, 1, 1)
        self.Reg_entr_btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Reg_entr_btn_3.setFont(font)
        self.Reg_entr_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reg_entr_btn_3.setStyleSheet("background-color: rgb(170, 85, 127);")
        self.Reg_entr_btn_3.setObjectName("Reg_entr_btn_3")
        self.gridLayout_3.addWidget(self.Reg_entr_btn_3, 10, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 180, 531, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Peace_radio_btn = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Peace_radio_btn.setFont(font)
        self.Peace_radio_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Peace_radio_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Покой.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("Покой_Выб.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("Покой_Выб.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("Покой_Выб.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("Покой_Выб.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.Peace_radio_btn.setIcon(icon)
        self.Peace_radio_btn.setIconSize(QtCore.QSize(100, 100))
        self.Peace_radio_btn.setObjectName("Peace_radio_btn")
        self.horizontalLayout.addWidget(self.Peace_radio_btn)
        self.Sad_radio_btn = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Sad_radio_btn.setFont(font)
        self.Sad_radio_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Sad_radio_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Грустно_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Sad_radio_btn.setIcon(icon1)
        self.Sad_radio_btn.setIconSize(QtCore.QSize(100, 100))
        self.Sad_radio_btn.setObjectName("Sad_radio_btn")
        self.horizontalLayout.addWidget(self.Sad_radio_btn)
        self.Angry_radio_btn = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Angry_radio_btn.setFont(font)
        self.Angry_radio_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Angry_radio_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Гнев.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Angry_radio_btn.setIcon(icon2)
        self.Angry_radio_btn.setIconSize(QtCore.QSize(100, 100))
        self.Angry_radio_btn.setObjectName("Angry_radio_btn")
        self.horizontalLayout.addWidget(self.Angry_radio_btn)
        self.Happy_radio_btn = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Happy_radio_btn.setFont(font)
        self.Happy_radio_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Happy_radio_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Весело.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Happy_radio_btn.setIcon(icon3)
        self.Happy_radio_btn.setIconSize(QtCore.QSize(100, 100))
        self.Happy_radio_btn.setObjectName("Happy_radio_btn")
        self.horizontalLayout.addWidget(self.Happy_radio_btn)
        self.Pl_2_btn = QtWidgets.QPushButton(self.page_3)
        self.Pl_2_btn.setGeometry(QtCore.QRect(630, 360, 150, 150))
        self.Pl_2_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pl_2_btn.setStyleSheet("background-image: url(альб_2.jpg);\n"
                                    "    background-repeat: no-repeat;\n"
                                    "    background-position: center;")
        self.Pl_2_btn.setText("")
        self.Pl_2_btn.setObjectName("Pl_2_btn")
        self.Pl_1_btn = QtWidgets.QPushButton(self.page_3)
        self.Pl_1_btn.setGeometry(QtCore.QRect(630, 180, 150, 150))
        self.Pl_1_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pl_1_btn.setStyleSheet("background-image: url(альб_1.jpg);\n"
                                    "    background-repeat: no-repeat;\n"
                                    "    background-position: center;")
        self.Pl_1_btn.setText("")
        self.Pl_1_btn.setObjectName("Pl_1_btn")
        self.Create_pl_btn = QtWidgets.QPushButton(self.page_3)
        self.Create_pl_btn.setGeometry(QtCore.QRect(30, 482, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(25)
        self.Create_pl_btn.setFont(font)
        self.Create_pl_btn.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Create_pl_btn.setObjectName("Create_pl_btn")
        self.Popular_pl_label = QtWidgets.QLabel(self.page_3)
        self.Popular_pl_label.setGeometry(QtCore.QRect(630, 110, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Popular_pl_label.setFont(font)
        self.Popular_pl_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Popular_pl_label.setObjectName("Popular_pl_label")
        self.Main_label = QtWidgets.QLabel(self.page_3)
        self.Main_label.setGeometry(QtCore.QRect(80, 40, 441, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.Main_label.setFont(font)
        self.Main_label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_label.setObjectName("Main_label")
        self.Mood_label = QtWidgets.QLabel(self.page_3)
        self.Mood_label.setGeometry(QtCore.QRect(120, 110, 351, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Mood_label.setFont(font)
        self.Mood_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Mood_label.setObjectName("Mood_label")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 410, 531, 58))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Language_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(17)
        self.Language_label.setFont(font)
        self.Language_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Language_label.setObjectName("Language_label")
        self.horizontalLayout_3.addWidget(self.Language_label)
        self.Language_combobox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Language_combobox.setFont(font)
        self.Language_combobox.setStyleSheet("")
        self.Language_combobox.setObjectName("Language_combobox")
        self.Language_combobox.addItem("")
        self.Language_combobox.addItem("")
        self.Language_combobox.addItem("")
        self.Language_combobox.addItem("")
        self.Language_combobox.addItem("")
        self.horizontalLayout_3.addWidget(self.Language_combobox)
        self.Main_to_reg_btn = QtWidgets.QPushButton(self.page_3)
        self.Main_to_reg_btn.setGeometry(QtCore.QRect(730, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(45)
        self.Main_to_reg_btn.setFont(font)
        self.Main_to_reg_btn.setStyleSheet("color: rgb(255, 85, 255);")
        self.Main_to_reg_btn.setObjectName("Main_to_reg_btn")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 330, 531, 68))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Genre_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(17)
        self.Genre_label.setFont(font)
        self.Genre_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Genre_label.setObjectName("Genre_label")
        self.horizontalLayout_2.addWidget(self.Genre_label)
        self.Genre_combobox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Genre_combobox.setFont(font)
        self.Genre_combobox.setObjectName("Genre_combobox")
        self.Genre_combobox.addItem("")
        self.Genre_combobox.addItem("")
        self.Genre_combobox.addItem("")
        self.Genre_combobox.addItem("")
        self.Genre_combobox.addItem("")
        self.Genre_combobox.addItem("")
        self.horizontalLayout_2.addWidget(self.Genre_combobox)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.Playlist_label = QtWidgets.QLabel(self.page_4)
        self.Playlist_label.setGeometry(QtCore.QRect(30, 40, 741, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.Playlist_label.setFont(font)
        self.Playlist_label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Playlist_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Playlist_label.setObjectName("Playlist_label")
        self.Out_to_reg_btn = QtWidgets.QPushButton(self.page_4)
        self.Out_to_reg_btn.setGeometry(QtCore.QRect(730, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(45)
        self.Out_to_reg_btn.setFont(font)
        self.Out_to_reg_btn.setStyleSheet("color: rgb(255, 85, 255);")
        self.Out_to_reg_btn.setObjectName("Out_to_reg_btn")
        self.Add_sons_list = QtWidgets.QListWidget(self.page_4)
        self.Add_sons_list.setGeometry(QtCore.QRect(25, 100, 751, 341))
        self.Add_sons_list.setObjectName("Add_sons_list")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.page_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(30, 460, 741, 92))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Add_del_songs_from_BD_btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Add_del_songs_from_BD_btn_2.setFont(font)
        self.Add_del_songs_from_BD_btn_2.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.Add_del_songs_from_BD_btn_2.setObjectName("Add_del_songs_from_BD_btn_2")
        self.gridLayout.addWidget(self.Add_del_songs_from_BD_btn_2, 1, 0, 1, 1)
        self.Add_del_songs_from_pl_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Add_del_songs_from_pl_btn.setFont(font)
        self.Add_del_songs_from_pl_btn.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Add_del_songs_from_pl_btn.setObjectName("Add_del_songs_from_pl_btn")
        self.gridLayout.addWidget(self.Add_del_songs_from_pl_btn, 0, 0, 1, 1)
        self.Add_to_pl_page_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Add_to_pl_page_btn.setFont(font)
        self.Add_to_pl_page_btn.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Add_to_pl_page_btn.setObjectName("Add_to_pl_page_btn")
        self.gridLayout.addWidget(self.Add_to_pl_page_btn, 0, 1, 1, 1)
        self.Out_to_main_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Out_to_main_btn.setFont(font)
        self.Out_to_main_btn.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Out_to_main_btn.setObjectName("Out_to_main_btn")
        self.gridLayout.addWidget(self.Out_to_main_btn, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.Add_to_reg_btn = QtWidgets.QPushButton(self.page_5)
        self.Add_to_reg_btn.setGeometry(QtCore.QRect(730, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(45)
        self.Add_to_reg_btn.setFont(font)
        self.Add_to_reg_btn.setStyleSheet("color: rgb(255, 85, 255);")
        self.Add_to_reg_btn.setObjectName("Add_to_reg_btn")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.page_5)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(130, 60, 543, 415))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Add_autor_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Add_autor_textbox.setFont(font)
        self.Add_autor_textbox.setObjectName("Add_autor_textbox")
        self.gridLayout_4.addWidget(self.Add_autor_textbox, 2, 1, 1, 1)
        self.Add_autor_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(20)
        self.Add_autor_label.setFont(font)
        self.Add_autor_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Add_autor_label.setObjectName("Add_autor_label")
        self.gridLayout_4.addWidget(self.Add_autor_label, 2, 0, 1, 1)
        self.Add_name_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Add_name_label.setFont(font)
        self.Add_name_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Add_name_label.setObjectName("Add_name_label")
        self.gridLayout_4.addWidget(self.Add_name_label, 1, 0, 1, 1)
        self.Add_albom_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Add_albom_textbox.setFont(font)
        self.Add_albom_textbox.setObjectName("Add_albom_textbox")
        self.gridLayout_4.addWidget(self.Add_albom_textbox, 4, 1, 1, 1)
        self.Add_href_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Add_href_textbox.setFont(font)
        self.Add_href_textbox.setObjectName("Add_href_textbox")
        self.gridLayout_4.addWidget(self.Add_href_textbox, 7, 1, 1, 1)
        self.Add_to_pl_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Add_to_pl_btn.setFont(font)
        self.Add_to_pl_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add_to_pl_btn.setStyleSheet("background-color: rgb(170, 85, 127);")
        self.Add_to_pl_btn.setObjectName("Add_to_pl_btn")
        self.gridLayout_4.addWidget(self.Add_to_pl_btn, 10, 1, 1, 1)
        self.Add_date_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Add_date_textbox.setFont(font)
        self.Add_date_textbox.setObjectName("Add_date_textbox")
        self.gridLayout_4.addWidget(self.Add_date_textbox, 6, 1, 1, 1)
        self.Add_name_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Add_name_textbox.setEnabled(True)
        self.Add_name_textbox.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Add_name_textbox.setFont(font)
        self.Add_name_textbox.setObjectName("Add_name_textbox")
        self.gridLayout_4.addWidget(self.Add_name_textbox, 1, 1, 1, 1)
        self.Add_date_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Add_date_label.setFont(font)
        self.Add_date_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Add_date_label.setObjectName("Add_date_label")
        self.gridLayout_4.addWidget(self.Add_date_label, 6, 0, 1, 1)
        self.Add_albom_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Add_albom_label.setFont(font)
        self.Add_albom_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Add_albom_label.setObjectName("Add_albom_label")
        self.gridLayout_4.addWidget(self.Add_albom_label, 4, 0, 1, 1)
        self.Back_to_pl_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Back_to_pl_btn.setFont(font)
        self.Back_to_pl_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_to_pl_btn.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Back_to_pl_btn.setObjectName("Back_to_pl_btn")
        self.gridLayout_4.addWidget(self.Back_to_pl_btn, 11, 1, 1, 1)
        self.Add_href_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(20)
        self.Add_href_label.setFont(font)
        self.Add_href_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Add_href_label.setObjectName("Add_href_label")
        self.gridLayout_4.addWidget(self.Add_href_label, 7, 0, 1, 1)
        self.Add_to_pl_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.Add_to_pl_label.setFont(font)
        self.Add_to_pl_label.setStyleSheet("color: rgb(255, 170, 0);")
        self.Add_to_pl_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.Add_to_pl_label.setObjectName("Add_to_pl_label")
        self.gridLayout_4.addWidget(self.Add_to_pl_label, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Out_action = QtWidgets.QAction(MainWindow)
        self.Out_action.setObjectName("Out_action")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.Out_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        # Кнопка "регистрация" на окне входа
        self.Log_registration_btn.clicked.connect(self.to_reg_page)

        self.Reg_entr_btn_3.clicked.connect(self.register)

        # Кнопка "вернуться ко входу" на окне регистрации
        self.Reg_entr_btn_4.clicked.connect(self.to_log_page)

        self.Reg_entr_btn_2.clicked.connect(self.login)

        # Кнопки в правом верхем углу
        self.Main_to_reg_btn.clicked.connect(self.to_log_page)
        self.Out_to_reg_btn.clicked.connect(self.to_log_page)
        self.Add_to_reg_btn.clicked.connect(self.to_log_page)

        # Кнопка "Создать плейлист" НЕ ГОТОВО
        self.Create_pl_btn.clicked.connect(self.create_playlist)

        # Кнопка "Вернуться на главную страницу" из созданного плейлиста
        self.Out_to_main_btn.clicked.connect(self.to_main_page)

        # Кнопка "Добавить новую песню в плейлист" ВООБЩЕ НЕ ГОТОВО
        self.Add_to_pl_page_btn.clicked.connect(self.create_new_song)

        # Кнопка "Вернуться к плейлисту" из добавления в плелист
        self.Back_to_pl_btn.clicked.connect(self.to_created_playlist_2)

        self.Add_to_pl_btn.clicked.connect(self.add_song_in_playlist)

        self.Add_del_songs_from_pl_btn.clicked.connect(self.del_this_song)

        self.Add_sons_list.itemDoubleClicked.connect(self.play_selected_music)

        self.Add_del_songs_from_BD_btn_2.clicked.connect(self.delete_song_from_database)

    # Функция "Создать плейлист" ВООБЩЕ НЕ ГОТОВО
    def to_created_playlist(self):
        self.stackedWidget.setCurrentIndex(3)

    # Функция "Вернуться к плейлисту"
    def to_created_playlist_2(self):
        self.stackedWidget.setCurrentIndex(3)

    # Функция "Добавить новую песню в плейлист" ВООБЩЕ НЕ ГОТОВО
    def create_new_song(self):
        self.stackedWidget.setCurrentIndex(4)

    def to_reg_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def to_log_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def to_main_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.Add_sons_list.clear()

    def show_error_message(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def show_message(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Успех")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Reg_entr_btn_2.setText(_translate("MainWindow", "Войти"))
        self.Password_label.setText(_translate("MainWindow", "Пароль"))
        self.MB_label_2.setText(_translate("MainWindow", "MUSICALBOX"))
        self.Login_label.setText(_translate("MainWindow", "Логин"))
        self.Log_registration_btn.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.Login_label_9.setText(_translate("MainWindow", "Логин"))
        self.Login_label_8.setText(_translate("MainWindow", "e-mail"))
        self.Login_label_11.setText(_translate("MainWindow", "Фамилия"))
        self.Login_label_12.setText(_translate("MainWindow", "Пароль"))
        self.Login_label_13.setText(_translate("MainWindow", "Регистрация"))
        self.MB_label_3.setText(_translate("MainWindow", "MUSICALBOX"))
        self.Login_label_10.setText(_translate("MainWindow", "Имя"))
        self.Reg_entr_btn_4.setText(_translate("MainWindow", "Вернуться ко входу"))
        self.Reg_entr_btn_3.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.Create_pl_btn.setText(_translate("MainWindow", "Создать Плейлист"))
        self.Popular_pl_label.setText(_translate("MainWindow", "Популярные \n"
                                                               "плейлисты"))
        self.Main_label.setText(_translate("MainWindow", "Создайте собственный плейлист"))
        self.Mood_label.setText(_translate("MainWindow", "Какое у вас сейчас настроение?"))
        self.Language_label.setText(_translate("MainWindow", "На каком языке вы бы \n"
                                                             "хотели слушать музыку?"))
        self.Language_combobox.setItemText(0, _translate("MainWindow", "..."))
        self.Language_combobox.setItemText(1, _translate("MainWindow", "Русский"))
        self.Language_combobox.setItemText(2, _translate("MainWindow", "Английский"))
        self.Language_combobox.setItemText(3, _translate("MainWindow", "Японский"))
        self.Language_combobox.setItemText(4, _translate("MainWindow", "Без вокала"))
        self.Main_to_reg_btn.setText(_translate("MainWindow", "MB"))
        self.Genre_label.setText(_translate("MainWindow", "Какие музыкальные жанры\n"
                                                          " вы предпочитаете?"))
        self.Genre_combobox.setItemText(0, _translate("MainWindow", "..."))
        self.Genre_combobox.setItemText(1, _translate("MainWindow", "Рок"))
        self.Genre_combobox.setItemText(2, _translate("MainWindow", "Поп"))
        self.Genre_combobox.setItemText(3, _translate("MainWindow", "Рэп"))
        self.Genre_combobox.setItemText(4, _translate("MainWindow", "Phonk"))
        self.Genre_combobox.setItemText(5, _translate("MainWindow", "Лирика"))
        self.Playlist_label.setText(_translate("MainWindow", "Созданный плейлист"))
        self.Out_to_reg_btn.setText(_translate("MainWindow", "MB"))
        __sortingEnabled = self.Add_sons_list.isSortingEnabled()
        self.Add_sons_list.setSortingEnabled(False)
        item = self.Add_sons_list.item(0)
        self.Add_sons_list.setSortingEnabled(__sortingEnabled)
        self.Add_del_songs_from_BD_btn_2.setText(_translate("MainWindow", "Удалить выбранные песни из БД"))
        self.Add_del_songs_from_pl_btn.setText(_translate("MainWindow", "Удалить выбранные песни из плейлиста"))
        self.Add_to_pl_page_btn.setText(_translate("MainWindow", "Добавить новую песню в плейлист"))
        self.Out_to_main_btn.setText(_translate("MainWindow", "Выйти на главную страницу"))
        self.Add_to_reg_btn.setText(_translate("MainWindow", "MB"))
        self.Add_autor_label.setText(_translate("MainWindow", "Автор"))
        self.Add_name_label.setText(_translate("MainWindow", "Название песни"))
        self.Add_to_pl_btn.setText(_translate("MainWindow", "Добавить в плейлист"))
        self.Add_date_label.setText(_translate("MainWindow", "Дата создания"))
        self.Add_albom_label.setText(_translate("MainWindow", "Альбом"))
        self.Back_to_pl_btn.setText(_translate("MainWindow", "Вернуться к плейлисту"))
        self.Add_href_label.setText(_translate("MainWindow", "Ссылка Youtube"))
        self.Add_to_pl_label.setText(_translate("MainWindow", "Добавление песен"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.Out_action.setText(_translate("MainWindow", "Выйти"))
        self.action.setText(_translate("MainWindow", "Важно!"))

    def login(self):
        username = self.Log_login_textbox.text()
        password1 = self.Log_password_textbox.text()
        # Проверка логина и пароля в базе данных
        try:
            # Подключение к базе данных
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            print("Connection already")

            # Создание объекта курсора
            cursor = connection.cursor()

            # Выполнение SQL-запроса для проверки логина и пароля
            query = "SELECT * FROM users WHERE Login=%s AND Password=%s"
            cursor.execute(query, (username, password1))

            # Получение результата запроса
            result = cursor.fetchone()

            print(result)

            if result:
                self.to_main_page()  # Переключение на индекс главного окна
            else:
                self.show_error_message("Неверный логин или пароль.")

            cursor.close()
            connection.close()

        except pymysql.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def register(self):
        username = self.Reg_login_textbox_3.text()
        password1 = self.Password_textbox_9.text()
        mail = self.Reg_emai_textbox.text()
        Name = self.Password_textbox_7.text()
        Surname = self.Password_textbox_8.text()
        try:
            # Подключение к базе данных
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            print("Connection already")
            # Создание объекта курсора
            cursor = connection.cursor()

            # Проверка, что логин не занят
            query = "SELECT * FROM users WHERE Login=%s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                self.show_error_message("Логин уже занят.")
                cursor.close()
                connection.close()
                return

            # Вставка нового пользователя в базу данных
            query = "INSERT INTO users (Login, Password, `e-mail`, Name, Surname) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (username, password1, mail, Name, Surname))
            connection.commit()

            self.show_message("Регистрация прошла успешно.")

            cursor.close()
            connection.close()

            self.to_log_page()  # Переключение на индекс окна входа

        except pymysql.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def create_playlist(self):
        genre = self.genre_combo_box_changed()
        nastroy = self.radio_button_checked()
        language = self.language_combo_box_changed()

        try:
            # Подключение к базе данных
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            print("Connection already3")
            # Создание объекта курсора
            cursor = connection.cursor()

            # Проверка, что логин не занят
            query = "SELECT m.MusicName, m.Autor_id, a.AutorName, m.href FROM music m JOIN autor a ON m.Autor_id = a.Autor_id " \
                    "WHERE m.Genre_id=%s AND m.Nastroy_id=%s AND m.Language_id=%s "

            cursor.execute(query, (genre, nastroy, language))
            result = cursor.fetchall()
            print(result)
            self.add_tuple_to_list(result)

            cursor.close()
            connection.close()
            self.to_created_playlist()

            # Переключение на индекс окна входа

        except pymysql.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def radio_button_checked(self):
        if self.Peace_radio_btn.isChecked():
            print("RadioButton 1 нажат")
            return 3
        elif self.Sad_radio_btn.isChecked():
            print("RadioButton 2 нажат")
            return 1
        elif self.Happy_radio_btn.isChecked():
            print("RadioButton 3 нажат")
            return 2
        elif self.Angry_radio_btn.isChecked():
            print("RadioButton 4 нажат")
            return 4

    def genre_combo_box_changed(self):
        selected_option = self.Genre_combobox.currentText()

        try:
            # Подключение к базе данных
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            print("Connection already1")
            # Создание объекта курсора
            cursor = connection.cursor()

            # Проверка, что логин не занят
            query = "SELECT Genre_id FROM genre WHERE Genre=%s"
            cursor.execute(query, (selected_option,))
            result = cursor.fetchone()
            print(result[0])
            cursor.close()
            connection.close()
            return result[0]

        except pymysql.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def language_combo_box_changed(self):
        selected_option = self.Language_combobox.currentText()

        try:
            # Подключение к базе данных
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            print("Connection already2")
            # Создание объекта курсора
            cursor = connection.cursor()

            # Проверка, что логин не занят
            query = "SELECT Language_id FROM language WHERE Language=%s"
            cursor.execute(query, (selected_option,))
            result = cursor.fetchone()
            print(result[0])
            cursor.close()
            connection.close()
            return result[0]

        except pymysql.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def add_tuple_to_list(self, tuple_item):
        for i in tuple_item:
            music_name = i[0]
            autor_id = i[1]
            autor_name = i[2]
            music_href = i[3]
            string_item = f"{music_name} - {autor_name}"
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(15)
            item.setFont(font)
            item.setCheckState(QtCore.Qt.Checked)
            self.Add_sons_list.addItem(string_item)
        __sortingEnabled = self.Add_sons_list.isSortingEnabled()
        self.Add_sons_list.setSortingEnabled(False)
        item = self.Add_sons_list.item(0)
        self.Add_sons_list.setSortingEnabled(__sortingEnabled)

    def add_song_in_playlist(self):
        song_name = self.Add_name_textbox.text()
        autor_song = self.Add_autor_textbox.text()
        albom = self.Add_albom_textbox.text()
        date_of_song = self.Add_date_textbox.text()
        href_of_song = self.Add_href_textbox.text()

        string_item = f"{song_name} - {autor_song}"
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        item.setCheckState(QtCore.Qt.Checked)
        self.Add_sons_list.addItem(string_item)

        __sortingEnabled = self.Add_sons_list.isSortingEnabled()
        self.Add_sons_list.setSortingEnabled(False)
        item = self.Add_sons_list.item(0)
        self.Add_sons_list.setSortingEnabled(__sortingEnabled)

        self.to_created_playlist()

    def del_this_song(self):
        selected_item = self.Add_sons_list.currentItem()
        if selected_item is not None:
            self.Add_sons_list.takeItem(self.Add_sons_list.row(selected_item))

    def play_selected_music(self):
        select_item = self.Add_sons_list.currentItem().text()
        song_name, autor_name = select_item.split(" - ")
        result = ""

        try:
            # Подключение к базе данных
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            print("Connection already5")
            # Создание объекта курсора
            cursor = connection.cursor()

            # Проверка, что логин не занят
            query = "SELECT href FROM music WHERE MusicName=%s"
            cursor.execute(query, (song_name,))
            result = cursor.fetchone()
            print(result[0])
            cursor.close()
            connection.close()

            url = result[0]  # Получаем ссылку на музыку из пользовательских данных элемента

            # Создаем объект YouTube для получения потока аудио
            youtube = YouTube(url)
            audio_stream = youtube.streams.filter(only_audio=True).first()

            # Скачиваем аудио во временный файл
            temp_file_path = "temp_audio.mp3"
            audio_stream.download(filename=temp_file_path)

            # Воспроизводим аудио с помощью pyglet
            music = pyglet.media.load(temp_file_path)

            player = pyglet.media.Player()
            player.queue(music)
            player.play()

            pyglet.app.run()

        except pymysql.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def delete_song_from_database(self):
        song_name, autor_name = self.Add_sons_list.currentItem().text().split(" - ")
        try:
            # Подключение к базе данных
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            print("Connection already5")
            # Создание объекта курсора
            cursor = connection.cursor()

            # Проверка, что логин не занят
            query = "DELETE FROM music WHERE MusicName=%s"
            cursor.execute(query, (song_name,))
            connection.commit()
            print("Запись успешно удалена")
            cursor.close()
            connection.close()
            selected_item = self.Add_sons_list.currentItem()
            self.Add_sons_list.takeItem(self.Add_sons_list.row(selected_item))

        except pymysql.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
