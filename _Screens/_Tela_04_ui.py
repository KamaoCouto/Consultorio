# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_Tela_04.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTimeEdit, QVBoxLayout, QWidget)

#==============================================================================================
# Criando Imports imagens.py
#==============================================================================================
from ._Imagens  import (Background_rc,BT_s_rc,Logo_rc,Title_rc)

class Ui_Form_Agenda(object):
    def setupUi(self, Form_Agenda):
        if not Form_Agenda.objectName():
            Form_Agenda.setObjectName(u"Form_Agenda")
        Form_Agenda.resize(750, 615)
        Form_Agenda.setMinimumSize(QSize(0, 615))
        Form_Agenda.setMaximumSize(QSize(16777215, 615))
        Form_Agenda.setStyleSheet(u"background-color: rgb(193, 237, 255);")
        self.gridLayout_2 = QGridLayout(Form_Agenda)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 5, 0, 0)
        self.widget_7 = QWidget(Form_Agenda)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QSize(625, 0))
        self.widget_7.setMaximumSize(QSize(625, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.widget_7)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 10, 0, 0)
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(625, 0))
        self.label_3.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"\n"
"")

        self.verticalLayout_14.addWidget(self.label_3)

        self.Tbox_Agenda = QStackedWidget(self.widget_7)
        self.Tbox_Agenda.setObjectName(u"Tbox_Agenda")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Tbox_Agenda.sizePolicy().hasHeightForWidth())
        self.Tbox_Agenda.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Lucida Calligraphy"])
        font.setPointSize(10)
        self.Tbox_Agenda.setFont(font)
        self.Tbox_Agenda.setStyleSheet(u"QToolBox::tab{\n"
"	border-radius:5px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.Tbox_AgendaHome = QWidget()
        self.Tbox_AgendaHome.setObjectName(u"Tbox_AgendaHome")
        self.horizontalLayout = QHBoxLayout(self.Tbox_AgendaHome)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.Tbox_AgendaHome)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(415, 532))
        self.label.setMaximumSize(QSize(415, 532))
        self.label.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Lucida Calligraphy\";\n"
