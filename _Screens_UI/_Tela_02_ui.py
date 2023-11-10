# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_Tela_02.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBox,
    QToolButton, QVBoxLayout, QWidget)
import Background_rc
import Infos_rc
import BT_s_rc
import Logo_rc
import Title_rc

class Ui_Tela_Inicial(object):
    def setupUi(self, Tela_Inicial):
        if not Tela_Inicial.objectName():
            Tela_Inicial.setObjectName(u"Tela_Inicial")
        Tela_Inicial.resize(1000, 800)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tela_Inicial.sizePolicy().hasHeightForWidth())
        Tela_Inicial.setSizePolicy(sizePolicy)
        Tela_Inicial.setMinimumSize(QSize(1000, 800))
        Tela_Inicial.setMaximumSize(QSize(1000, 859))
        font = QFont()
        font.setFamilies([u"Lucida Calligraphy"])
        Tela_Inicial.setFont(font)
        Tela_Inicial.setStyleSheet(u"")
        self.centralwidget = QWidget(Tela_Inicial)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(900, 0))
        self.centralwidget.setMaximumSize(QSize(1100, 16777215))
        self.centralwidget.setStyleSheet(u"background-color: rgb(193, 237, 255);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Left_Container = QFrame(self.centralwidget)
        self.Left_Container.setObjectName(u"Left_Container")
        sizePolicy.setHeightForWidth(self.Left_Container.sizePolicy().hasHeightForWidth())
        self.Left_Container.setSizePolicy(sizePolicy)
        self.Left_Container.setMinimumSize(QSize(200, 0))
        self.Left_Container.setMaximumSize(QSize(0, 16777215))
        self.Left_Container.setFrameShape(QFrame.StyledPanel)
        self.Left_Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Left_Container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 9, 0, 9)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.frame_5 = QFrame(self.Left_Container)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(200, 150))
        self.frame_5.setMaximumSize(QSize(200, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 9, -1, -1)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)

        self.verticalLayout_20.addWidget(self.label_2)

        self.widget_5 = QWidget(self.frame_5)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QToolBox{\n"
"text-align: left;	\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"border-radius:10px;\n"
"text-align: left;\n"
"background-image: url(:/BackGround/Icons/Backgrounds/Sorriso.jpg);\n"
"color: rgb(206, 255, 254);\n"
"}\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.widget_5)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy2)
        self.toolBox.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setFamilies([u"Lucida Calligraphy"])
        font1.setPointSize(10)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.toolBox.setFont(font1)
        self.toolBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBox.setMouseTracking(False)
        self.toolBox.setTabletTracking(False)
        self.toolBox.setStyleSheet(u"QPushButton:{\n"
"color: rgb(255, 255, 255);\n"
"border-image: url(:/BackGround/Icons/Backgrounds/Sorriso_2.jpg);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(149, 149, 149);\n"
"border:15px;\n"
"}\n"
"")
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.toolBox.setFrameShadow(QFrame.Sunken)
        self.Tbox_Atendimento = QWidget()
        self.Tbox_Atendimento.setObjectName(u"Tbox_Atendimento")
        self.Tbox_Atendimento.setGeometry(QRect(0, 0, 182, 336))
        self.Tbox_Atendimento.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.Tbox_Atendimento)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.BT_Cadastros = QPushButton(self.Tbox_Atendimento)
        self.BT_Cadastros.setObjectName(u"BT_Cadastros")
        self.BT_Cadastros.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        self.BT_Cadastros.setFont(font2)
        self.BT_Cadastros.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Cadastros.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_4.addWidget(self.BT_Cadastros)

        self.BT_Agendar = QPushButton(self.Tbox_Atendimento)
        self.BT_Agendar.setObjectName(u"BT_Agendar")
        self.BT_Agendar.setMinimumSize(QSize(0, 20))
        self.BT_Agendar.setSizeIncrement(QSize(0, 0))
        self.BT_Agendar.setFont(font2)
        self.BT_Agendar.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Agendar.setLayoutDirection(Qt.LeftToRight)
        self.BT_Agendar.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.BT_Agendar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.Tbox_Atendimento, u"Atendimento")
        self.Tbox_Medico = QWidget()
        self.Tbox_Medico.setObjectName(u"Tbox_Medico")
        self.Tbox_Medico.setGeometry(QRect(0, 0, 182, 336))
        self.verticalLayout_7 = QVBoxLayout(self.Tbox_Medico)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.BT_Pacientes = QPushButton(self.Tbox_Medico)
        self.BT_Pacientes.setObjectName(u"BT_Pacientes")
        self.BT_Pacientes.setMinimumSize(QSize(0, 20))
        self.BT_Pacientes.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.BT_Pacientes.setFont(font3)
        self.BT_Pacientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Pacientes.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_7.addWidget(self.BT_Pacientes)

        self.BT_Prontuarios = QPushButton(self.Tbox_Medico)
        self.BT_Prontuarios.setObjectName(u"BT_Prontuarios")
        self.BT_Prontuarios.setMinimumSize(QSize(0, 20))
        self.BT_Prontuarios.setFont(font2)
        self.BT_Prontuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Prontuarios.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_7.addWidget(self.BT_Prontuarios)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.Tbox_Medico, u"M\u00e9dico")
        self.Tbox_Financeito = QWidget()
        self.Tbox_Financeito.setObjectName(u"Tbox_Financeito")
        self.Tbox_Financeito.setGeometry(QRect(0, 0, 182, 336))
        self.verticalLayout_9 = QVBoxLayout(self.Tbox_Financeito)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.BT_Caixa = QPushButton(self.Tbox_Financeito)
        self.BT_Caixa.setObjectName(u"BT_Caixa")
        self.BT_Caixa.setMinimumSize(QSize(0, 20))
        self.BT_Caixa.setFont(font2)
        self.BT_Caixa.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Caixa.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")
        self.BT_Caixa.setIconSize(QSize(50, 50))

        self.verticalLayout_9.addWidget(self.BT_Caixa)

        self.BT_Receitas = QPushButton(self.Tbox_Financeito)
        self.BT_Receitas.setObjectName(u"BT_Receitas")
        self.BT_Receitas.setMinimumSize(QSize(0, 20))
        self.BT_Receitas.setFont(font2)
        self.BT_Receitas.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Receitas.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_9.addWidget(self.BT_Receitas)

        self.BT_Despesas = QPushButton(self.Tbox_Financeito)
        self.BT_Despesas.setObjectName(u"BT_Despesas")
        self.BT_Despesas.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_9.addWidget(self.BT_Despesas)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.toolBox.addItem(self.Tbox_Financeito, u"Financeiro")
        self.Tbox_Gestao = QWidget()
        self.Tbox_Gestao.setObjectName(u"Tbox_Gestao")
        self.Tbox_Gestao.setGeometry(QRect(0, 0, 182, 336))
        self.verticalLayout_8 = QVBoxLayout(self.Tbox_Gestao)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.BT_Estoques = QPushButton(self.Tbox_Gestao)
        self.BT_Estoques.setObjectName(u"BT_Estoques")
        self.BT_Estoques.setMinimumSize(QSize(0, 20))
        self.BT_Estoques.setFont(font2)
        self.BT_Estoques.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_8.addWidget(self.BT_Estoques)

        self.BT_Instrumentos = QPushButton(self.Tbox_Gestao)
        self.BT_Instrumentos.setObjectName(u"BT_Instrumentos")
        self.BT_Instrumentos.setMinimumSize(QSize(0, 20))
        self.BT_Instrumentos.setFont(font2)
        self.BT_Instrumentos.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Instrumentos.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_8.addWidget(self.BT_Instrumentos)

        self.BT_Medicamentos = QPushButton(self.Tbox_Gestao)
        self.BT_Medicamentos.setObjectName(u"BT_Medicamentos")
        self.BT_Medicamentos.setMinimumSize(QSize(0, 20))
        self.BT_Medicamentos.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_8.addWidget(self.BT_Medicamentos)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.Tbox_Gestao, u"Gest\u00e3o")
        self.Tbox_Convenios = QWidget()
        self.Tbox_Convenios.setObjectName(u"Tbox_Convenios")
        self.Tbox_Convenios.setGeometry(QRect(0, 0, 182, 336))
        self.verticalLayout_10 = QVBoxLayout(self.Tbox_Convenios)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.BT_instituicoes = QPushButton(self.Tbox_Convenios)
        self.BT_instituicoes.setObjectName(u"BT_instituicoes")
        self.BT_instituicoes.setMinimumSize(QSize(0, 20))
        self.BT_instituicoes.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_10.addWidget(self.BT_instituicoes)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.toolBox.addItem(self.Tbox_Convenios, u"Conv\u00eanios")
        self.Tbox_Analise = QWidget()
        self.Tbox_Analise.setObjectName(u"Tbox_Analise")
        self.Tbox_Analise.setGeometry(QRect(0, 0, 182, 336))
        self.verticalLayout_19 = QVBoxLayout(self.Tbox_Analise)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.BT_Analise1 = QPushButton(self.Tbox_Analise)
        self.BT_Analise1.setObjectName(u"BT_Analise1")
        self.BT_Analise1.setMinimumSize(QSize(0, 20))
        self.BT_Analise1.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_19.addWidget(self.BT_Analise1)

        self.BT_Analise2 = QPushButton(self.Tbox_Analise)
        self.BT_Analise2.setObjectName(u"BT_Analise2")
        self.BT_Analise2.setMinimumSize(QSize(0, 20))
        self.BT_Analise2.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_19.addWidget(self.BT_Analise2)

        self.BT_Analise3 = QPushButton(self.Tbox_Analise)
        self.BT_Analise3.setObjectName(u"BT_Analise3")
        self.BT_Analise3.setMinimumSize(QSize(0, 20))
        self.BT_Analise3.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout_19.addWidget(self.BT_Analise3)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_12)

        self.toolBox.addItem(self.Tbox_Analise, u"An\u00e1lise")
        self.Tbox_Sobre = QWidget()
        self.Tbox_Sobre.setObjectName(u"Tbox_Sobre")
        self.Tbox_Sobre.setGeometry(QRect(0, 0, 182, 336))
        self.verticalLayout = QVBoxLayout(self.Tbox_Sobre)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.BT_Home = QPushButton(self.Tbox_Sobre)
        self.BT_Home.setObjectName(u"BT_Home")
        self.BT_Home.setMinimumSize(QSize(0, 20))
        self.BT_Home.setFont(font2)
        self.BT_Home.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Home.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout.addWidget(self.BT_Home)

        self.BT_Info = QPushButton(self.Tbox_Sobre)
        self.BT_Info.setObjectName(u"BT_Info")
        self.BT_Info.setMinimumSize(QSize(0, 20))
        self.BT_Info.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/BackGround/Icons/Backgrounds/GreySorriso.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.verticalLayout.addWidget(self.BT_Info)

        self.LBL_Info = QLabel(self.Tbox_Sobre)
        self.LBL_Info.setObjectName(u"LBL_Info")

        self.verticalLayout.addWidget(self.LBL_Info)

        self.toolBox.addItem(self.Tbox_Sobre, u"Sobre")

        self.verticalLayout_16.addWidget(self.toolBox)


        self.verticalLayout_20.addWidget(self.widget_5)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.Left_Container)

        self.Right_Container = QFrame(self.centralwidget)
        self.Right_Container.setObjectName(u"Right_Container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Right_Container.sizePolicy().hasHeightForWidth())
        self.Right_Container.setSizePolicy(sizePolicy3)
        self.Right_Container.setMinimumSize(QSize(750, 300))
        self.Right_Container.setMaximumSize(QSize(1200, 16777215))
        self.Right_Container.setFrameShape(QFrame.StyledPanel)
        self.Right_Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.Right_Container)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.WID_Menu = QWidget(self.Right_Container)
        self.WID_Menu.setObjectName(u"WID_Menu")
        self.WID_Menu.setMaximumSize(QSize(16777215, 16777215))
        self.WID_Menu.setStyleSheet(u"\n"
"QPushButton:{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(149, 149, 149);\n"
"border:15px;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.WID_Menu)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.BT_Menu = QToolButton(self.WID_Menu)
        self.BT_Menu.setObjectName(u"BT_Menu")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.BT_Menu.sizePolicy().hasHeightForWidth())
        self.BT_Menu.setSizePolicy(sizePolicy4)
        self.BT_Menu.setMinimumSize(QSize(80, 60))
        self.BT_Menu.setStyleSheet(u"border:15px;\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/Logos/Icons/Logos/Icon_Menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_Menu.setIcon(icon)
        self.BT_Menu.setIconSize(QSize(80, 80))

        self.horizontalLayout_8.addWidget(self.BT_Menu)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.LBL_Logo_Clinica_Jansen = QLabel(self.WID_Menu)
        self.LBL_Logo_Clinica_Jansen.setObjectName(u"LBL_Logo_Clinica_Jansen")
        self.LBL_Logo_Clinica_Jansen.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.LBL_Logo_Clinica_Jansen.sizePolicy().hasHeightForWidth())
        self.LBL_Logo_Clinica_Jansen.setSizePolicy(sizePolicy5)
        self.LBL_Logo_Clinica_Jansen.setMinimumSize(QSize(1, 0))
        self.LBL_Logo_Clinica_Jansen.setStyleSheet(u"\n"
"border-radius:25px;")
        self.LBL_Logo_Clinica_Jansen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.LBL_Logo_Clinica_Jansen)


        self.verticalLayout_15.addWidget(self.WID_Menu)

        self.widget_3 = QWidget(self.Right_Container)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy6)
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.PAGES_Sistema = QStackedWidget(self.widget_3)
        self.PAGES_Sistema.setObjectName(u"PAGES_Sistema")
        self.PAGES_Sistema.setStyleSheet(u"")
        self.PAGE_Home = QWidget()
        self.PAGE_Home.setObjectName(u"PAGE_Home")
        self.gridLayout_3 = QGridLayout(self.PAGE_Home)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.PAGE_Home)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border-radius:32px;\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"\n"
