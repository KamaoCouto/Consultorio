# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_Tela_00.ui'
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

class Ui_Form_Login(object):
    def setupUi(self, Form_Login):
        if not Form_Login.objectName():
            Form_Login.setObjectName(u"Form_Login")
        Form_Login.resize(377, 587)
        Form_Login.setMinimumSize(QSize(377, 587))
        Form_Login.setMaximumSize(QSize(377, 587))
        self.LBL_Fundo = QLabel(Form_Login)
        self.LBL_Fundo.setObjectName(u"LBL_Fundo")
        self.LBL_Fundo.setGeometry(QRect(0, 0, 377, 588))
        self.LBL_Fundo.setMaximumSize(QSize(377, 588))
        self.LBL_Fundo.setStyleSheet(u"background-image: url(:/Bt_s/Icons/Backgrounds/Imagem1.png);")
        self.BT_Entrar = QPushButton(Form_Login)
        self.BT_Entrar.setObjectName(u"BT_Entrar")
        self.BT_Entrar.setGeometry(QRect(250, 310, 88, 35))
        font = QFont()
        font.setFamilies([u"Verdana"])
        self.BT_Entrar.setFont(font)
        self.BT_Entrar.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_7.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_8.png);\n"
"}")
        self.LBL_PasswordConfirm = QLabel(Form_Login)
        self.LBL_PasswordConfirm.setObjectName(u"LBL_PasswordConfirm")
        self.LBL_PasswordConfirm.setGeometry(QRect(30, 250, 40, 50))
        self.LBL_PasswordConfirm.setStyleSheet(u"QLabel{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_4.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_5.png);\n"
"}")
        self.TXT_Senha = QLineEdit(Form_Login)
        self.TXT_Senha.setObjectName(u"TXT_Senha")
        self.TXT_Senha.setGeometry(QRect(80, 260, 220, 30))
        self.TXT_Senha.setFont(font)
        self.LBL_EmailConfirm = QLabel(Form_Login)
        self.LBL_EmailConfirm.setObjectName(u"LBL_EmailConfirm")
        self.LBL_EmailConfirm.setGeometry(QRect(30, 190, 40, 50))
        self.LBL_EmailConfirm.setStyleSheet(u"QLabel{ \n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_Mail_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border:15px;\n"
"background-image: url(:/BackGround/Icons/BT_s/Icon_Mail_2.png);\n"
"}")
        self.CB_LembrarMe = QCheckBox(Form_Login)
        self.CB_LembrarMe.setObjectName(u"CB_LembrarMe")
        self.CB_LembrarMe.setGeometry(QRect(40, 320, 100, 21))
        self.CB_LembrarMe.setFont(font)
        self.TXT_Nome = QLineEdit(Form_Login)
        self.TXT_Nome.setObjectName(u"TXT_Nome")
        self.TXT_Nome.setGeometry(QRect(80, 140, 261, 30))
        self.TXT_Nome.setFont(font)
        self.F_ShowHide = QFrame(Form_Login)
        self.F_ShowHide.setObjectName(u"F_ShowHide")
        self.F_ShowHide.setGeometry(QRect(300, 260, 40, 28))
        self.F_ShowHide.setMaximumSize(QSize(40, 28))
        self.F_ShowHide.setFrameShape(QFrame.StyledPanel)
        self.F_ShowHide.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.F_ShowHide)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.f_senhaShow_2 = QFrame(self.F_ShowHide)
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

        self.f_senhaHide_2 = QFrame(self.F_ShowHide)
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

        self.LBL_UserConfirm = QLabel(Form_Login)
        self.LBL_UserConfirm.setObjectName(u"LBL_UserConfirm")
        self.LBL_UserConfirm.setGeometry(QRect(30, 130, 40, 50))
        self.LBL_UserConfirm.setStyleSheet(u"QLabel{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"border:15px;\n"
"	background-image: url(:/Bt_s/Icons/BT_s/Icon_Login_2.png);\n"
"}")
        self.TXT_Email = QLineEdit(Form_Login)
        self.TXT_Email.setObjectName(u"TXT_Email")
        self.TXT_Email.setGeometry(QRect(80, 200, 261, 30))
        self.TXT_Email.setFont(font)
        self.BT_NewUser = QPushButton(Form_Login)
        self.BT_NewUser.setObjectName(u"BT_NewUser")
        self.BT_NewUser.setGeometry(QRect(100, 90, 181, 28))
        self.BT_NewUser.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_NewUser_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bt_s/Icons/BT_s/Icon_NewUser_2.png);\n"
"}")

        self.retranslateUi(Form_Login)

        QMetaObject.connectSlotsByName(Form_Login)
    # setupUi

    def retranslateUi(self, Form_Login):
        Form_Login.setWindowTitle(QCoreApplication.translate("Form_Login", u"Form", None))
        self.LBL_Fundo.setText("")
        self.BT_Entrar.setText(QCoreApplication.translate("Form_Login", u"Entrar", None))
        self.LBL_PasswordConfirm.setText("")
        self.TXT_Senha.setPlaceholderText(QCoreApplication.translate("Form_Login", u" Senha", None))
        self.LBL_EmailConfirm.setText("")
        self.CB_LembrarMe.setText(QCoreApplication.translate("Form_Login", u"Lembrar-me", None))
        self.TXT_Nome.setPlaceholderText(QCoreApplication.translate("Form_Login", u"  Nome ", None))
        self.BT_senhaHide_2.setText("")
        self.pushButton_2.setText("")
        self.LBL_UserConfirm.setText("")
        self.TXT_Email.setPlaceholderText(QCoreApplication.translate("Form_Login", u"  Email ", None))
        self.BT_NewUser.setText("")
    # retranslateUi