"placeHolder-text-align: Center;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QFrame{\n"
"border-radius:10px;\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Sorriso.jpg);\n"
"}")

        self.horizontalLayout.addWidget(self.label)

        self.Tbox_Agenda.addWidget(self.Tbox_AgendaHome)
        self.Tbox_AgendaPage1 = QWidget()
        self.Tbox_AgendaPage1.setObjectName(u"Tbox_AgendaPage1")
        self.gridLayout_11 = QGridLayout(self.Tbox_AgendaPage1)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.frame_8 = QFrame(self.Tbox_AgendaPage1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(415, 532))
        self.frame_8.setMaximumSize(QSize(415, 532))
        self.frame_8.setStyleSheet(u"QFrame{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Sorriso.jpg);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Lucida Calligraphy\";\n"
"}\n"
"\n"
"QRadioButton{\n"
"background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Lucida Calligraphy\";\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 10, 0, 0)
        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.timeEdit = QTimeEdit(self.frame_6)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout_10.addWidget(self.timeEdit, 3, 0, 1, 1)

        self.BT_Consultar_Agenda = QPushButton(self.frame_6)
        self.BT_Consultar_Agenda.setObjectName(u"BT_Consultar_Agenda")
        self.BT_Consultar_Agenda.setMinimumSize(QSize(0, 20))
        font1 = QFont()
        font1.setFamilies([u"Lucida Calligraphy"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.BT_Consultar_Agenda.setFont(font1)
        self.BT_Consultar_Agenda.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Consultar_Agenda.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Yellow.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.gridLayout_10.addWidget(self.BT_Consultar_Agenda, 2, 2, 1, 1)

        self.Calendario = QCalendarWidget(self.frame_6)
        self.Calendario.setObjectName(u"Calendario")
        self.Calendario.setStyleSheet(u"background-color: rgb(193, 237, 255);\n"
"selection-color: rgb(0, 85, 255);")

        self.gridLayout_10.addWidget(self.Calendario, 1, 0, 1, 3)

        self.dateEdit = QDateEdit(self.frame_6)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout_10.addWidget(self.dateEdit, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 1, 3)


        self.gridLayout_11.addWidget(self.frame_8, 0, 1, 1, 1)

        self.Tbox_Agenda.addWidget(self.Tbox_AgendaPage1)
        self.Tbox_AgendaPage2 = QWidget()
        self.Tbox_AgendaPage2.setObjectName(u"Tbox_AgendaPage2")
        self.horizontalLayout_3 = QHBoxLayout(self.Tbox_AgendaPage2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_2 = QWidget(self.Tbox_AgendaPage2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"border-radius:10px;")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.frame_47 = QFrame(self.widget_2)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(415, 0))
        self.frame_47.setMaximumSize(QSize(415, 16777215))
        self.frame_47.setStyleSheet(u"border-radius:10px;\n"
"selection-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_47)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_26 = QLabel(self.frame_47)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(60, 20))
        self.label_26.setMaximumSize(QSize(150, 50))

        self.gridLayout_6.addWidget(self.label_26, 0, 2, 1, 1)

        self.comboBox_9 = QComboBox(self.frame_47)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(60, 20))
        self.comboBox_9.setMaximumSize(QSize(200, 50))

        self.gridLayout_6.addWidget(self.comboBox_9, 1, 3, 1, 1)

        self.radioButton = QRadioButton(self.frame_47)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_6.addWidget(self.radioButton, 1, 0, 1, 1)

        self.label_27 = QLabel(self.frame_47)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(60, 20))
        self.label_27.setMaximumSize(QSize(150, 50))

        self.gridLayout_6.addWidget(self.label_27, 0, 1, 1, 1)

        self.label_28 = QLabel(self.frame_47)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(60, 20))
        self.label_28.setMaximumSize(QSize(150, 50))

        self.gridLayout_6.addWidget(self.label_28, 0, 3, 1, 1)

        self.comboBox_8 = QComboBox(self.frame_47)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(60, 20))
        self.comboBox_8.setMaximumSize(QSize(200, 50))

        self.gridLayout_6.addWidget(self.comboBox_8, 1, 2, 1, 1)

        self.comboBox_10 = QComboBox(self.frame_47)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMinimumSize(QSize(60, 20))
        self.comboBox_10.setMaximumSize(QSize(200, 50))

        self.gridLayout_6.addWidget(self.comboBox_10, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_47, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.frame_9 = QFrame(self.widget_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setStyleSheet(u"border-radius:20px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.tableWidget_2 = QTableWidget(self.frame_9)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget_2.rowCount() < 26):
            self.tableWidget_2.setRowCount(26)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(19, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(20, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(21, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(22, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(23, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(24, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(25, __qtablewidgetitem30)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy2)
        self.tableWidget_2.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.tableWidget_2)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.BT_Medicamentos_4 = QPushButton(self.frame_10)
        self.BT_Medicamentos_4.setObjectName(u"BT_Medicamentos_4")
        self.BT_Medicamentos_4.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        self.BT_Medicamentos_4.setFont(font2)
        self.BT_Medicamentos_4.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.BT_Medicamentos_4)

        self.BT_Medicamentos_6 = QPushButton(self.frame_10)
        self.BT_Medicamentos_6.setObjectName(u"BT_Medicamentos_6")
        self.BT_Medicamentos_6.setMinimumSize(QSize(0, 20))
        self.BT_Medicamentos_6.setFont(font2)
        self.BT_Medicamentos_6.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.BT_Medicamentos_6)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)


        self.horizontalLayout_13.addWidget(self.frame_10)


        self.gridLayout.addWidget(self.frame_9, 1, 0, 1, 4)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.Tbox_Agenda.addWidget(self.Tbox_AgendaPage2)

        self.verticalLayout_14.addWidget(self.Tbox_Agenda)


        self.gridLayout_2.addWidget(self.widget_7, 0, 1, 1, 1)

        self.frameAgenda_BTs_1 = QFrame(Form_Agenda)
        self.frameAgenda_BTs_1.setObjectName(u"frameAgenda_BTs_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frameAgenda_BTs_1.sizePolicy().hasHeightForWidth())
        self.frameAgenda_BTs_1.setSizePolicy(sizePolicy3)
        self.frameAgenda_BTs_1.setMinimumSize(QSize(0, 0))
        self.frameAgenda_BTs_1.setMaximumSize(QSize(125, 16777215))
        self.frameAgenda_BTs_1.setStyleSheet(u"border-radius:20px;")
        self.frameAgenda_BTs_1.setFrameShape(QFrame.StyledPanel)
        self.frameAgenda_BTs_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameAgenda_BTs_1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.fCadastro_Left_Opened = QFrame(self.frameAgenda_BTs_1)
        self.fCadastro_Left_Opened.setObjectName(u"fCadastro_Left_Opened")
        sizePolicy3.setHeightForWidth(self.fCadastro_Left_Opened.sizePolicy().hasHeightForWidth())
        self.fCadastro_Left_Opened.setSizePolicy(sizePolicy3)
        self.fCadastro_Left_Opened.setMinimumSize(QSize(60, 500))
        self.fCadastro_Left_Opened.setMaximumSize(QSize(0, 16777215))
        self.fCadastro_Left_Opened.setStyleSheet(u"")
        self.fCadastro_Left_Opened.setFrameShape(QFrame.StyledPanel)
        self.fCadastro_Left_Opened.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.fCadastro_Left_Opened)
        self.verticalLayout_55.setSpacing(5)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(5, 5, 5, 0)
        self.fCad_Left_01 = QFrame(self.fCadastro_Left_Opened)
        self.fCad_Left_01.setObjectName(u"fCad_Left_01")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(50)
        sizePolicy4.setVerticalStretch(50)
        sizePolicy4.setHeightForWidth(self.fCad_Left_01.sizePolicy().hasHeightForWidth())
        self.fCad_Left_01.setSizePolicy(sizePolicy4)
        self.fCad_Left_01.setMinimumSize(QSize(0, 0))
        self.fCad_Left_01.setMaximumSize(QSize(50, 50))
        self.fCad_Left_01.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_01.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.fCad_Left_01)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_12 = QFrame(self.fCad_Left_01)
        self.fCad_Left_12.setObjectName(u"fCad_Left_12")
        sizePolicy4.setHeightForWidth(self.fCad_Left_12.sizePolicy().hasHeightForWidth())
        self.fCad_Left_12.setSizePolicy(sizePolicy4)
        self.fCad_Left_12.setMinimumSize(QSize(0, 0))
        self.fCad_Left_12.setMaximumSize(QSize(0, 50))
        self.fCad_Left_12.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.fCad_Left_12)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_01 = QPushButton(self.fCad_Left_12)
        self.btCad_Left_LIG_01.setObjectName(u"btCad_Left_LIG_01")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btCad_Left_LIG_01.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_01.setSizePolicy(sizePolicy5)
        self.btCad_Left_LIG_01.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_01.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_01.setStyleSheet(u"\n"
"QPushButton{\n"
"\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Data_3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Data_2.png);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_69.addWidget(self.btCad_Left_LIG_01)


        self.horizontalLayout_46.addWidget(self.fCad_Left_12)

        self.fCad_Left_11 = QFrame(self.fCad_Left_01)
        self.fCad_Left_11.setObjectName(u"fCad_Left_11")
        sizePolicy4.setHeightForWidth(self.fCad_Left_11.sizePolicy().hasHeightForWidth())
        self.fCad_Left_11.setSizePolicy(sizePolicy4)
        self.fCad_Left_11.setMinimumSize(QSize(40, 0))
        self.fCad_Left_11.setMaximumSize(QSize(0, 50))
        self.fCad_Left_11.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.fCad_Left_11)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_01 = QPushButton(self.fCad_Left_11)
        self.btCad_Left_DESL_01.setObjectName(u"btCad_Left_DESL_01")
        sizePolicy5.setHeightForWidth(self.btCad_Left_DESL_01.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_01.setSizePolicy(sizePolicy5)
        self.btCad_Left_DESL_01.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_01.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_01.setStyleSheet(u"\n"
"QPushButton{\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Data_1.png);\n"
"border:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Data_2.png);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_68.addWidget(self.btCad_Left_DESL_01)


        self.horizontalLayout_46.addWidget(self.fCad_Left_11)


        self.verticalLayout_55.addWidget(self.fCad_Left_01)

        self.fCad_Left_02 = QFrame(self.fCadastro_Left_Opened)
        self.fCad_Left_02.setObjectName(u"fCad_Left_02")
        sizePolicy4.setHeightForWidth(self.fCad_Left_02.sizePolicy().hasHeightForWidth())
        self.fCad_Left_02.setSizePolicy(sizePolicy4)
        self.fCad_Left_02.setMinimumSize(QSize(0, 0))
        self.fCad_Left_02.setMaximumSize(QSize(50, 50))
        self.fCad_Left_02.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_02.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.fCad_Left_02)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_22 = QFrame(self.fCad_Left_02)
        self.fCad_Left_22.setObjectName(u"fCad_Left_22")
        sizePolicy4.setHeightForWidth(self.fCad_Left_22.sizePolicy().hasHeightForWidth())
        self.fCad_Left_22.setSizePolicy(sizePolicy4)
        self.fCad_Left_22.setMinimumSize(QSize(0, 0))
        self.fCad_Left_22.setMaximumSize(QSize(0, 50))
        self.fCad_Left_22.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.fCad_Left_22)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_02 = QPushButton(self.fCad_Left_22)
        self.btCad_Left_LIG_02.setObjectName(u"btCad_Left_LIG_02")
        sizePolicy5.setHeightForWidth(self.btCad_Left_LIG_02.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_02.setSizePolicy(sizePolicy5)
        self.btCad_Left_LIG_02.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_02.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_02.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Clock_3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Clock_2.png);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_70.addWidget(self.btCad_Left_LIG_02)


        self.horizontalLayout_55.addWidget(self.fCad_Left_22)

        self.fCad_Left_21 = QFrame(self.fCad_Left_02)
        self.fCad_Left_21.setObjectName(u"fCad_Left_21")
        sizePolicy4.setHeightForWidth(self.fCad_Left_21.sizePolicy().hasHeightForWidth())
        self.fCad_Left_21.setSizePolicy(sizePolicy4)
        self.fCad_Left_21.setMinimumSize(QSize(40, 0))
        self.fCad_Left_21.setMaximumSize(QSize(0, 50))
        self.fCad_Left_21.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.fCad_Left_21)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_02 = QPushButton(self.fCad_Left_21)
        self.btCad_Left_DESL_02.setObjectName(u"btCad_Left_DESL_02")
        sizePolicy5.setHeightForWidth(self.btCad_Left_DESL_02.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_02.setSizePolicy(sizePolicy5)
        self.btCad_Left_DESL_02.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_02.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_02.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Clock_1.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Clock_2.png);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_71.addWidget(self.btCad_Left_DESL_02)


        self.horizontalLayout_55.addWidget(self.fCad_Left_21)


        self.verticalLayout_55.addWidget(self.fCad_Left_02)

        self.fCad_Left_3 = QFrame(self.fCadastro_Left_Opened)
        self.fCad_Left_3.setObjectName(u"fCad_Left_3")
        sizePolicy4.setHeightForWidth(self.fCad_Left_3.sizePolicy().hasHeightForWidth())
        self.fCad_Left_3.setSizePolicy(sizePolicy4)
        self.fCad_Left_3.setMinimumSize(QSize(0, 0))
        self.fCad_Left_3.setMaximumSize(QSize(50, 50))
        self.fCad_Left_3.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.fCad_Left_3)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_32 = QFrame(self.fCad_Left_3)
        self.fCad_Left_32.setObjectName(u"fCad_Left_32")
        sizePolicy4.setHeightForWidth(self.fCad_Left_32.sizePolicy().hasHeightForWidth())
        self.fCad_Left_32.setSizePolicy(sizePolicy4)
        self.fCad_Left_32.setMinimumSize(QSize(0, 0))
        self.fCad_Left_32.setMaximumSize(QSize(0, 50))
        self.fCad_Left_32.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.fCad_Left_32)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_05 = QPushButton(self.fCad_Left_32)
        self.btCad_Left_LIG_05.setObjectName(u"btCad_Left_LIG_05")
        sizePolicy5.setHeightForWidth(self.btCad_Left_LIG_05.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_05.setSizePolicy(sizePolicy5)
        self.btCad_Left_LIG_05.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_05.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_05.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Find_3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icon_Find_2.png);\n"