"background-image: url(:/BackGround/Icons/Backgrounds/Sorriso.jpg);")

        self.horizontalLayout_6.addWidget(self.label)


        self.gridLayout_3.addWidget(self.widget, 0, 1, 1, 1)

        self.PAGES_Sistema.addWidget(self.PAGE_Home)
        self.PAGE_Cadastros = QWidget()
        self.PAGE_Cadastros.setObjectName(u"PAGE_Cadastros")
        self.horizontalLayout_54 = QHBoxLayout(self.PAGE_Cadastros)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.frame_45 = QFrame(self.PAGE_Cadastros)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(16777215, 16777215))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_45)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 250, 501, 311))

        self.horizontalLayout_54.addWidget(self.frame_45)

        self.PAGES_Sistema.addWidget(self.PAGE_Cadastros)
        self.PAGE_Prontuarios = QWidget()
        self.PAGE_Prontuarios.setObjectName(u"PAGE_Prontuarios")
        self.verticalLayout_5 = QVBoxLayout(self.PAGE_Prontuarios)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.LBL_GerenciarProntuarios = QLabel(self.PAGE_Prontuarios)
        self.LBL_GerenciarProntuarios.setObjectName(u"LBL_GerenciarProntuarios")
        self.LBL_GerenciarProntuarios.setStyleSheet(u"background-image: url(:/BackGround/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_5.addWidget(self.LBL_GerenciarProntuarios)

        self.widget_Prontuarios = QWidget(self.PAGE_Prontuarios)
        self.widget_Prontuarios.setObjectName(u"widget_Prontuarios")
        self.widget_Prontuarios.setMinimumSize(QSize(800, 0))
        self.widget_Prontuarios.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_Prontuarios)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.Tbox_Prontuarios = QStackedWidget(self.widget_Prontuarios)
        self.Tbox_Prontuarios.setObjectName(u"Tbox_Prontuarios")
        self.Tbox_Prontuarios.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.Tbox_ProntuariosPage1_2 = QWidget()
        self.Tbox_ProntuariosPage1_2.setObjectName(u"Tbox_ProntuariosPage1_2")
        self.horizontalLayout_2 = QHBoxLayout(self.Tbox_ProntuariosPage1_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.Tbox_ProntuariosPage1_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 500))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_21 = QFrame(self.frame_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"QFrame{\n"
"background-color: rgb(193, 237, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_21)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setFont(font)

        self.verticalLayout_2.addWidget(self.label_9)

        self.frame_36 = QFrame(self.frame_21)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 40))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_14 = QLabel(self.frame_36)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font)

        self.horizontalLayout_33.addWidget(self.label_14)

        self.label_13 = QLabel(self.frame_36)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(50, 30))
        self.label_13.setFont(font)

        self.horizontalLayout_33.addWidget(self.label_13)


        self.verticalLayout_2.addWidget(self.frame_36)

        self.frame_16 = QFrame(self.frame_21)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 40))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.comboBox_23 = QComboBox(self.frame_16)
        self.comboBox_23.setObjectName(u"comboBox_23")
        self.comboBox_23.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_9.addWidget(self.comboBox_23)

        self.comboBox_28 = QComboBox(self.frame_16)
        self.comboBox_28.setObjectName(u"comboBox_28")
        self.comboBox_28.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_9.addWidget(self.comboBox_28)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 40))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.comboBox_26 = QComboBox(self.frame_23)
        self.comboBox_26.setObjectName(u"comboBox_26")
        self.comboBox_26.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_17.addWidget(self.comboBox_26)

        self.comboBox_31 = QComboBox(self.frame_23)
        self.comboBox_31.setObjectName(u"comboBox_31")
        self.comboBox_31.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_17.addWidget(self.comboBox_31)


        self.verticalLayout_2.addWidget(self.frame_23)

        self.frame_27 = QFrame(self.frame_21)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 40))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.comboBox_37 = QComboBox(self.frame_27)
        self.comboBox_37.setObjectName(u"comboBox_37")
        self.comboBox_37.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_21.addWidget(self.comboBox_37)

        self.comboBox_38 = QComboBox(self.frame_27)
        self.comboBox_38.setObjectName(u"comboBox_38")
        self.comboBox_38.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_21.addWidget(self.comboBox_38)


        self.verticalLayout_2.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.frame_21)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 40))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.comboBox_35 = QComboBox(self.frame_26)
        self.comboBox_35.setObjectName(u"comboBox_35")
        self.comboBox_35.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_20.addWidget(self.comboBox_35)

        self.comboBox_36 = QComboBox(self.frame_26)
        self.comboBox_36.setObjectName(u"comboBox_36")
        self.comboBox_36.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_20.addWidget(self.comboBox_36)


        self.verticalLayout_2.addWidget(self.frame_26)

        self.frame_25 = QFrame(self.frame_21)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 40))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.comboBox_33 = QComboBox(self.frame_25)
        self.comboBox_33.setObjectName(u"comboBox_33")
        self.comboBox_33.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_19.addWidget(self.comboBox_33)

        self.comboBox_34 = QComboBox(self.frame_25)
        self.comboBox_34.setObjectName(u"comboBox_34")
        self.comboBox_34.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_19.addWidget(self.comboBox_34)


        self.verticalLayout_2.addWidget(self.frame_25)

        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 40))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.comboBox_27 = QComboBox(self.frame_24)
        self.comboBox_27.setObjectName(u"comboBox_27")
        self.comboBox_27.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_18.addWidget(self.comboBox_27)

        self.comboBox_32 = QComboBox(self.frame_24)
        self.comboBox_32.setObjectName(u"comboBox_32")
        self.comboBox_32.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_18.addWidget(self.comboBox_32)


        self.verticalLayout_2.addWidget(self.frame_24)

        self.frame_17 = QFrame(self.frame_21)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 40))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.comboBox_24 = QComboBox(self.frame_17)
        self.comboBox_24.setObjectName(u"comboBox_24")
        self.comboBox_24.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_15.addWidget(self.comboBox_24)

        self.comboBox_29 = QComboBox(self.frame_17)
        self.comboBox_29.setObjectName(u"comboBox_29")
        self.comboBox_29.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_15.addWidget(self.comboBox_29)


        self.verticalLayout_2.addWidget(self.frame_17)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 40))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.comboBox_25 = QComboBox(self.frame_22)
        self.comboBox_25.setObjectName(u"comboBox_25")
        self.comboBox_25.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_16.addWidget(self.comboBox_25)

        self.comboBox_30 = QComboBox(self.frame_22)
        self.comboBox_30.setObjectName(u"comboBox_30")
        self.comboBox_30.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_16.addWidget(self.comboBox_30)


        self.verticalLayout_2.addWidget(self.frame_22)

        self.label_11 = QLabel(self.frame_21)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.label_11)

        self.textEdit = QTextEdit(self.frame_21)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 150))
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout_11.addWidget(self.frame_21)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_11.addWidget(self.label_4)

        self.frame_28 = QFrame(self.frame_3)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"QFrame{\n"
