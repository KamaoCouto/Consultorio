# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_Tela_01.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import Background_rc
import BT_s_rc
import Infos_rc
import Logo_rc
import Title_rc

class Ui_Form_novoUsuario(object):
    def setupUi(self, Form_novoUsuario):
        if not Form_novoUsuario.objectName():
            Form_novoUsuario.setObjectName(u"Form_novoUsuario")
        Form_novoUsuario.resize(375, 587)
        Form_novoUsuario.setMaximumSize(QSize(377, 587))
        self.LBL_Fundo = QLabel(Form_novoUsuario)
        self.LBL_Fundo.setObjectName(u"LBL_Fundo")
        self.LBL_Fundo.setGeometry(QRect(0, 0, 377, 588))
        self.LBL_Fundo.setMinimumSize(QSize(377, 588))
        self.LBL_Fundo.setMaximumSize(QSize(588, 16777215))
        self.LBL_Fundo.setStyleSheet(u"background-image: url(:/BackGround/Icons/Backgrounds/NovoCadastro.png);\n"
"")
        self.TXT_Senha = QLineEdit(Form_novoUsuario)
        self.TXT_Senha.setObjectName(u"TXT_Senha")
        self.TXT_Senha.setGeometry(QRect(80, 155, 220, 30))
        font = QFont()
        font.setFamilies([u"Verdana"])
        self.TXT_Senha.setFont(font)
        self.LBL_Email = QLabel(Form_novoUsuario)
        self.LBL_Email.setObjectName(u"LBL_Email")
        self.LBL_Email.setGeometry(QRect(30, 265, 40, 50))
        self.LBL_Email.setStyleSheet(u"QLabel{ \n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_Mail_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border:15px;\n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_Mail_2.png);\n"
"}")
        self.LBL_Nome = QLabel(Form_novoUsuario)
        self.LBL_Nome.setObjectName(u"LBL_Nome")
        self.LBL_Nome.setGeometry(QRect(30, 85, 40, 50))
        self.LBL_Nome.setStyleSheet(u"QLabel{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border:15px;\n"
"	background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_2.png);\n"
"}")
        self.LBL_Senha = QLabel(Form_novoUsuario)
        self.LBL_Senha.setObjectName(u"LBL_Senha")
        self.LBL_Senha.setGeometry(QRect(30, 145, 40, 50))
        self.LBL_Senha.setStyleSheet(u"QLabel{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_4.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_5.png);\n"
"}")
        self.TXT_Email = QLineEdit(Form_novoUsuario)
        self.TXT_Email.setObjectName(u"TXT_Email")
        self.TXT_Email.setGeometry(QRect(80, 275, 201, 30))
        self.TXT_Email.setFont(font)
        self.TXT_SenhaConfirmacao = QLineEdit(Form_novoUsuario)
        self.TXT_SenhaConfirmacao.setObjectName(u"TXT_SenhaConfirmacao")
        self.TXT_SenhaConfirmacao.setGeometry(QRect(80, 215, 220, 30))
        self.TXT_SenhaConfirmacao.setFont(font)
        self.LBL_SenhaConfirmacao = QLabel(Form_novoUsuario)
        self.LBL_SenhaConfirmacao.setObjectName(u"LBL_SenhaConfirmacao")
        self.LBL_SenhaConfirmacao.setGeometry(QRect(30, 205, 40, 50))
        self.LBL_SenhaConfirmacao.setStyleSheet(u"QLabel{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_4.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_5.png);\n"
"}")
        self.frame = QFrame(Form_novoUsuario)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(300, 155, 38, 28))
        self.frame.setMaximumSize(QSize(40, 28))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.f_senhaShow_1 = QFrame(self.frame)
        self.f_senhaShow_1.setObjectName(u"f_senhaShow_1")
        self.f_senhaShow_1.setMaximumSize(QSize(40, 28))
        self.f_senhaShow_1.setFrameShape(QFrame.StyledPanel)
        self.f_senhaShow_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_senhaShow_1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BT_senhaShow_1 = QPushButton(self.f_senhaShow_1)
        self.BT_senhaShow_1.setObjectName(u"BT_senhaShow_1")
        self.BT_senhaShow_1.setMaximumSize(QSize(40, 28))
        self.BT_senhaShow_1.setFont(font)
        self.BT_senhaShow_1.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_eye_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_eye_2.png);\n"