"}")

        self.horizontalLayout_75.addWidget(self.btCad_Left_LIG_05)


        self.horizontalLayout_74.addWidget(self.fCad_Left_32)

        self.fCad_Left_31 = QFrame(self.fCad_Left_3)
        self.fCad_Left_31.setObjectName(u"fCad_Left_31")
        sizePolicy4.setHeightForWidth(self.fCad_Left_31.sizePolicy().hasHeightForWidth())
        self.fCad_Left_31.setSizePolicy(sizePolicy4)
        self.fCad_Left_31.setMinimumSize(QSize(40, 0))
        self.fCad_Left_31.setMaximumSize(QSize(0, 50))
        self.fCad_Left_31.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.fCad_Left_31)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_03 = QPushButton(self.fCad_Left_31)
        self.btCad_Left_DESL_03.setObjectName(u"btCad_Left_DESL_03")
        sizePolicy5.setHeightForWidth(self.btCad_Left_DESL_03.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_03.setSizePolicy(sizePolicy5)
        self.btCad_Left_DESL_03.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_03.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_03.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Find_1.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Find_2.png);\n"
"}")

        self.horizontalLayout_76.addWidget(self.btCad_Left_DESL_03)


        self.horizontalLayout_74.addWidget(self.fCad_Left_31)


        self.verticalLayout_55.addWidget(self.fCad_Left_3)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_11)


        self.horizontalLayout_2.addWidget(self.fCadastro_Left_Opened)

        self.frameAgenda_Left_2 = QFrame(self.frameAgenda_BTs_1)
        self.frameAgenda_Left_2.setObjectName(u"frameAgenda_Left_2")
        sizePolicy3.setHeightForWidth(self.frameAgenda_Left_2.sizePolicy().hasHeightForWidth())
        self.frameAgenda_Left_2.setSizePolicy(sizePolicy3)
        self.frameAgenda_Left_2.setMinimumSize(QSize(60, 0))
        self.frameAgenda_Left_2.setMaximumSize(QSize(0, 16777215))
        self.frameAgenda_Left_2.setStyleSheet(u"border-radius:20px;\n"
"")
        self.frameAgenda_Left_2.setFrameShape(QFrame.StyledPanel)
        self.frameAgenda_Left_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frameAgenda_Left_2)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.BT_Agenda_Left_1 = QPushButton(self.frameAgenda_Left_2)
        self.BT_Agenda_Left_1.setObjectName(u"BT_Agenda_Left_1")
        self.BT_Agenda_Left_1.setMinimumSize(QSize(40, 50))
        self.BT_Agenda_Left_1.setMaximumSize(QSize(0, 95))
        self.BT_Agenda_Left_1.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_RIGHT.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-image: url(:/Bts/Icons/BT_s/Icon_RIGHT_2.png);\n"