"background-color: rgb(193, 237, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_28)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.frame_28)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_11.addWidget(self.label_10)

        self.frame_37 = QFrame(self.frame_28)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(16777215, 40))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_16 = QLabel(self.frame_37)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_34.addWidget(self.label_16)

        self.label_15 = QLabel(self.frame_37)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_34.addWidget(self.label_15)


        self.verticalLayout_11.addWidget(self.frame_37)

        self.frame_20 = QFrame(self.frame_28)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 40))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.comboBox_40 = QComboBox(self.frame_20)
        self.comboBox_40.setObjectName(u"comboBox_40")
        self.comboBox_40.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_22.addWidget(self.comboBox_40)

        self.comboBox_39 = QComboBox(self.frame_20)
        self.comboBox_39.setObjectName(u"comboBox_39")
        self.comboBox_39.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_22.addWidget(self.comboBox_39)


        self.verticalLayout_11.addWidget(self.frame_20)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 40))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.comboBox_42 = QComboBox(self.frame_29)
        self.comboBox_42.setObjectName(u"comboBox_42")
        self.comboBox_42.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_23.addWidget(self.comboBox_42)

        self.comboBox_41 = QComboBox(self.frame_29)
        self.comboBox_41.setObjectName(u"comboBox_41")
        self.comboBox_41.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_23.addWidget(self.comboBox_41)


        self.verticalLayout_11.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 40))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.comboBox_44 = QComboBox(self.frame_30)
        self.comboBox_44.setObjectName(u"comboBox_44")
        self.comboBox_44.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_24.addWidget(self.comboBox_44)

        self.comboBox_43 = QComboBox(self.frame_30)
        self.comboBox_43.setObjectName(u"comboBox_43")
        self.comboBox_43.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_24.addWidget(self.comboBox_43)


        self.verticalLayout_11.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 40))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.comboBox_46 = QComboBox(self.frame_31)
        self.comboBox_46.setObjectName(u"comboBox_46")
        self.comboBox_46.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_25.addWidget(self.comboBox_46)

        self.comboBox_45 = QComboBox(self.frame_31)
        self.comboBox_45.setObjectName(u"comboBox_45")
        self.comboBox_45.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_25.addWidget(self.comboBox_45)


        self.verticalLayout_11.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_28)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 40))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.comboBox_48 = QComboBox(self.frame_32)
        self.comboBox_48.setObjectName(u"comboBox_48")
        self.comboBox_48.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_26.addWidget(self.comboBox_48)

        self.comboBox_47 = QComboBox(self.frame_32)
        self.comboBox_47.setObjectName(u"comboBox_47")
        self.comboBox_47.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_26.addWidget(self.comboBox_47)


        self.verticalLayout_11.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_28)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 40))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.comboBox_50 = QComboBox(self.frame_33)
        self.comboBox_50.setObjectName(u"comboBox_50")
        self.comboBox_50.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_27.addWidget(self.comboBox_50)

        self.comboBox_49 = QComboBox(self.frame_33)
        self.comboBox_49.setObjectName(u"comboBox_49")
        self.comboBox_49.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_27.addWidget(self.comboBox_49)


        self.verticalLayout_11.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_28)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 40))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.comboBox_52 = QComboBox(self.frame_34)
        self.comboBox_52.setObjectName(u"comboBox_52")
        self.comboBox_52.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_28.addWidget(self.comboBox_52)

        self.comboBox_51 = QComboBox(self.frame_34)
        self.comboBox_51.setObjectName(u"comboBox_51")
        self.comboBox_51.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_28.addWidget(self.comboBox_51)


        self.verticalLayout_11.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_28)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 40))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.comboBox_54 = QComboBox(self.frame_35)
        self.comboBox_54.setObjectName(u"comboBox_54")
        self.comboBox_54.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_29.addWidget(self.comboBox_54)

        self.comboBox_53 = QComboBox(self.frame_35)
        self.comboBox_53.setObjectName(u"comboBox_53")
        self.comboBox_53.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_29.addWidget(self.comboBox_53)


        self.verticalLayout_11.addWidget(self.frame_35)

        self.label_12 = QLabel(self.frame_28)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_11.addWidget(self.label_12)

        self.textEdit_2 = QTextEdit(self.frame_28)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 150))
        self.textEdit_2.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_11.addWidget(self.textEdit_2)


        self.horizontalLayout_11.addWidget(self.frame_28)


        self.verticalLayout_18.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.Tbox_Prontuarios.addWidget(self.Tbox_ProntuariosPage1_2)
        self.Tbox_ProntuariosPage2_2 = QWidget()
        self.Tbox_ProntuariosPage2_2.setObjectName(u"Tbox_ProntuariosPage2_2")
        self.frame_Menu_Prontuario = QFrame(self.Tbox_ProntuariosPage2_2)
        self.frame_Menu_Prontuario.setObjectName(u"frame_Menu_Prontuario")
        self.frame_Menu_Prontuario.setGeometry(QRect(200, 0, 675, 587))
        self.frame_Menu_Prontuario.setMinimumSize(QSize(100, 0))
        self.frame_Menu_Prontuario.setMaximumSize(QSize(675, 16777215))
        self.frame_Menu_Prontuario.setFrameShape(QFrame.StyledPanel)
        self.frame_Menu_Prontuario.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_Menu_Prontuario)
        self.horizontalLayout_43.setSpacing(6)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_Menu_Prontuario)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"QFrame{\n"
"background-color: rgb(193, 237, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_43)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(9, 9, 261, 19))
        self.label_17.setMaximumSize(QSize(16777215, 30))
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setGeometry(QRect(9, 39, 261, 31))
        self.frame_44.setMaximumSize(QSize(16777215, 40))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_18 = QLabel(self.frame_44)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_35.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_44)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_35.addWidget(self.label_19)

        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setGeometry(QRect(9, 79, 261, 34))
        self.frame_46.setMaximumSize(QSize(16777215, 40))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.comboBox_55 = QComboBox(self.frame_46)
        self.comboBox_55.setObjectName(u"comboBox_55")
        self.comboBox_55.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_30.addWidget(self.comboBox_55)

        self.comboBox_56 = QComboBox(self.frame_46)
        self.comboBox_56.setObjectName(u"comboBox_56")
        self.comboBox_56.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_30.addWidget(self.comboBox_56)

        self.frame_48 = QFrame(self.frame_43)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setGeometry(QRect(9, 119, 261, 34))
        self.frame_48.setMaximumSize(QSize(16777215, 40))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.comboBox_57 = QComboBox(self.frame_48)
        self.comboBox_57.setObjectName(u"comboBox_57")
        self.comboBox_57.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_36.addWidget(self.comboBox_57)

        self.comboBox_58 = QComboBox(self.frame_48)
        self.comboBox_58.setObjectName(u"comboBox_58")
        self.comboBox_58.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_36.addWidget(self.comboBox_58)

        self.frame_49 = QFrame(self.frame_43)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setGeometry(QRect(9, 159, 261, 34))
        self.frame_49.setMaximumSize(QSize(16777215, 40))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.comboBox_59 = QComboBox(self.frame_49)
        self.comboBox_59.setObjectName(u"comboBox_59")
        self.comboBox_59.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_37.addWidget(self.comboBox_59)

        self.comboBox_60 = QComboBox(self.frame_49)
        self.comboBox_60.setObjectName(u"comboBox_60")
        self.comboBox_60.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_37.addWidget(self.comboBox_60)

        self.frame_51 = QFrame(self.frame_43)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setGeometry(QRect(9, 199, 261, 34))
        self.frame_51.setMaximumSize(QSize(16777215, 40))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.comboBox_61 = QComboBox(self.frame_51)
        self.comboBox_61.setObjectName(u"comboBox_61")
        self.comboBox_61.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_38.addWidget(self.comboBox_61)

        self.comboBox_62 = QComboBox(self.frame_51)
        self.comboBox_62.setObjectName(u"comboBox_62")
        self.comboBox_62.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_38.addWidget(self.comboBox_62)

        self.frame_52 = QFrame(self.frame_43)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setGeometry(QRect(9, 239, 261, 34))
        self.frame_52.setMaximumSize(QSize(16777215, 40))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.comboBox_63 = QComboBox(self.frame_52)
        self.comboBox_63.setObjectName(u"comboBox_63")
        self.comboBox_63.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_39.addWidget(self.comboBox_63)

        self.comboBox_64 = QComboBox(self.frame_52)
        self.comboBox_64.setObjectName(u"comboBox_64")
        self.comboBox_64.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_39.addWidget(self.comboBox_64)

        self.frame_53 = QFrame(self.frame_43)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setGeometry(QRect(9, 279, 261, 34))
        self.frame_53.setMaximumSize(QSize(16777215, 40))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.comboBox_65 = QComboBox(self.frame_53)
        self.comboBox_65.setObjectName(u"comboBox_65")
        self.comboBox_65.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_40.addWidget(self.comboBox_65)

        self.comboBox_66 = QComboBox(self.frame_53)
        self.comboBox_66.setObjectName(u"comboBox_66")
        self.comboBox_66.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_40.addWidget(self.comboBox_66)

        self.frame_54 = QFrame(self.frame_43)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setGeometry(QRect(9, 319, 261, 34))
        self.frame_54.setMaximumSize(QSize(16777215, 40))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.comboBox_67 = QComboBox(self.frame_54)
        self.comboBox_67.setObjectName(u"comboBox_67")
        self.comboBox_67.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_41.addWidget(self.comboBox_67)

        self.comboBox_68 = QComboBox(self.frame_54)
        self.comboBox_68.setObjectName(u"comboBox_68")
        self.comboBox_68.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_41.addWidget(self.comboBox_68)

        self.frame_56 = QFrame(self.frame_43)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setGeometry(QRect(9, 359, 261, 34))
        self.frame_56.setMaximumSize(QSize(16777215, 40))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.comboBox_69 = QComboBox(self.frame_56)
        self.comboBox_69.setObjectName(u"comboBox_69")
        self.comboBox_69.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_42.addWidget(self.comboBox_69)

        self.comboBox_70 = QComboBox(self.frame_56)
        self.comboBox_70.setObjectName(u"comboBox_70")
        self.comboBox_70.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_42.addWidget(self.comboBox_70)

        self.label_20 = QLabel(self.frame_43)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(200, 410, 71, 16))
        self.label_20.setMaximumSize(QSize(16777215, 30))
        self.textEdit_3 = QTextEdit(self.frame_43)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(9, 429, 314, 140))
        self.textEdit_3.setMaximumSize(QSize(16777215, 140))
        self.textEdit_3.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_43.addWidget(self.frame_43)

        self.frame_50 = QFrame(self.frame_Menu_Prontuario)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy)
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_50)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_50)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_41)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.tableWidget_5 = QTableWidget(self.frame_41)
        if (self.tableWidget_5.columnCount() < 4):
            self.tableWidget_5.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setMinimumSize(QSize(100, 200))
        self.tableWidget_5.setStyleSheet(u"QHeaderView::Section{\n"
"	background-color: rgb(0, 59, 179);\n"
"background-color: rgb(85, 170, 255);\n"
"font: 8pt \"Lucida Calligraphy\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(185, 219, 255);\n"
"color: rgb(0, 85, 255);\n"
"\n"
"}")

        self.verticalLayout_51.addWidget(self.tableWidget_5)


        self.verticalLayout_12.addWidget(self.frame_41)

        self.frame_40 = QFrame(self.frame_50)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_40)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.tableWidget_4 = QTableWidget(self.frame_40)
        if (self.tableWidget_4.columnCount() < 4):
            self.tableWidget_4.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMinimumSize(QSize(100, 50))
        self.tableWidget_4.setStyleSheet(u"QHeaderView::Section{\n"
"background-color: rgb(85, 170, 255);\n"
"font: 8pt \"Lucida Calligraphy\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(185, 219, 255);\n"
"color: rgb(0, 85, 255);\n"
"\n"
"}")

        self.verticalLayout_50.addWidget(self.tableWidget_4)


        self.verticalLayout_12.addWidget(self.frame_40)


        self.horizontalLayout_43.addWidget(self.frame_50)

        self.frame_38 = QFrame(self.frame_Menu_Prontuario)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy2.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy2)
        self.frame_38.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_38)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_43.addWidget(self.frame_38)

        self.frame_58 = QFrame(self.Tbox_ProntuariosPage2_2)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setGeometry(QRect(0, 0, 198, 587))
        self.frame_58.setStyleSheet(u"border-radius:20px;")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frameCadastroLEFT_4 = QFrame(self.frame_58)
        self.frameCadastroLEFT_4.setObjectName(u"frameCadastroLEFT_4")
        sizePolicy2.setHeightForWidth(self.frameCadastroLEFT_4.sizePolicy().hasHeightForWidth())
        self.frameCadastroLEFT_4.setSizePolicy(sizePolicy2)
        self.frameCadastroLEFT_4.setMinimumSize(QSize(60, 0))
        self.frameCadastroLEFT_4.setMaximumSize(QSize(0, 16777215))
        self.frameCadastroLEFT_4.setStyleSheet(u"border-radius:20px;\n"
"")
        self.frameCadastroLEFT_4.setFrameShape(QFrame.StyledPanel)
        self.frameCadastroLEFT_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frameCadastroLEFT_4)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.pushButton_14 = QPushButton(self.frameCadastroLEFT_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(40, 70))
        self.pushButton_14.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Backgrounds/Icons/BT_s/Icons_Finance.png);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"	background-image: url(:/Backgrounds/Icons/BT_s/Icons_Finance_2.png);\n"