"}")

        self.horizontalLayout_2.addWidget(self.BT_senhaShow_1)


        self.horizontalLayout.addWidget(self.f_senhaShow_1)

        self.f_senhaHide_1 = QFrame(self.frame)
        self.f_senhaHide_1.setObjectName(u"f_senhaHide_1")
        self.f_senhaHide_1.setMaximumSize(QSize(0, 28))
        self.f_senhaHide_1.setFrameShape(QFrame.StyledPanel)
        self.f_senhaHide_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.f_senhaHide_1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BT_senhaHide_1 = QPushButton(self.f_senhaHide_1)
        self.BT_senhaHide_1.setObjectName(u"BT_senhaHide_1")
        self.BT_senhaHide_1.setMaximumSize(QSize(40, 28))
        self.BT_senhaHide_1.setFont(font)
        self.BT_senhaHide_1.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_eye_2.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_eye_1.png);\n"
"}")

        self.horizontalLayout_3.addWidget(self.BT_senhaHide_1)


        self.horizontalLayout.addWidget(self.f_senhaHide_1)

        self.frame_4 = QFrame(Form_novoUsuario)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(300, 215, 40, 28))
        self.frame_4.setMaximumSize(QSize(40, 28))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.f_senhaShow_2 = QFrame(self.frame_4)
        self.f_senhaShow_2.setObjectName(u"f_senhaShow_2")
        self.f_senhaShow_2.setMaximumSize(QSize(40, 28))
        self.f_senhaShow_2.setFrameShape(QFrame.StyledPanel)
        self.f_senhaShow_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.f_senhaShow_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.BT_senhaHide_2 = QPushButton(self.f_senhaShow_2)
        self.BT_senhaHide_2.setObjectName(u"BT_senhaHide_2")
        self.BT_senhaHide_2.setMaximumSize(QSize(40, 28))
        self.BT_senhaHide_2.setFont(font)
        self.BT_senhaHide_2.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_eye_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_eye_2.png);\n"
"}")

        self.horizontalLayout_8.addWidget(self.BT_senhaHide_2)


        self.horizontalLayout_7.addWidget(self.f_senhaShow_2)

        self.f_senhaHide_2 = QFrame(self.frame_4)
        self.f_senhaHide_2.setObjectName(u"f_senhaHide_2")
        self.f_senhaHide_2.setMaximumSize(QSize(0, 28))
        self.f_senhaHide_2.setFrameShape(QFrame.StyledPanel)
        self.f_senhaHide_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.f_senhaHide_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.f_senhaHide_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(40, 28))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_eye_2.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_eye_1.png);\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.horizontalLayout_7.addWidget(self.f_senhaHide_2)

        self.LBL_CodigoAcesso = QLabel(Form_novoUsuario)
        self.LBL_CodigoAcesso.setObjectName(u"LBL_CodigoAcesso")
        self.LBL_CodigoAcesso.setGeometry(QRect(30, 325, 40, 50))
        self.LBL_CodigoAcesso.setStyleSheet(u"QLabel{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Key_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Key_2.png);\n"
"}")
        self.TXT_CodigoAcesso = QLineEdit(Form_novoUsuario)
        self.TXT_CodigoAcesso.setObjectName(u"TXT_CodigoAcesso")
        self.TXT_CodigoAcesso.setGeometry(QRect(80, 335, 260, 30))
        self.TXT_CodigoAcesso.setFont(font)
        self.CB_Dentista = QCheckBox(Form_novoUsuario)
        self.CB_Dentista.setObjectName(u"CB_Dentista")
        self.CB_Dentista.setGeometry(QRect(35, 415, 100, 21))
        self.CB_Dentista.setFont(font)
        self.CB_Atenfimento = QCheckBox(Form_novoUsuario)
        self.CB_Atenfimento.setObjectName(u"CB_Atenfimento")
        self.CB_Atenfimento.setGeometry(QRect(35, 440, 100, 21))
        self.CB_Atenfimento.setFont(font)
        self.LBLFuncao = QLabel(Form_novoUsuario)
        self.LBLFuncao.setObjectName(u"LBLFuncao")
        self.LBLFuncao.setGeometry(QRect(30, 385, 71, 21))
        font1 = QFont()
        font1.setFamilies([u"Lucida Calligraphy"])
        font1.setPointSize(10)
        self.LBLFuncao.setFont(font1)
        self.LBLFuncao.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.TXT_Nome = QLineEdit(Form_novoUsuario)
        self.TXT_Nome.setObjectName(u"TXT_Nome")
        self.TXT_Nome.setGeometry(QRect(80, 100, 260, 30))
        self.TXT_Nome.setFont(font)
        self.frame_7 = QFrame(Form_novoUsuario)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(280, 275, 68, 31))
        self.frame_7.setMaximumSize(QSize(68, 35))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(65, 35))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(65, 35))
        self.pushButton_4.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_SendKey_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_SendKey_2.png);\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_4)


        self.horizontalLayout_12.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(0, 35))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(65, 35))
        self.pushButton_5.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_SendKey_3.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_SendKey_2.png);\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton_5)


        self.horizontalLayout_12.addWidget(self.frame_3)

        self.widget_4 = QWidget(Form_novoUsuario)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(210, 420, 131, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.BT_ValidarCadastro = QPushButton(self.widget_3)
        self.BT_ValidarCadastro.setObjectName(u"BT_ValidarCadastro")
        self.BT_ValidarCadastro.setMaximumSize(QSize(123, 35))
        self.BT_ValidarCadastro.setFont(font)
        self.BT_ValidarCadastro.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_Login_9.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_Login_10.png);\n"