"}")

        self.verticalLayout_53.addWidget(self.BT_Agenda_Left_1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_19)


        self.horizontalLayout_2.addWidget(self.frameAgenda_Left_2)

        self.frameAgenda_Left_3 = QFrame(self.frameAgenda_BTs_1)
        self.frameAgenda_Left_3.setObjectName(u"frameAgenda_Left_3")
        sizePolicy3.setHeightForWidth(self.frameAgenda_Left_3.sizePolicy().hasHeightForWidth())
        self.frameAgenda_Left_3.setSizePolicy(sizePolicy3)
        self.frameAgenda_Left_3.setMinimumSize(QSize(0, 0))
        self.frameAgenda_Left_3.setMaximumSize(QSize(0, 16777215))
        self.frameAgenda_Left_3.setStyleSheet(u"border-radius:20px;\n"
"")
        self.frameAgenda_Left_3.setFrameShape(QFrame.StyledPanel)
        self.frameAgenda_Left_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frameAgenda_Left_3)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.BT_Agenda_Left_2 = QPushButton(self.frameAgenda_Left_3)
        self.BT_Agenda_Left_2.setObjectName(u"BT_Agenda_Left_2")
        self.BT_Agenda_Left_2.setMinimumSize(QSize(40, 50))
        self.BT_Agenda_Left_2.setMaximumSize(QSize(0, 95))
        self.BT_Agenda_Left_2.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_LEFT_2.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_LEFT_1.png);\n"