"}")

        self.verticalLayout_59.addWidget(self.pushButton_14)


        self.horizontalLayout_48.addWidget(self.frameCadastroLEFT_4)

        self.frameCadastroLEFT_5 = QFrame(self.frame_58)
        self.frameCadastroLEFT_5.setObjectName(u"frameCadastroLEFT_5")
        sizePolicy2.setHeightForWidth(self.frameCadastroLEFT_5.sizePolicy().hasHeightForWidth())
        self.frameCadastroLEFT_5.setSizePolicy(sizePolicy2)
        self.frameCadastroLEFT_5.setMinimumSize(QSize(60, 0))
        self.frameCadastroLEFT_5.setMaximumSize(QSize(60, 16777215))
        self.frameCadastroLEFT_5.setStyleSheet(u"border-radius:20px;\n"
"")
        self.frameCadastroLEFT_5.setFrameShape(QFrame.StyledPanel)
        self.frameCadastroLEFT_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frameCadastroLEFT_5)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")

        self.horizontalLayout_48.addWidget(self.frameCadastroLEFT_5)

        self.frameCadastroLEFT_6 = QFrame(self.frame_58)
        self.frameCadastroLEFT_6.setObjectName(u"frameCadastroLEFT_6")
        sizePolicy2.setHeightForWidth(self.frameCadastroLEFT_6.sizePolicy().hasHeightForWidth())
        self.frameCadastroLEFT_6.setSizePolicy(sizePolicy2)
        self.frameCadastroLEFT_6.setMinimumSize(QSize(60, 0))
        self.frameCadastroLEFT_6.setMaximumSize(QSize(0, 16777215))
        self.frameCadastroLEFT_6.setStyleSheet(u"border-radius:20px;\n"
"")
        self.frameCadastroLEFT_6.setFrameShape(QFrame.StyledPanel)
        self.frameCadastroLEFT_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frameCadastroLEFT_6)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.BT_CadastroLEFT_4 = QPushButton(self.frameCadastroLEFT_6)
        self.BT_CadastroLEFT_4.setObjectName(u"BT_CadastroLEFT_4")
        self.BT_CadastroLEFT_4.setMaximumSize(QSize(40, 95))
        self.BT_CadastroLEFT_4.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"	background-image: url(:/newPrefix/Icons/BT_s/Icon_RIGHT_4.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/newPrefix/Icons/BT_s/Icon_RIGHT_3.png);\n"
"\n"
"}")

        self.verticalLayout_65.addWidget(self.BT_CadastroLEFT_4)


        self.horizontalLayout_48.addWidget(self.frameCadastroLEFT_6)

        self.Tbox_Prontuarios.addWidget(self.Tbox_ProntuariosPage2_2)
        self.Tbox_ProntuariosPage3_2 = QWidget()
        self.Tbox_ProntuariosPage3_2.setObjectName(u"Tbox_ProntuariosPage3_2")
        self.horizontalLayout_79 = QHBoxLayout(self.Tbox_ProntuariosPage3_2)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.frame = QFrame(self.Tbox_ProntuariosPage3_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")

        self.horizontalLayout_79.addWidget(self.frame)

        self.frame_11 = QFrame(self.Tbox_ProntuariosPage3_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 500))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_11)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_42 = QFrame(self.frame_11)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"QFrame{\n"