"}")

        self.horizontalLayout_6.addWidget(self.BT_ValidarCadastro)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(0, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BT_Cadastrar = QPushButton(self.widget)
        self.BT_Cadastrar.setObjectName(u"BT_Cadastrar")
        self.BT_Cadastrar.setMaximumSize(QSize(123, 35))
        self.BT_Cadastrar.setFont(font)
        self.BT_Cadastrar.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_Login_10.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_Login_9.png);\n"
"}")

        self.horizontalLayout_4.addWidget(self.BT_Cadastrar)


        self.horizontalLayout_5.addWidget(self.widget)


        self.retranslateUi(Form_novoUsuario)

        QMetaObject.connectSlotsByName(Form_novoUsuario)
    # setupUi

    def retranslateUi(self, Form_novoUsuario):
        Form_novoUsuario.setWindowTitle(QCoreApplication.translate("Form_novoUsuario", u"Form", None))
        self.LBL_Fundo.setText("")
        self.TXT_Senha.setPlaceholderText(QCoreApplication.translate("Form_novoUsuario", u"  Senha", None))
        self.LBL_Email.setText("")
        self.LBL_Nome.setText("")
        self.LBL_Senha.setText("")
        self.TXT_Email.setPlaceholderText(QCoreApplication.translate("Form_novoUsuario", u"  Email ", None))
        self.TXT_SenhaConfirmacao.setPlaceholderText(QCoreApplication.translate("Form_novoUsuario", u" Confirma\u00e7\u00e3o de senha", None))
        self.LBL_SenhaConfirmacao.setText("")
        self.BT_senhaShow_1.setText("")
        self.BT_senhaHide_1.setText("")
        self.BT_senhaHide_2.setText("")
        self.pushButton_2.setText("")
        self.LBL_CodigoAcesso.setText("")
        self.TXT_CodigoAcesso.setPlaceholderText(QCoreApplication.translate("Form_novoUsuario", u"  C\u00f3digo de acesso \"xxx - xxx\"", None))
        self.CB_Dentista.setText(QCoreApplication.translate("Form_novoUsuario", u"Dentista", None))
        self.CB_Atenfimento.setText(QCoreApplication.translate("Form_novoUsuario", u"Atendimento", None))
        self.LBLFuncao.setText(QCoreApplication.translate("Form_novoUsuario", u" Fun\u00e7\u00e3o ", None))
        self.TXT_Nome.setPlaceholderText(QCoreApplication.translate("Form_novoUsuario", u" Nome", None))
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.BT_ValidarCadastro.setText(QCoreApplication.translate("Form_novoUsuario", u"Validar", None))
        self.BT_Cadastrar.setText(QCoreApplication.translate("Form_novoUsuario", u"Cadastrar", None))
    # retranslateUi