"}")

        self.verticalLayout_66.addWidget(self.BT_Agenda_Left_2)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_66.addItem(self.verticalSpacer_18)


        self.horizontalLayout_2.addWidget(self.frameAgenda_Left_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.gridLayout_2.addWidget(self.frameAgenda_BTs_1, 0, 0, 1, 1)


        self.retranslateUi(Form_Agenda)

        self.Tbox_Agenda.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form_Agenda)
    # setupUi

    def retranslateUi(self, Form_Agenda):
        Form_Agenda.setWindowTitle(QCoreApplication.translate("Form_Agenda", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form_Agenda", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_ControleDeAgenda.png\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form_Agenda", u"<html><head/><body><p align=\"center\"><img src=\":/Backgrounds/Icons/Logos/Icon_Menu2.png\"/></p></body></html>", None))
        self.BT_Consultar_Agenda.setText(QCoreApplication.translate("Form_Agenda", u"Consultar Agenda", None))
        self.label_26.setText(QCoreApplication.translate("Form_Agenda", u"<html><head/><body><p align=\"center\">M\u00eas</p></body></html>", None))
        self.radioButton.setText(QCoreApplication.translate("Form_Agenda", u"Hoje", None))
        self.label_27.setText(QCoreApplication.translate("Form_Agenda", u"<html><head/><body><p align=\"center\">Dia</p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("Form_Agenda", u"<html><head/><body><p align=\"center\">Ano</p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_Agenda", u"Paciente", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_Agenda", u"Procedimento", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_Agenda", u"Plano_de_Saude", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_Agenda", u"Categoria", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_Agenda", u"Pagamento", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_Agenda", u"8:00", None));
        ___qtablewidgetitem6 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_Agenda", u"8:30", None));
        ___qtablewidgetitem7 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_Agenda", u"9:00", None));
        ___qtablewidgetitem8 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_Agenda", u"9:30", None));
        ___qtablewidgetitem9 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_Agenda", u"10:00", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form_Agenda", u"10:30", None));
        ___qtablewidgetitem11 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form_Agenda", u"11:00", None));
        ___qtablewidgetitem12 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form_Agenda", u"11:30", None));
        ___qtablewidgetitem13 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form_Agenda", u"11:00", None));
        ___qtablewidgetitem14 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form_Agenda", u"12:00", None));
        ___qtablewidgetitem15 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form_Agenda", u"13:00", None));
        ___qtablewidgetitem16 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form_Agenda", u"13:30", None));
        ___qtablewidgetitem17 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form_Agenda", u"14:00", None));
        ___qtablewidgetitem18 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form_Agenda", u"14:30", None));
        ___qtablewidgetitem19 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form_Agenda", u"15:00", None));
        ___qtablewidgetitem20 = self.tableWidget_2.verticalHeaderItem(15)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form_Agenda", u"15:30", None));
        ___qtablewidgetitem21 = self.tableWidget_2.verticalHeaderItem(16)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form_Agenda", u"16:00", None));
        ___qtablewidgetitem22 = self.tableWidget_2.verticalHeaderItem(17)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form_Agenda", u"16:30", None));
        ___qtablewidgetitem23 = self.tableWidget_2.verticalHeaderItem(18)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form_Agenda", u"17:00", None));
        ___qtablewidgetitem24 = self.tableWidget_2.verticalHeaderItem(19)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form_Agenda", u"17:30", None));
        ___qtablewidgetitem25 = self.tableWidget_2.verticalHeaderItem(20)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form_Agenda", u"18:00", None));
        ___qtablewidgetitem26 = self.tableWidget_2.verticalHeaderItem(21)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form_Agenda", u"18:30", None));
        ___qtablewidgetitem27 = self.tableWidget_2.verticalHeaderItem(22)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form_Agenda", u"19:00", None));
        ___qtablewidgetitem28 = self.tableWidget_2.verticalHeaderItem(23)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form_Agenda", u"19:30", None));
        ___qtablewidgetitem29 = self.tableWidget_2.verticalHeaderItem(24)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Form_Agenda", u"20:00", None));
        ___qtablewidgetitem30 = self.tableWidget_2.verticalHeaderItem(25)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Form_Agenda", u"20:30", None));
        self.BT_Medicamentos_4.setText(QCoreApplication.translate("Form_Agenda", u"Gerar aviso", None))
        self.BT_Medicamentos_6.setText(QCoreApplication.translate("Form_Agenda", u"Gerar PDF", None))
        self.btCad_Left_LIG_01.setText("")
        self.btCad_Left_DESL_01.setText("")
        self.btCad_Left_LIG_02.setText("")
        self.btCad_Left_DESL_02.setText("")
        self.btCad_Left_LIG_05.setText("")
        self.btCad_Left_DESL_03.setText("")
        self.BT_Agenda_Left_1.setText("")
        self.BT_Agenda_Left_2.setText("")
    # retranslateUi