"background-color: rgb(193, 237, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_42)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_34 = QLabel(self.frame_42)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 30))
        self.label_34.setFont(font)

        self.verticalLayout_13.addWidget(self.label_34)

        self.frame_61 = QFrame(self.frame_42)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMaximumSize(QSize(16777215, 40))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_35 = QLabel(self.frame_61)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 30))
        self.label_35.setFont(font)

        self.horizontalLayout_80.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_61)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(50, 30))
        self.label_36.setFont(font)

        self.horizontalLayout_80.addWidget(self.label_36)


        self.verticalLayout_13.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_42)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMaximumSize(QSize(16777215, 40))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.comboBox_71 = QComboBox(self.frame_62)
        self.comboBox_71.setObjectName(u"comboBox_71")
        self.comboBox_71.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_81.addWidget(self.comboBox_71)

        self.comboBox_72 = QComboBox(self.frame_62)
        self.comboBox_72.setObjectName(u"comboBox_72")
        self.comboBox_72.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_81.addWidget(self.comboBox_72)


        self.verticalLayout_13.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_42)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMaximumSize(QSize(16777215, 40))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.comboBox_73 = QComboBox(self.frame_63)
        self.comboBox_73.setObjectName(u"comboBox_73")
        self.comboBox_73.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_82.addWidget(self.comboBox_73)

        self.comboBox_74 = QComboBox(self.frame_63)
        self.comboBox_74.setObjectName(u"comboBox_74")
        self.comboBox_74.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_82.addWidget(self.comboBox_74)


        self.verticalLayout_13.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_42)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMaximumSize(QSize(16777215, 40))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.comboBox_75 = QComboBox(self.frame_64)
        self.comboBox_75.setObjectName(u"comboBox_75")
        self.comboBox_75.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_83.addWidget(self.comboBox_75)

        self.comboBox_76 = QComboBox(self.frame_64)
        self.comboBox_76.setObjectName(u"comboBox_76")
        self.comboBox_76.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_83.addWidget(self.comboBox_76)


        self.verticalLayout_13.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.frame_42)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMaximumSize(QSize(16777215, 40))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.comboBox_77 = QComboBox(self.frame_65)
        self.comboBox_77.setObjectName(u"comboBox_77")
        self.comboBox_77.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_84.addWidget(self.comboBox_77)

        self.comboBox_78 = QComboBox(self.frame_65)
        self.comboBox_78.setObjectName(u"comboBox_78")
        self.comboBox_78.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_84.addWidget(self.comboBox_78)


        self.verticalLayout_13.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.frame_42)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMaximumSize(QSize(16777215, 40))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.comboBox_79 = QComboBox(self.frame_66)
        self.comboBox_79.setObjectName(u"comboBox_79")
        self.comboBox_79.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_85.addWidget(self.comboBox_79)

        self.comboBox_80 = QComboBox(self.frame_66)
        self.comboBox_80.setObjectName(u"comboBox_80")
        self.comboBox_80.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_85.addWidget(self.comboBox_80)


        self.verticalLayout_13.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_42)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMaximumSize(QSize(16777215, 40))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.comboBox_81 = QComboBox(self.frame_67)
        self.comboBox_81.setObjectName(u"comboBox_81")
        self.comboBox_81.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_86.addWidget(self.comboBox_81)

        self.comboBox_82 = QComboBox(self.frame_67)
        self.comboBox_82.setObjectName(u"comboBox_82")
        self.comboBox_82.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_86.addWidget(self.comboBox_82)


        self.verticalLayout_13.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_42)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMaximumSize(QSize(16777215, 40))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.comboBox_83 = QComboBox(self.frame_68)
        self.comboBox_83.setObjectName(u"comboBox_83")
        self.comboBox_83.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_87.addWidget(self.comboBox_83)

        self.comboBox_84 = QComboBox(self.frame_68)
        self.comboBox_84.setObjectName(u"comboBox_84")
        self.comboBox_84.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_87.addWidget(self.comboBox_84)


        self.verticalLayout_13.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.frame_42)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMaximumSize(QSize(16777215, 40))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.comboBox_85 = QComboBox(self.frame_69)
        self.comboBox_85.setObjectName(u"comboBox_85")
        self.comboBox_85.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_88.addWidget(self.comboBox_85)

        self.comboBox_86 = QComboBox(self.frame_69)
        self.comboBox_86.setObjectName(u"comboBox_86")
        self.comboBox_86.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_88.addWidget(self.comboBox_86)


        self.verticalLayout_13.addWidget(self.frame_69)

        self.label_37 = QLabel(self.frame_42)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_13.addWidget(self.label_37)

        self.textEdit_4 = QTextEdit(self.frame_42)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(16777215, 150))
        self.textEdit_4.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.textEdit_4)


        self.horizontalLayout_32.addWidget(self.frame_42)

        self.label_38 = QLabel(self.frame_11)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_32.addWidget(self.label_38)

        self.frame_70 = QFrame(self.frame_11)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setStyleSheet(u"QFrame{\n"
"background-color: rgb(193, 237, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_70)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_39 = QLabel(self.frame_70)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_52.addWidget(self.label_39)

        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMaximumSize(QSize(16777215, 40))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.label_40 = QLabel(self.frame_71)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_89.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_71)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_89.addWidget(self.label_41)


        self.verticalLayout_52.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.frame_70)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMaximumSize(QSize(16777215, 40))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.comboBox_87 = QComboBox(self.frame_72)
        self.comboBox_87.setObjectName(u"comboBox_87")
        self.comboBox_87.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_90.addWidget(self.comboBox_87)

        self.comboBox_88 = QComboBox(self.frame_72)
        self.comboBox_88.setObjectName(u"comboBox_88")
        self.comboBox_88.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_90.addWidget(self.comboBox_88)


        self.verticalLayout_52.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_70)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMaximumSize(QSize(16777215, 40))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.comboBox_89 = QComboBox(self.frame_73)
        self.comboBox_89.setObjectName(u"comboBox_89")
        self.comboBox_89.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_91.addWidget(self.comboBox_89)

        self.comboBox_90 = QComboBox(self.frame_73)
        self.comboBox_90.setObjectName(u"comboBox_90")
        self.comboBox_90.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_91.addWidget(self.comboBox_90)


        self.verticalLayout_52.addWidget(self.frame_73)

        self.frame_74 = QFrame(self.frame_70)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMaximumSize(QSize(16777215, 40))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.comboBox_91 = QComboBox(self.frame_74)
        self.comboBox_91.setObjectName(u"comboBox_91")
        self.comboBox_91.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_92.addWidget(self.comboBox_91)

        self.comboBox_92 = QComboBox(self.frame_74)
        self.comboBox_92.setObjectName(u"comboBox_92")
        self.comboBox_92.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_92.addWidget(self.comboBox_92)


        self.verticalLayout_52.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_70)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMaximumSize(QSize(16777215, 40))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.comboBox_93 = QComboBox(self.frame_75)
        self.comboBox_93.setObjectName(u"comboBox_93")
        self.comboBox_93.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_93.addWidget(self.comboBox_93)

        self.comboBox_94 = QComboBox(self.frame_75)
        self.comboBox_94.setObjectName(u"comboBox_94")
        self.comboBox_94.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_93.addWidget(self.comboBox_94)


        self.verticalLayout_52.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.frame_70)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMaximumSize(QSize(16777215, 40))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.comboBox_95 = QComboBox(self.frame_76)
        self.comboBox_95.setObjectName(u"comboBox_95")
        self.comboBox_95.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_94.addWidget(self.comboBox_95)

        self.comboBox_96 = QComboBox(self.frame_76)
        self.comboBox_96.setObjectName(u"comboBox_96")
        self.comboBox_96.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_94.addWidget(self.comboBox_96)


        self.verticalLayout_52.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.frame_70)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMaximumSize(QSize(16777215, 40))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.comboBox_97 = QComboBox(self.frame_77)
        self.comboBox_97.setObjectName(u"comboBox_97")
        self.comboBox_97.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_95.addWidget(self.comboBox_97)

        self.comboBox_98 = QComboBox(self.frame_77)
        self.comboBox_98.setObjectName(u"comboBox_98")
        self.comboBox_98.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_95.addWidget(self.comboBox_98)


        self.verticalLayout_52.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.frame_70)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMaximumSize(QSize(16777215, 40))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.comboBox_99 = QComboBox(self.frame_78)
        self.comboBox_99.setObjectName(u"comboBox_99")
        self.comboBox_99.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_96.addWidget(self.comboBox_99)

        self.comboBox_100 = QComboBox(self.frame_78)
        self.comboBox_100.setObjectName(u"comboBox_100")
        self.comboBox_100.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_96.addWidget(self.comboBox_100)


        self.verticalLayout_52.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_70)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMaximumSize(QSize(16777215, 40))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.comboBox_101 = QComboBox(self.frame_79)
        self.comboBox_101.setObjectName(u"comboBox_101")
        self.comboBox_101.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_97.addWidget(self.comboBox_101)

        self.comboBox_102 = QComboBox(self.frame_79)
        self.comboBox_102.setObjectName(u"comboBox_102")
        self.comboBox_102.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_97.addWidget(self.comboBox_102)


        self.verticalLayout_52.addWidget(self.frame_79)

        self.label_42 = QLabel(self.frame_70)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_52.addWidget(self.label_42)

        self.textEdit_5 = QTextEdit(self.frame_70)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(16777215, 150))
        self.textEdit_5.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_52.addWidget(self.textEdit_5)


        self.horizontalLayout_32.addWidget(self.frame_70)


        self.verticalLayout_49.addLayout(self.horizontalLayout_32)


        self.horizontalLayout_79.addWidget(self.frame_11)

        self.frame_2 = QFrame(self.Tbox_ProntuariosPage3_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")

        self.horizontalLayout_79.addWidget(self.frame_2)

        self.Tbox_Prontuarios.addWidget(self.Tbox_ProntuariosPage3_2)

        self.horizontalLayout_31.addWidget(self.Tbox_Prontuarios)


        self.verticalLayout_5.addWidget(self.widget_Prontuarios)

        self.PAGES_Sistema.addWidget(self.PAGE_Prontuarios)
        self.PAGE_Procedimentos = QWidget()
        self.PAGE_Procedimentos.setObjectName(u"PAGE_Procedimentos")
        self.verticalLayout_6 = QVBoxLayout(self.PAGE_Procedimentos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.LBL_GerenciarProncedimentos = QLabel(self.PAGE_Procedimentos)
        self.LBL_GerenciarProncedimentos.setObjectName(u"LBL_GerenciarProncedimentos")
        self.LBL_GerenciarProncedimentos.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_6.addWidget(self.LBL_GerenciarProncedimentos)

        self.widget_Proncedimentos = QWidget(self.PAGE_Procedimentos)
        self.widget_Proncedimentos.setObjectName(u"widget_Proncedimentos")
        self.widget_Proncedimentos.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_29 = QVBoxLayout(self.widget_Proncedimentos)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.Tbox_Proncedimentos = QToolBox(self.widget_Proncedimentos)
        self.Tbox_Proncedimentos.setObjectName(u"Tbox_Proncedimentos")
        self.Tbox_Proncedimentos.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_4 = QWidget()
        self.toolBox_2Page1_4.setObjectName(u"toolBox_2Page1_4")
        self.toolBox_2Page1_4.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_Proncedimentos.addItem(self.toolBox_2Page1_4, u"Page1")
        self.toolBox_2Page2_4 = QWidget()
        self.toolBox_2Page2_4.setObjectName(u"toolBox_2Page2_4")
        self.toolBox_2Page2_4.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_Proncedimentos.addItem(self.toolBox_2Page2_4, u"Page2")

        self.verticalLayout_29.addWidget(self.Tbox_Proncedimentos)


        self.verticalLayout_6.addWidget(self.widget_Proncedimentos)

        self.PAGES_Sistema.addWidget(self.PAGE_Procedimentos)
        self.PAGE_Caixa = QWidget()
        self.PAGE_Caixa.setObjectName(u"PAGE_Caixa")
        self.verticalLayout_23 = QVBoxLayout(self.PAGE_Caixa)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.LBL_FluxoCaixa = QLabel(self.PAGE_Caixa)
        self.LBL_FluxoCaixa.setObjectName(u"LBL_FluxoCaixa")
        self.LBL_FluxoCaixa.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_23.addWidget(self.LBL_FluxoCaixa)

        self.widget_Proncedimentos_2 = QWidget(self.PAGE_Caixa)
        self.widget_Proncedimentos_2.setObjectName(u"widget_Proncedimentos_2")
        self.widget_Proncedimentos_2.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_30 = QVBoxLayout(self.widget_Proncedimentos_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.Tbox_Proncedimentos_2 = QToolBox(self.widget_Proncedimentos_2)
        self.Tbox_Proncedimentos_2.setObjectName(u"Tbox_Proncedimentos_2")
        self.Tbox_Proncedimentos_2.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_5 = QWidget()
        self.toolBox_2Page1_5.setObjectName(u"toolBox_2Page1_5")
        self.toolBox_2Page1_5.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_Proncedimentos_2.addItem(self.toolBox_2Page1_5, u"Page1")
        self.toolBox_2Page2_5 = QWidget()
        self.toolBox_2Page2_5.setObjectName(u"toolBox_2Page2_5")
        self.toolBox_2Page2_5.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_Proncedimentos_2.addItem(self.toolBox_2Page2_5, u"Page2")

        self.verticalLayout_30.addWidget(self.Tbox_Proncedimentos_2)


        self.verticalLayout_23.addWidget(self.widget_Proncedimentos_2)

        self.PAGES_Sistema.addWidget(self.PAGE_Caixa)
        self.PAGE_Receitas = QWidget()
        self.PAGE_Receitas.setObjectName(u"PAGE_Receitas")
        self.verticalLayout_32 = QVBoxLayout(self.PAGE_Receitas)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.LBL_GerenciarReceitas = QLabel(self.PAGE_Receitas)
        self.LBL_GerenciarReceitas.setObjectName(u"LBL_GerenciarReceitas")
        self.LBL_GerenciarReceitas.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_32.addWidget(self.LBL_GerenciarReceitas)

        self.widget_GerenciarReceitas = QWidget(self.PAGE_Receitas)
        self.widget_GerenciarReceitas.setObjectName(u"widget_GerenciarReceitas")
        self.widget_GerenciarReceitas.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_31 = QVBoxLayout(self.widget_GerenciarReceitas)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.Tbox_GerenciarReceitas = QToolBox(self.widget_GerenciarReceitas)
        self.Tbox_GerenciarReceitas.setObjectName(u"Tbox_GerenciarReceitas")
        self.Tbox_GerenciarReceitas.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_6 = QWidget()
        self.toolBox_2Page1_6.setObjectName(u"toolBox_2Page1_6")
        self.toolBox_2Page1_6.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_GerenciarReceitas.addItem(self.toolBox_2Page1_6, u"Page1")
        self.toolBox_2Page2_6 = QWidget()
        self.toolBox_2Page2_6.setObjectName(u"toolBox_2Page2_6")
        self.toolBox_2Page2_6.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_GerenciarReceitas.addItem(self.toolBox_2Page2_6, u"Page2")

        self.verticalLayout_31.addWidget(self.Tbox_GerenciarReceitas)


        self.verticalLayout_32.addWidget(self.widget_GerenciarReceitas)

        self.PAGES_Sistema.addWidget(self.PAGE_Receitas)
        self.PAGE_Despesas = QWidget()
        self.PAGE_Despesas.setObjectName(u"PAGE_Despesas")
        self.verticalLayout_34 = QVBoxLayout(self.PAGE_Despesas)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.LBL_GerenciarDespesas = QLabel(self.PAGE_Despesas)
        self.LBL_GerenciarDespesas.setObjectName(u"LBL_GerenciarDespesas")
        self.LBL_GerenciarDespesas.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_34.addWidget(self.LBL_GerenciarDespesas)

        self.widget_GerenciarDespesas = QWidget(self.PAGE_Despesas)
        self.widget_GerenciarDespesas.setObjectName(u"widget_GerenciarDespesas")
        self.widget_GerenciarDespesas.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_33 = QVBoxLayout(self.widget_GerenciarDespesas)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.Tbox_GerenciarDespesas = QToolBox(self.widget_GerenciarDespesas)
        self.Tbox_GerenciarDespesas.setObjectName(u"Tbox_GerenciarDespesas")
        self.Tbox_GerenciarDespesas.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_7 = QWidget()
        self.toolBox_2Page1_7.setObjectName(u"toolBox_2Page1_7")
        self.toolBox_2Page1_7.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_GerenciarDespesas.addItem(self.toolBox_2Page1_7, u"Page1")
        self.toolBox_2Page2_7 = QWidget()
        self.toolBox_2Page2_7.setObjectName(u"toolBox_2Page2_7")
        self.toolBox_2Page2_7.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_GerenciarDespesas.addItem(self.toolBox_2Page2_7, u"Page2")

        self.verticalLayout_33.addWidget(self.Tbox_GerenciarDespesas)


        self.verticalLayout_34.addWidget(self.widget_GerenciarDespesas)

        self.PAGES_Sistema.addWidget(self.PAGE_Despesas)
        self.PAGE_Estoques = QWidget()
        self.PAGE_Estoques.setObjectName(u"PAGE_Estoques")
        self.verticalLayout_36 = QVBoxLayout(self.PAGE_Estoques)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.LBL_GerenciarEstoque = QLabel(self.PAGE_Estoques)
        self.LBL_GerenciarEstoque.setObjectName(u"LBL_GerenciarEstoque")
        self.LBL_GerenciarEstoque.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_36.addWidget(self.LBL_GerenciarEstoque)

        self.widget_GerenciarEstoque = QWidget(self.PAGE_Estoques)
        self.widget_GerenciarEstoque.setObjectName(u"widget_GerenciarEstoque")
        self.widget_GerenciarEstoque.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_35 = QVBoxLayout(self.widget_GerenciarEstoque)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.Tbox_GerenciarEstoque = QToolBox(self.widget_GerenciarEstoque)
        self.Tbox_GerenciarEstoque.setObjectName(u"Tbox_GerenciarEstoque")
        self.Tbox_GerenciarEstoque.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_8 = QWidget()
        self.toolBox_2Page1_8.setObjectName(u"toolBox_2Page1_8")
        self.toolBox_2Page1_8.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_GerenciarEstoque.addItem(self.toolBox_2Page1_8, u"Page1")
        self.toolBox_2Page2_8 = QWidget()
        self.toolBox_2Page2_8.setObjectName(u"toolBox_2Page2_8")
        self.toolBox_2Page2_8.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_GerenciarEstoque.addItem(self.toolBox_2Page2_8, u"Page2")

        self.verticalLayout_35.addWidget(self.Tbox_GerenciarEstoque)


        self.verticalLayout_36.addWidget(self.widget_GerenciarEstoque)

        self.PAGES_Sistema.addWidget(self.PAGE_Estoques)
        self.PAGE_Medicamentos = QWidget()
        self.PAGE_Medicamentos.setObjectName(u"PAGE_Medicamentos")
        self.verticalLayout_38 = QVBoxLayout(self.PAGE_Medicamentos)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.LBL_GerenciarMedicamentos = QLabel(self.PAGE_Medicamentos)
        self.LBL_GerenciarMedicamentos.setObjectName(u"LBL_GerenciarMedicamentos")
        self.LBL_GerenciarMedicamentos.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_38.addWidget(self.LBL_GerenciarMedicamentos)

        self.widget_GerenciarMedicamentos = QWidget(self.PAGE_Medicamentos)
        self.widget_GerenciarMedicamentos.setObjectName(u"widget_GerenciarMedicamentos")
        self.widget_GerenciarMedicamentos.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_37 = QVBoxLayout(self.widget_GerenciarMedicamentos)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.Tbox_GerenciarMedicamentos = QToolBox(self.widget_GerenciarMedicamentos)
        self.Tbox_GerenciarMedicamentos.setObjectName(u"Tbox_GerenciarMedicamentos")
        self.Tbox_GerenciarMedicamentos.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_9 = QWidget()
        self.toolBox_2Page1_9.setObjectName(u"toolBox_2Page1_9")
        self.toolBox_2Page1_9.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_GerenciarMedicamentos.addItem(self.toolBox_2Page1_9, u"Page1")
        self.toolBox_2Page2_9 = QWidget()
        self.toolBox_2Page2_9.setObjectName(u"toolBox_2Page2_9")
        self.toolBox_2Page2_9.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_GerenciarMedicamentos.addItem(self.toolBox_2Page2_9, u"Page2")

        self.verticalLayout_37.addWidget(self.Tbox_GerenciarMedicamentos)


        self.verticalLayout_38.addWidget(self.widget_GerenciarMedicamentos)

        self.PAGES_Sistema.addWidget(self.PAGE_Medicamentos)
        self.PAGE_Instituicoes = QWidget()
        self.PAGE_Instituicoes.setObjectName(u"PAGE_Instituicoes")
        self.verticalLayout_40 = QVBoxLayout(self.PAGE_Instituicoes)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.LBL_InstituicoesParceiras = QLabel(self.PAGE_Instituicoes)
        self.LBL_InstituicoesParceiras.setObjectName(u"LBL_InstituicoesParceiras")
        self.LBL_InstituicoesParceiras.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_40.addWidget(self.LBL_InstituicoesParceiras)

        self.widget_InstituicoesParceiras = QWidget(self.PAGE_Instituicoes)
        self.widget_InstituicoesParceiras.setObjectName(u"widget_InstituicoesParceiras")
        self.widget_InstituicoesParceiras.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_39 = QVBoxLayout(self.widget_InstituicoesParceiras)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.Tbox_InstituicoesParceiras = QToolBox(self.widget_InstituicoesParceiras)
        self.Tbox_InstituicoesParceiras.setObjectName(u"Tbox_InstituicoesParceiras")
        self.Tbox_InstituicoesParceiras.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_10 = QWidget()
        self.toolBox_2Page1_10.setObjectName(u"toolBox_2Page1_10")
        self.toolBox_2Page1_10.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_InstituicoesParceiras.addItem(self.toolBox_2Page1_10, u"Page1")
        self.toolBox_2Page2_10 = QWidget()
        self.toolBox_2Page2_10.setObjectName(u"toolBox_2Page2_10")
        self.toolBox_2Page2_10.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_InstituicoesParceiras.addItem(self.toolBox_2Page2_10, u"Page2")

        self.verticalLayout_39.addWidget(self.Tbox_InstituicoesParceiras)


        self.verticalLayout_40.addWidget(self.widget_InstituicoesParceiras)

        self.PAGES_Sistema.addWidget(self.PAGE_Instituicoes)
        self.PAGE_Analise_1 = QWidget()
        self.PAGE_Analise_1.setObjectName(u"PAGE_Analise_1")
        self.verticalLayout_42 = QVBoxLayout(self.PAGE_Analise_1)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.LBL_AnaliseDados1 = QLabel(self.PAGE_Analise_1)
        self.LBL_AnaliseDados1.setObjectName(u"LBL_AnaliseDados1")
        self.LBL_AnaliseDados1.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_42.addWidget(self.LBL_AnaliseDados1)

        self.widget_AnaliseDados1 = QWidget(self.PAGE_Analise_1)
        self.widget_AnaliseDados1.setObjectName(u"widget_AnaliseDados1")
        self.widget_AnaliseDados1.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_41 = QVBoxLayout(self.widget_AnaliseDados1)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.Tbox_AnaliseDados1 = QToolBox(self.widget_AnaliseDados1)
        self.Tbox_AnaliseDados1.setObjectName(u"Tbox_AnaliseDados1")
        self.Tbox_AnaliseDados1.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_11 = QWidget()
        self.toolBox_2Page1_11.setObjectName(u"toolBox_2Page1_11")
        self.toolBox_2Page1_11.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_AnaliseDados1.addItem(self.toolBox_2Page1_11, u"Page1")
        self.toolBox_2Page2_11 = QWidget()
        self.toolBox_2Page2_11.setObjectName(u"toolBox_2Page2_11")
        self.toolBox_2Page2_11.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_AnaliseDados1.addItem(self.toolBox_2Page2_11, u"Page2")

        self.verticalLayout_41.addWidget(self.Tbox_AnaliseDados1)


        self.verticalLayout_42.addWidget(self.widget_AnaliseDados1)

        self.PAGES_Sistema.addWidget(self.PAGE_Analise_1)
        self.PAGE_Analise_2 = QWidget()
        self.PAGE_Analise_2.setObjectName(u"PAGE_Analise_2")
        self.verticalLayout_44 = QVBoxLayout(self.PAGE_Analise_2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.LBL_AnaliseDados2 = QLabel(self.PAGE_Analise_2)
        self.LBL_AnaliseDados2.setObjectName(u"LBL_AnaliseDados2")
        self.LBL_AnaliseDados2.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_44.addWidget(self.LBL_AnaliseDados2)

        self.widget_AnaliseDados2 = QWidget(self.PAGE_Analise_2)
        self.widget_AnaliseDados2.setObjectName(u"widget_AnaliseDados2")
        self.widget_AnaliseDados2.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_43 = QVBoxLayout(self.widget_AnaliseDados2)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.Tbox_AnaliseDados2 = QToolBox(self.widget_AnaliseDados2)
        self.Tbox_AnaliseDados2.setObjectName(u"Tbox_AnaliseDados2")
        self.Tbox_AnaliseDados2.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_12 = QWidget()
        self.toolBox_2Page1_12.setObjectName(u"toolBox_2Page1_12")
        self.toolBox_2Page1_12.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_AnaliseDados2.addItem(self.toolBox_2Page1_12, u"Page1")
        self.toolBox_2Page2_12 = QWidget()
        self.toolBox_2Page2_12.setObjectName(u"toolBox_2Page2_12")
        self.toolBox_2Page2_12.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_AnaliseDados2.addItem(self.toolBox_2Page2_12, u"Page2")

        self.verticalLayout_43.addWidget(self.Tbox_AnaliseDados2)


        self.verticalLayout_44.addWidget(self.widget_AnaliseDados2)

        self.PAGES_Sistema.addWidget(self.PAGE_Analise_2)
        self.PAGE_Analise_3 = QWidget()
        self.PAGE_Analise_3.setObjectName(u"PAGE_Analise_3")
        self.verticalLayout_46 = QVBoxLayout(self.PAGE_Analise_3)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.LBL_AnaliseDados2_2 = QLabel(self.PAGE_Analise_3)
        self.LBL_AnaliseDados2_2.setObjectName(u"LBL_AnaliseDados2_2")
        self.LBL_AnaliseDados2_2.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_46.addWidget(self.LBL_AnaliseDados2_2)

        self.widget_AnaliseDados2_2 = QWidget(self.PAGE_Analise_3)
        self.widget_AnaliseDados2_2.setObjectName(u"widget_AnaliseDados2_2")
        self.widget_AnaliseDados2_2.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_45 = QVBoxLayout(self.widget_AnaliseDados2_2)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.Tbox_AnaliseDados2_2 = QToolBox(self.widget_AnaliseDados2_2)
        self.Tbox_AnaliseDados2_2.setObjectName(u"Tbox_AnaliseDados2_2")
        self.Tbox_AnaliseDados2_2.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_13 = QWidget()
        self.toolBox_2Page1_13.setObjectName(u"toolBox_2Page1_13")
        self.toolBox_2Page1_13.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_AnaliseDados2_2.addItem(self.toolBox_2Page1_13, u"Page1")
        self.toolBox_2Page2_13 = QWidget()
        self.toolBox_2Page2_13.setObjectName(u"toolBox_2Page2_13")
        self.toolBox_2Page2_13.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_AnaliseDados2_2.addItem(self.toolBox_2Page2_13, u"Page2")

        self.verticalLayout_45.addWidget(self.Tbox_AnaliseDados2_2)


        self.verticalLayout_46.addWidget(self.widget_AnaliseDados2_2)

        self.PAGES_Sistema.addWidget(self.PAGE_Analise_3)
        self.PAGE_Sobre = QWidget()
        self.PAGE_Sobre.setObjectName(u"PAGE_Sobre")
        self.verticalLayout_48 = QVBoxLayout(self.PAGE_Sobre)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.LBL_AnaliseDados3 = QLabel(self.PAGE_Sobre)
        self.LBL_AnaliseDados3.setObjectName(u"LBL_AnaliseDados3")
        self.LBL_AnaliseDados3.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_48.addWidget(self.LBL_AnaliseDados3)

        self.widget_AnaliseDados3 = QWidget(self.PAGE_Sobre)
        self.widget_AnaliseDados3.setObjectName(u"widget_AnaliseDados3")
        self.widget_AnaliseDados3.setStyleSheet(u"border-radius:25px;\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_47 = QVBoxLayout(self.widget_AnaliseDados3)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.Tbox_AnaliseDados3 = QToolBox(self.widget_AnaliseDados3)
        self.Tbox_AnaliseDados3.setObjectName(u"Tbox_AnaliseDados3")
        self.Tbox_AnaliseDados3.setStyleSheet(u"QToolBox::tab{\n"
"	\n"
"	font: 10pt \"Lucida Calligraphy\";\n"
"	border-radius:10px;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.toolBox_2Page1_14 = QWidget()
        self.toolBox_2Page1_14.setObjectName(u"toolBox_2Page1_14")
        self.toolBox_2Page1_14.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_AnaliseDados3.addItem(self.toolBox_2Page1_14, u"Page1")
        self.toolBox_2Page2_14 = QWidget()
        self.toolBox_2Page2_14.setObjectName(u"toolBox_2Page2_14")
        self.toolBox_2Page2_14.setGeometry(QRect(0, 0, 100, 30))
        self.Tbox_AnaliseDados3.addItem(self.toolBox_2Page2_14, u"Page2")

        self.verticalLayout_47.addWidget(self.Tbox_AnaliseDados3)


        self.verticalLayout_48.addWidget(self.widget_AnaliseDados3)

        self.PAGES_Sistema.addWidget(self.PAGE_Sobre)

        self.horizontalLayout_10.addWidget(self.PAGES_Sistema)


        self.verticalLayout_15.addWidget(self.widget_3)

        self.frame_Rodape = QFrame(self.Right_Container)
        self.frame_Rodape.setObjectName(u"frame_Rodape")
        self.frame_Rodape.setEnabled(True)
        self.frame_Rodape.setMinimumSize(QSize(100, 50))
        self.frame_Rodape.setFrameShape(QFrame.StyledPanel)
        self.frame_Rodape.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_Rodape)


        self.horizontalLayout.addWidget(self.Right_Container)

        Tela_Inicial.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.BT_Agendar, self.BT_Prontuarios)
        QWidget.setTabOrder(self.BT_Prontuarios, self.BT_Caixa)
        QWidget.setTabOrder(self.BT_Caixa, self.BT_Receitas)
        QWidget.setTabOrder(self.BT_Receitas, self.BT_Despesas)
        QWidget.setTabOrder(self.BT_Despesas, self.BT_Estoques)
        QWidget.setTabOrder(self.BT_Estoques, self.BT_Medicamentos)
        QWidget.setTabOrder(self.BT_Medicamentos, self.BT_instituicoes)
        QWidget.setTabOrder(self.BT_instituicoes, self.BT_Analise1)
        QWidget.setTabOrder(self.BT_Analise1, self.BT_Analise2)
        QWidget.setTabOrder(self.BT_Analise2, self.BT_Analise3)
        QWidget.setTabOrder(self.BT_Analise3, self.BT_Home)
        QWidget.setTabOrder(self.BT_Home, self.BT_Info)
        QWidget.setTabOrder(self.BT_Info, self.BT_Menu)
        QWidget.setTabOrder(self.BT_Menu, self.BT_Cadastros)
        QWidget.setTabOrder(self.BT_Cadastros, self.comboBox_23)
        QWidget.setTabOrder(self.comboBox_23, self.comboBox_28)
        QWidget.setTabOrder(self.comboBox_28, self.comboBox_26)
        QWidget.setTabOrder(self.comboBox_26, self.comboBox_31)
        QWidget.setTabOrder(self.comboBox_31, self.comboBox_37)
        QWidget.setTabOrder(self.comboBox_37, self.comboBox_38)
        QWidget.setTabOrder(self.comboBox_38, self.comboBox_35)
        QWidget.setTabOrder(self.comboBox_35, self.comboBox_36)
        QWidget.setTabOrder(self.comboBox_36, self.comboBox_33)
        QWidget.setTabOrder(self.comboBox_33, self.comboBox_34)
        QWidget.setTabOrder(self.comboBox_34, self.comboBox_27)
        QWidget.setTabOrder(self.comboBox_27, self.comboBox_32)
        QWidget.setTabOrder(self.comboBox_32, self.comboBox_24)
        QWidget.setTabOrder(self.comboBox_24, self.comboBox_29)
        QWidget.setTabOrder(self.comboBox_29, self.comboBox_25)
        QWidget.setTabOrder(self.comboBox_25, self.comboBox_30)
        QWidget.setTabOrder(self.comboBox_30, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.comboBox_40)
        QWidget.setTabOrder(self.comboBox_40, self.comboBox_39)
        QWidget.setTabOrder(self.comboBox_39, self.comboBox_42)
        QWidget.setTabOrder(self.comboBox_42, self.comboBox_41)
        QWidget.setTabOrder(self.comboBox_41, self.comboBox_44)
        QWidget.setTabOrder(self.comboBox_44, self.comboBox_43)
        QWidget.setTabOrder(self.comboBox_43, self.comboBox_46)
        QWidget.setTabOrder(self.comboBox_46, self.comboBox_45)
        QWidget.setTabOrder(self.comboBox_45, self.comboBox_48)
        QWidget.setTabOrder(self.comboBox_48, self.comboBox_47)
        QWidget.setTabOrder(self.comboBox_47, self.comboBox_50)
        QWidget.setTabOrder(self.comboBox_50, self.comboBox_49)
        QWidget.setTabOrder(self.comboBox_49, self.comboBox_52)
        QWidget.setTabOrder(self.comboBox_52, self.comboBox_51)
        QWidget.setTabOrder(self.comboBox_51, self.comboBox_54)
        QWidget.setTabOrder(self.comboBox_54, self.comboBox_53)
        QWidget.setTabOrder(self.comboBox_53, self.textEdit_2)
        QWidget.setTabOrder(self.textEdit_2, self.comboBox_55)
        QWidget.setTabOrder(self.comboBox_55, self.comboBox_56)
        QWidget.setTabOrder(self.comboBox_56, self.comboBox_57)
        QWidget.setTabOrder(self.comboBox_57, self.comboBox_58)
        QWidget.setTabOrder(self.comboBox_58, self.comboBox_59)
        QWidget.setTabOrder(self.comboBox_59, self.comboBox_60)
        QWidget.setTabOrder(self.comboBox_60, self.comboBox_61)
        QWidget.setTabOrder(self.comboBox_61, self.comboBox_62)
        QWidget.setTabOrder(self.comboBox_62, self.comboBox_63)
        QWidget.setTabOrder(self.comboBox_63, self.comboBox_64)
        QWidget.setTabOrder(self.comboBox_64, self.comboBox_65)
        QWidget.setTabOrder(self.comboBox_65, self.comboBox_66)
        QWidget.setTabOrder(self.comboBox_66, self.comboBox_67)
        QWidget.setTabOrder(self.comboBox_67, self.comboBox_68)
        QWidget.setTabOrder(self.comboBox_68, self.comboBox_69)
        QWidget.setTabOrder(self.comboBox_69, self.comboBox_70)
        QWidget.setTabOrder(self.comboBox_70, self.textEdit_3)
        QWidget.setTabOrder(self.textEdit_3, self.tableWidget_5)
        QWidget.setTabOrder(self.tableWidget_5, self.tableWidget_4)
        QWidget.setTabOrder(self.tableWidget_4, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.BT_CadastroLEFT_4)

        self.retranslateUi(Tela_Inicial)

        self.toolBox.setCurrentIndex(1)
        self.PAGES_Sistema.setCurrentIndex(1)
        self.Tbox_Prontuarios.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Tela_Inicial)
    # setupUi

    def retranslateUi(self, Tela_Inicial):
        Tela_Inicial.setWindowTitle(QCoreApplication.translate("Tela_Inicial", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Logos/Icons/Logos/Inicial_Cadastro.png\"/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolBox.setToolTip(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolBox.setWhatsThis(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.BT_Cadastros.setText(QCoreApplication.translate("Tela_Inicial", u"Cadastro", None))
        self.BT_Agendar.setText(QCoreApplication.translate("Tela_Inicial", u"Agenda", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Tbox_Atendimento), QCoreApplication.translate("Tela_Inicial", u"Atendimento", None))
        self.BT_Pacientes.setText(QCoreApplication.translate("Tela_Inicial", u"Pacientes", None))
        self.BT_Prontuarios.setText(QCoreApplication.translate("Tela_Inicial", u"Prontu\u00e1rios", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Tbox_Medico), QCoreApplication.translate("Tela_Inicial", u"M\u00e9dico", None))
        self.BT_Caixa.setText(QCoreApplication.translate("Tela_Inicial", u"Caixa", None))
        self.BT_Receitas.setText(QCoreApplication.translate("Tela_Inicial", u"Receitas", None))
        self.BT_Despesas.setText(QCoreApplication.translate("Tela_Inicial", u"Despesas", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Tbox_Financeito), QCoreApplication.translate("Tela_Inicial", u"Financeiro", None))
        self.BT_Estoques.setText(QCoreApplication.translate("Tela_Inicial", u"Estoque", None))
        self.BT_Instrumentos.setText(QCoreApplication.translate("Tela_Inicial", u"Instrumentos", None))
        self.BT_Medicamentos.setText(QCoreApplication.translate("Tela_Inicial", u"Medicamentos", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Tbox_Gestao), QCoreApplication.translate("Tela_Inicial", u"Gest\u00e3o", None))
        self.BT_instituicoes.setText(QCoreApplication.translate("Tela_Inicial", u"Institui\u00e7\u00f5es", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Tbox_Convenios), QCoreApplication.translate("Tela_Inicial", u"Conv\u00eanios", None))
        self.BT_Analise1.setText(QCoreApplication.translate("Tela_Inicial", u"An\u00e1lise 1", None))
        self.BT_Analise2.setText(QCoreApplication.translate("Tela_Inicial", u"An\u00e1lise 2", None))
        self.BT_Analise3.setText(QCoreApplication.translate("Tela_Inicial", u"An\u00e1lise 3", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Tbox_Analise), QCoreApplication.translate("Tela_Inicial", u"An\u00e1lise", None))
        self.BT_Home.setText(QCoreApplication.translate("Tela_Inicial", u"Home", None))
        self.BT_Info.setText(QCoreApplication.translate("Tela_Inicial", u"Info", None))
        self.LBL_Info.setText(QCoreApplication.translate("Tela_Inicial", u"Informa\u00e7\u00f5es", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Tbox_Sobre), QCoreApplication.translate("Tela_Inicial", u"Sobre", None))
#if QT_CONFIG(whatsthis)
        self.Right_Container.setWhatsThis(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.BT_Menu.setText("")
#if QT_CONFIG(whatsthis)
        self.LBL_Logo_Clinica_Jansen.setWhatsThis(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.LBL_Logo_Clinica_Jansen.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_Logo.png\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/BackGround/Icons/Backgrounds/Imagem4.png\"/></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Tela_Inicial", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Tela_Inicial", u"Agendamento", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Tela_Inicial", u"Hor\u00e1rio", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Tela_Inicial", u"Procedimento", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Tela_Inicial", u"Pagamento", None));
        self.LBL_GerenciarProntuarios.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_GerenciarProntu\u00e1rios.png\"/></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Superior</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Ocorr\u00eancia</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Posi\u00e7\u00e3o</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Tela_Inicial", u"Observa\u00e7\u00e3o:", None))
        self.label_4.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Logos/Icons/Logos/Prontuario.png\"/></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Inferior</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Posi\u00e7\u00e3o</p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Ocorr\u00eancia</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Tela_Inicial", u"Observa\u00e7\u00e3o:", None))
        self.label_17.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Superior</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Ocorr\u00eancia</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Posi\u00e7\u00e3o</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Tela_Inicial", u"Observa\u00e7\u00e3o:", None))
        ___qtablewidgetitem5 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Tela_Inicial", u"Atendimentos", None));
        ___qtablewidgetitem6 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Tela_Inicial", u"Procedimentos", None));
        ___qtablewidgetitem7 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Tela_Inicial", u"Descri\u00e7\u00f5es", None));
        ___qtablewidgetitem8 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Tela_Inicial", u"Observa\u00e7\u00f5es", None));
        ___qtablewidgetitem9 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Tela_Inicial", u"Posi\u00e7\u00f5es", None));
        ___qtablewidgetitem10 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Tela_Inicial", u"Ocorr\u00eancias", None));
        ___qtablewidgetitem11 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Tela_Inicial", u"Descri\u00e7\u00f5es", None));
        ___qtablewidgetitem12 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Tela_Inicial", u"Observa\u00e7\u00f5es", None));
        self.pushButton_14.setText("")
        self.BT_CadastroLEFT_4.setText("")
        self.label_34.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Superior</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Ocorr\u00eancia</p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Posi\u00e7\u00e3o</p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("Tela_Inicial", u"Observa\u00e7\u00e3o:", None))
        self.label_38.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Logos/Icons/Logos/Prontuario.png\"/></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Inferior</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Posi\u00e7\u00e3o</p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\">Ocorr\u00eancia</p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("Tela_Inicial", u"Observa\u00e7\u00e3o:", None))
        self.LBL_GerenciarProncedimentos.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_Procedimentos.png\"/></p></body></html>", None))
        self.Tbox_Proncedimentos.setItemText(self.Tbox_Proncedimentos.indexOf(self.toolBox_2Page1_4), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_Proncedimentos.setItemText(self.Tbox_Proncedimentos.indexOf(self.toolBox_2Page2_4), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_FluxoCaixa.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_FluxoCaixa.png\"/></p></body></html>", None))
        self.Tbox_Proncedimentos_2.setItemText(self.Tbox_Proncedimentos_2.indexOf(self.toolBox_2Page1_5), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_Proncedimentos_2.setItemText(self.Tbox_Proncedimentos_2.indexOf(self.toolBox_2Page2_5), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_GerenciarReceitas.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_GerenciarReceitas.png\"/></p></body></html>", None))
        self.Tbox_GerenciarReceitas.setItemText(self.Tbox_GerenciarReceitas.indexOf(self.toolBox_2Page1_6), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_GerenciarReceitas.setItemText(self.Tbox_GerenciarReceitas.indexOf(self.toolBox_2Page2_6), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_GerenciarDespesas.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_GerenciarDespesas.png\"/></p></body></html>", None))
        self.Tbox_GerenciarDespesas.setItemText(self.Tbox_GerenciarDespesas.indexOf(self.toolBox_2Page1_7), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_GerenciarDespesas.setItemText(self.Tbox_GerenciarDespesas.indexOf(self.toolBox_2Page2_7), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_GerenciarEstoque.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_GerenciarEstoque.png\"/></p></body></html>", None))
        self.Tbox_GerenciarEstoque.setItemText(self.Tbox_GerenciarEstoque.indexOf(self.toolBox_2Page1_8), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_GerenciarEstoque.setItemText(self.Tbox_GerenciarEstoque.indexOf(self.toolBox_2Page2_8), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_GerenciarMedicamentos.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_ControleDeMedicamentos.png\"/></p></body></html>", None))
        self.Tbox_GerenciarMedicamentos.setItemText(self.Tbox_GerenciarMedicamentos.indexOf(self.toolBox_2Page1_9), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_GerenciarMedicamentos.setItemText(self.Tbox_GerenciarMedicamentos.indexOf(self.toolBox_2Page2_9), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_InstituicoesParceiras.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_InstituicoesParceiras.png\"/></p></body></html>", None))
        self.Tbox_InstituicoesParceiras.setItemText(self.Tbox_InstituicoesParceiras.indexOf(self.toolBox_2Page1_10), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_InstituicoesParceiras.setItemText(self.Tbox_InstituicoesParceiras.indexOf(self.toolBox_2Page2_10), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_AnaliseDados1.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_AnaliseDados1.png\"/></p></body></html>", None))
        self.Tbox_AnaliseDados1.setItemText(self.Tbox_AnaliseDados1.indexOf(self.toolBox_2Page1_11), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_AnaliseDados1.setItemText(self.Tbox_AnaliseDados1.indexOf(self.toolBox_2Page2_11), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_AnaliseDados2.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_AnaliseDados2.png\"/></p></body></html>", None))
        self.Tbox_AnaliseDados2.setItemText(self.Tbox_AnaliseDados2.indexOf(self.toolBox_2Page1_12), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_AnaliseDados2.setItemText(self.Tbox_AnaliseDados2.indexOf(self.toolBox_2Page2_12), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_AnaliseDados2_2.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_AnaliseDados3.png\"/></p></body></html>", None))
        self.Tbox_AnaliseDados2_2.setItemText(self.Tbox_AnaliseDados2_2.indexOf(self.toolBox_2Page1_13), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_AnaliseDados2_2.setItemText(self.Tbox_AnaliseDados2_2.indexOf(self.toolBox_2Page2_13), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
        self.LBL_AnaliseDados3.setText(QCoreApplication.translate("Tela_Inicial", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_Informacoes.png\"/></p></body></html>", None))
        self.Tbox_AnaliseDados3.setItemText(self.Tbox_AnaliseDados3.indexOf(self.toolBox_2Page1_14), QCoreApplication.translate("Tela_Inicial", u"Page1", None))
        self.Tbox_AnaliseDados3.setItemText(self.Tbox_AnaliseDados3.indexOf(self.toolBox_2Page2_14), QCoreApplication.translate("Tela_Inicial", u"Page2", None))
    # retranslateUi

