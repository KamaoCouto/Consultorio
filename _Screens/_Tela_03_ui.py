# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_Tela_03.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFontComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

#==============================================================================================
# Criando Imports imagens.py
#==============================================================================================
from ._Imagens  import (Background_rc,BT_s_rc,Logo_rc,Title_rc)

class Ui_Form_dadosPessoais(object):
    def setupUi(self, Form_dadosPessoais):
        if not Form_dadosPessoais.objectName():
            Form_dadosPessoais.setObjectName(u"Form_dadosPessoais")
        Form_dadosPessoais.resize(785, 640)
        Form_dadosPessoais.setMinimumSize(QSize(0, 640))
        Form_dadosPessoais.setMaximumSize(QSize(16777215, 640))
        Form_dadosPessoais.setStyleSheet(u"background-color: rgb(193, 237, 255);")
        self.horizontalLayout = QHBoxLayout(Form_dadosPessoais)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.fCadastro_Left = QFrame(Form_dadosPessoais)
        self.fCadastro_Left.setObjectName(u"fCadastro_Left")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fCadastro_Left.sizePolicy().hasHeightForWidth())
        self.fCadastro_Left.setSizePolicy(sizePolicy)
        self.fCadastro_Left.setMinimumSize(QSize(120, 0))
        self.fCadastro_Left.setMaximumSize(QSize(125, 16777215))
        self.fCadastro_Left.setStyleSheet(u"border-radius:20px;\n"
"")
        self.fCadastro_Left.setFrameShape(QFrame.StyledPanel)
        self.fCadastro_Left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.fCadastro_Left)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 10, 0, 0)
        self.fCadastro_Left_Opened = QFrame(self.fCadastro_Left)
        self.fCadastro_Left_Opened.setObjectName(u"fCadastro_Left_Opened")
        sizePolicy.setHeightForWidth(self.fCadastro_Left_Opened.sizePolicy().hasHeightForWidth())
        self.fCadastro_Left_Opened.setSizePolicy(sizePolicy)
        self.fCadastro_Left_Opened.setMinimumSize(QSize(0, 500))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.fCad_Left_01.sizePolicy().hasHeightForWidth())
        self.fCad_Left_01.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.fCad_Left_12.sizePolicy().hasHeightForWidth())
        self.fCad_Left_12.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btCad_Left_LIG_01.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_01.setSizePolicy(sizePolicy2)
        self.btCad_Left_LIG_01.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_01.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_01.setStyleSheet(u"\n"
"QPushButton{\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_User_3.png);\n"
"border:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_User_2.png);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_69.addWidget(self.btCad_Left_LIG_01)


        self.horizontalLayout_46.addWidget(self.fCad_Left_12)

        self.fCad_Left_11 = QFrame(self.fCad_Left_01)
        self.fCad_Left_11.setObjectName(u"fCad_Left_11")
        sizePolicy1.setHeightForWidth(self.fCad_Left_11.sizePolicy().hasHeightForWidth())
        self.fCad_Left_11.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.btCad_Left_DESL_01.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_01.setSizePolicy(sizePolicy2)
        self.btCad_Left_DESL_01.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_01.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_01.setStyleSheet(u"\n"
"QPushButton{\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_User_1.png);\n"
"border:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_User_2.png);\n"
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
        sizePolicy1.setHeightForWidth(self.fCad_Left_02.sizePolicy().hasHeightForWidth())
        self.fCad_Left_02.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.fCad_Left_22.sizePolicy().hasHeightForWidth())
        self.fCad_Left_22.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.btCad_Left_LIG_02.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_02.setSizePolicy(sizePolicy2)
        self.btCad_Left_LIG_02.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_02.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_02.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Dente_3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Dente_2.png);	\n"
"}\n"
"\n"
"")

        self.horizontalLayout_70.addWidget(self.btCad_Left_LIG_02)


        self.horizontalLayout_55.addWidget(self.fCad_Left_22)

        self.fCad_Left_21 = QFrame(self.fCad_Left_02)
        self.fCad_Left_21.setObjectName(u"fCad_Left_21")
        sizePolicy1.setHeightForWidth(self.fCad_Left_21.sizePolicy().hasHeightForWidth())
        self.fCad_Left_21.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.btCad_Left_DESL_02.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_02.setSizePolicy(sizePolicy2)
        self.btCad_Left_DESL_02.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_02.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_02.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Dente_1.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Dente_2.png);	\n"
"}\n"
"\n"
"")

        self.horizontalLayout_71.addWidget(self.btCad_Left_DESL_02)


        self.horizontalLayout_55.addWidget(self.fCad_Left_21)


        self.verticalLayout_55.addWidget(self.fCad_Left_02)

        self.fCad_Left_03 = QFrame(self.fCadastro_Left_Opened)
        self.fCad_Left_03.setObjectName(u"fCad_Left_03")
        sizePolicy1.setHeightForWidth(self.fCad_Left_03.sizePolicy().hasHeightForWidth())
        self.fCad_Left_03.setSizePolicy(sizePolicy1)
        self.fCad_Left_03.setMinimumSize(QSize(0, 0))
        self.fCad_Left_03.setMaximumSize(QSize(50, 50))
        self.fCad_Left_03.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_03.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.fCad_Left_03)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_32 = QFrame(self.fCad_Left_03)
        self.fCad_Left_32.setObjectName(u"fCad_Left_32")
        sizePolicy1.setHeightForWidth(self.fCad_Left_32.sizePolicy().hasHeightForWidth())
        self.fCad_Left_32.setSizePolicy(sizePolicy1)
        self.fCad_Left_32.setMinimumSize(QSize(0, 0))
        self.fCad_Left_32.setMaximumSize(QSize(0, 50))
        self.fCad_Left_32.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.fCad_Left_32)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_03 = QPushButton(self.fCad_Left_32)
        self.btCad_Left_LIG_03.setObjectName(u"btCad_Left_LIG_03")
        sizePolicy2.setHeightForWidth(self.btCad_Left_LIG_03.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_03.setSizePolicy(sizePolicy2)
        self.btCad_Left_LIG_03.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_03.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_03.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_historyHealt3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_historyHealt_2.png);\n"
"}")

        self.horizontalLayout_65.addWidget(self.btCad_Left_LIG_03)


        self.horizontalLayout_57.addWidget(self.fCad_Left_32)

        self.fCad_Left_31 = QFrame(self.fCad_Left_03)
        self.fCad_Left_31.setObjectName(u"fCad_Left_31")
        sizePolicy1.setHeightForWidth(self.fCad_Left_31.sizePolicy().hasHeightForWidth())
        self.fCad_Left_31.setSizePolicy(sizePolicy1)
        self.fCad_Left_31.setMinimumSize(QSize(40, 0))
        self.fCad_Left_31.setMaximumSize(QSize(0, 50))
        self.fCad_Left_31.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.fCad_Left_31)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_03 = QPushButton(self.fCad_Left_31)
        self.btCad_Left_DESL_03.setObjectName(u"btCad_Left_DESL_03")
        sizePolicy2.setHeightForWidth(self.btCad_Left_DESL_03.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_03.setSizePolicy(sizePolicy2)
        self.btCad_Left_DESL_03.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_03.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_03.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_historyHealt.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_historyHealt_2.png);\n"
"}")

        self.horizontalLayout_47.addWidget(self.btCad_Left_DESL_03)


        self.horizontalLayout_57.addWidget(self.fCad_Left_31)


        self.verticalLayout_55.addWidget(self.fCad_Left_03)

        self.fCad_Left_04 = QFrame(self.fCadastro_Left_Opened)
        self.fCad_Left_04.setObjectName(u"fCad_Left_04")
        sizePolicy1.setHeightForWidth(self.fCad_Left_04.sizePolicy().hasHeightForWidth())
        self.fCad_Left_04.setSizePolicy(sizePolicy1)
        self.fCad_Left_04.setMinimumSize(QSize(0, 0))
        self.fCad_Left_04.setMaximumSize(QSize(50, 50))
        self.fCad_Left_04.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_04.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.fCad_Left_04)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_42 = QFrame(self.fCad_Left_04)
        self.fCad_Left_42.setObjectName(u"fCad_Left_42")
        sizePolicy1.setHeightForWidth(self.fCad_Left_42.sizePolicy().hasHeightForWidth())
        self.fCad_Left_42.setSizePolicy(sizePolicy1)
        self.fCad_Left_42.setMinimumSize(QSize(0, 0))
        self.fCad_Left_42.setMaximumSize(QSize(0, 50))
        self.fCad_Left_42.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.fCad_Left_42)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_04 = QPushButton(self.fCad_Left_42)
        self.btCad_Left_LIG_04.setObjectName(u"btCad_Left_LIG_04")
        sizePolicy2.setHeightForWidth(self.btCad_Left_LIG_04.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_04.setSizePolicy(sizePolicy2)
        self.btCad_Left_LIG_04.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_04.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_04.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_Finance_3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_Finance_2.png);\n"
"}")

        self.horizontalLayout_72.addWidget(self.btCad_Left_LIG_04)


        self.horizontalLayout_56.addWidget(self.fCad_Left_42)

        self.fCad_Left_41 = QFrame(self.fCad_Left_04)
        self.fCad_Left_41.setObjectName(u"fCad_Left_41")
        sizePolicy1.setHeightForWidth(self.fCad_Left_41.sizePolicy().hasHeightForWidth())
        self.fCad_Left_41.setSizePolicy(sizePolicy1)
        self.fCad_Left_41.setMinimumSize(QSize(40, 0))
        self.fCad_Left_41.setMaximumSize(QSize(0, 50))
        self.fCad_Left_41.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.fCad_Left_41)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_04 = QPushButton(self.fCad_Left_41)
        self.btCad_Left_DESL_04.setObjectName(u"btCad_Left_DESL_04")
        sizePolicy2.setHeightForWidth(self.btCad_Left_DESL_04.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_04.setSizePolicy(sizePolicy2)
        self.btCad_Left_DESL_04.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_04.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_04.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_Finance.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_Finance_2.png);\n"
"}")

        self.horizontalLayout_59.addWidget(self.btCad_Left_DESL_04)


        self.horizontalLayout_56.addWidget(self.fCad_Left_41)


        self.verticalLayout_55.addWidget(self.fCad_Left_04)

        self.fCad_Left_5 = QFrame(self.fCadastro_Left_Opened)
        self.fCad_Left_5.setObjectName(u"fCad_Left_5")
        sizePolicy1.setHeightForWidth(self.fCad_Left_5.sizePolicy().hasHeightForWidth())
        self.fCad_Left_5.setSizePolicy(sizePolicy1)
        self.fCad_Left_5.setMinimumSize(QSize(0, 0))
        self.fCad_Left_5.setMaximumSize(QSize(50, 50))
        self.fCad_Left_5.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.fCad_Left_5)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_52 = QFrame(self.fCad_Left_5)
        self.fCad_Left_52.setObjectName(u"fCad_Left_52")
        sizePolicy1.setHeightForWidth(self.fCad_Left_52.sizePolicy().hasHeightForWidth())
        self.fCad_Left_52.setSizePolicy(sizePolicy1)
        self.fCad_Left_52.setMinimumSize(QSize(0, 0))
        self.fCad_Left_52.setMaximumSize(QSize(0, 50))
        self.fCad_Left_52.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.fCad_Left_52)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_05 = QPushButton(self.fCad_Left_52)
        self.btCad_Left_LIG_05.setObjectName(u"btCad_Left_LIG_05")
        sizePolicy2.setHeightForWidth(self.btCad_Left_LIG_05.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_05.setSizePolicy(sizePolicy2)
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


        self.horizontalLayout_74.addWidget(self.fCad_Left_52)

        self.fCad_Left_51 = QFrame(self.fCad_Left_5)
        self.fCad_Left_51.setObjectName(u"fCad_Left_51")
        sizePolicy1.setHeightForWidth(self.fCad_Left_51.sizePolicy().hasHeightForWidth())
        self.fCad_Left_51.setSizePolicy(sizePolicy1)
        self.fCad_Left_51.setMinimumSize(QSize(40, 0))
        self.fCad_Left_51.setMaximumSize(QSize(0, 50))
        self.fCad_Left_51.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.fCad_Left_51)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_05 = QPushButton(self.fCad_Left_51)
        self.btCad_Left_DESL_05.setObjectName(u"btCad_Left_DESL_05")
        sizePolicy2.setHeightForWidth(self.btCad_Left_DESL_05.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_05.setSizePolicy(sizePolicy2)
        self.btCad_Left_DESL_05.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_05.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_05.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Find_1.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Find_2.png);\n"
"}")

        self.horizontalLayout_76.addWidget(self.btCad_Left_DESL_05)


        self.horizontalLayout_74.addWidget(self.fCad_Left_51)


        self.verticalLayout_55.addWidget(self.fCad_Left_5)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_11)


        self.horizontalLayout_45.addWidget(self.fCadastro_Left_Opened)

        self.fCadastro_Left_On = QFrame(self.fCadastro_Left)
        self.fCadastro_Left_On.setObjectName(u"fCadastro_Left_On")
        sizePolicy.setHeightForWidth(self.fCadastro_Left_On.sizePolicy().hasHeightForWidth())
        self.fCadastro_Left_On.setSizePolicy(sizePolicy)
        self.fCadastro_Left_On.setMinimumSize(QSize(60, 0))
        self.fCadastro_Left_On.setMaximumSize(QSize(0, 16777215))
        self.fCadastro_Left_On.setStyleSheet(u"")
        self.fCadastro_Left_On.setFrameShape(QFrame.StyledPanel)
        self.fCadastro_Left_On.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.fCadastro_Left_On)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 0)
        self.BT_Cad_Left_LIGAR = QPushButton(self.fCadastro_Left_On)
        self.BT_Cad_Left_LIGAR.setObjectName(u"BT_Cad_Left_LIGAR")
        self.BT_Cad_Left_LIGAR.setMinimumSize(QSize(40, 50))
        self.BT_Cad_Left_LIGAR.setMaximumSize(QSize(0, 50))
        self.BT_Cad_Left_LIGAR.setStyleSheet(u"\n"
"QPushButton{\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_RIGHT.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-image: url(:/Bts/Icons/BT_s/Icon_RIGHT_2.png);\n"
"}")

        self.verticalLayout_27.addWidget(self.BT_Cad_Left_LIGAR)

        self.verticalSpacer_10 = QSpacerItem(20, 541, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_10)


        self.horizontalLayout_45.addWidget(self.fCadastro_Left_On)

        self.fCad_Left_Off = QFrame(self.fCadastro_Left)
        self.fCad_Left_Off.setObjectName(u"fCad_Left_Off")
        sizePolicy.setHeightForWidth(self.fCad_Left_Off.sizePolicy().hasHeightForWidth())
        self.fCad_Left_Off.setSizePolicy(sizePolicy)
        self.fCad_Left_Off.setMinimumSize(QSize(0, 0))
        self.fCad_Left_Off.setMaximumSize(QSize(0, 16777215))
        self.fCad_Left_Off.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_Off.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.fCad_Left_Off)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 0)
        self.BT_Cad_Left_DESLIGAR = QPushButton(self.fCad_Left_Off)
        self.BT_Cad_Left_DESLIGAR.setObjectName(u"BT_Cad_Left_DESLIGAR")
        sizePolicy.setHeightForWidth(self.BT_Cad_Left_DESLIGAR.sizePolicy().hasHeightForWidth())
        self.BT_Cad_Left_DESLIGAR.setSizePolicy(sizePolicy)
        self.BT_Cad_Left_DESLIGAR.setMinimumSize(QSize(40, 50))
        self.BT_Cad_Left_DESLIGAR.setMaximumSize(QSize(0, 60))
        self.BT_Cad_Left_DESLIGAR.setStyleSheet(u"\n"
"QPushButton{\n"
"\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_LEFT_2.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_LEFT.png);\n"
"}")

        self.verticalLayout_25.addWidget(self.BT_Cad_Left_DESLIGAR)

        self.verticalSpacer_9 = QSpacerItem(20, 541, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_9)


        self.horizontalLayout_45.addWidget(self.fCad_Left_Off)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.fCadastro_Left)

        self.Frame_USER = QWidget(Form_dadosPessoais)
        self.Frame_USER.setObjectName(u"Frame_USER")
        self.Frame_USER.setMinimumSize(QSize(625, 0))
        self.Frame_USER.setMaximumSize(QSize(16777215, 16777215))
        self.Frame_USER.setStyleSheet(u"QWidget{\n"
"\n"
"font-color: rgb(11, 11, 11);\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"	text-align: left;	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius:10px;\n"
"	text-align: left;\n"
"	background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"	color: rgb(206, 255, 254);\n"
"	\n"
"}")
        self.gridLayout_5 = QGridLayout(self.Frame_USER)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, -1, 0, 0)
        self.LBL_AddCadastro = QLabel(self.Frame_USER)
        self.LBL_AddCadastro.setObjectName(u"LBL_AddCadastro")
        self.LBL_AddCadastro.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;\n"
"")

        self.gridLayout_5.addWidget(self.LBL_AddCadastro, 1, 0, 1, 1)

        self.Tbox_Cadastro = QStackedWidget(self.Frame_USER)
        self.Tbox_Cadastro.setObjectName(u"Tbox_Cadastro")
        sizePolicy.setHeightForWidth(self.Tbox_Cadastro.sizePolicy().hasHeightForWidth())
        self.Tbox_Cadastro.setSizePolicy(sizePolicy)
        self.Tbox_Cadastro.setMinimumSize(QSize(550, 0))
        font = QFont()
        font.setFamilies([u"Lucida Calligraphy"])
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.Tbox_Cadastro.setFont(font)
        self.Tbox_Cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.Tbox_Cadastro.setMouseTracking(False)
        self.Tbox_Cadastro.setTabletTracking(False)
        self.Tbox_Cadastro.setStyleSheet(u"\n"
"QPushButton:{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(149, 149, 149);\n"
"border:15px;\n"
"}\n"
"")
        self.Tbox_CadastroHome = QWidget()
        self.Tbox_CadastroHome.setObjectName(u"Tbox_CadastroHome")
        self.horizontalLayout_63 = QHBoxLayout(self.Tbox_CadastroHome)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.Tela_Inicio = QLabel(self.Tbox_CadastroHome)
        self.Tela_Inicio.setObjectName(u"Tela_Inicio")
        sizePolicy.setHeightForWidth(self.Tela_Inicio.sizePolicy().hasHeightForWidth())
        self.Tela_Inicio.setSizePolicy(sizePolicy)
        self.Tela_Inicio.setMinimumSize(QSize(415, 532))
        self.Tela_Inicio.setMaximumSize(QSize(415, 532))
        self.Tela_Inicio.setStyleSheet(u"QLineEdit{\n"
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

        self.horizontalLayout_63.addWidget(self.Tela_Inicio)

        self.Tbox_Cadastro.addWidget(self.Tbox_CadastroHome)
        self.Tbox_CadastroPage1 = QWidget()
        self.Tbox_CadastroPage1.setObjectName(u"Tbox_CadastroPage1")
        self.horizontalLayout_73 = QHBoxLayout(self.Tbox_CadastroPage1)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.Frame_Dados_Pessoais_ = QFrame(self.Tbox_CadastroPage1)
        self.Frame_Dados_Pessoais_.setObjectName(u"Frame_Dados_Pessoais_")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Frame_Dados_Pessoais_.sizePolicy().hasHeightForWidth())
        self.Frame_Dados_Pessoais_.setSizePolicy(sizePolicy3)
        self.Frame_Dados_Pessoais_.setMinimumSize(QSize(415, 532))
        self.Frame_Dados_Pessoais_.setMaximumSize(QSize(415, 532))
        self.Frame_Dados_Pessoais_.setStyleSheet(u"QLineEdit{\n"
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
        self.Frame_Dados_Pessoais_.setFrameShape(QFrame.StyledPanel)
        self.Frame_Dados_Pessoais_.setFrameShadow(QFrame.Raised)
        self.GENERO = QWidget(self.Frame_Dados_Pessoais_)
        self.GENERO.setObjectName(u"GENERO")
        self.GENERO.setGeometry(QRect(5, 330, 0, 157))
        self.GENERO.setStyleSheet(u"border-radius:10px;")
        self.BT_sexo_Fem = QCheckBox(self.GENERO)
        self.BT_sexo_Fem.setObjectName(u"BT_sexo_Fem")
        self.BT_sexo_Fem.setEnabled(True)
        self.BT_sexo_Fem.setGeometry(QRect(5, 35, 80, 25))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        self.BT_sexo_Fem.setFont(font1)
        self.BT_sexo_Outros = QCheckBox(self.GENERO)
        self.BT_sexo_Outros.setObjectName(u"BT_sexo_Outros")
        self.BT_sexo_Outros.setEnabled(True)
        self.BT_sexo_Outros.setGeometry(QRect(5, 95, 80, 25))
        self.BT_sexo_Outros.setFont(font1)
        self.BT_sexo_Masc = QCheckBox(self.GENERO)
        self.BT_sexo_Masc.setObjectName(u"BT_sexo_Masc")
        self.BT_sexo_Masc.setGeometry(QRect(5, 65, 80, 25))
        self.BT_sexo_Masc.setFont(font1)
        self.label_5 = QLabel(self.GENERO)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(5, 5, 80, 25))
        self.label_5.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.BT_sexo_Ocultar = QCheckBox(self.GENERO)
        self.BT_sexo_Ocultar.setObjectName(u"BT_sexo_Ocultar")
        self.BT_sexo_Ocultar.setGeometry(QRect(5, 125, 80, 25))
        self.BT_sexo_Ocultar.setFont(font1)
        self.widget_9 = QWidget(self.Frame_Dados_Pessoais_)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(5, 5, 405, 320))
        self.widget_9.setStyleSheet(u"border-radius:10px;")
        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(5, 5, 395, 25))
        self.label_6.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.TXT_Nome_Completo = QLineEdit(self.widget_9)
        self.TXT_Nome_Completo.setObjectName(u"TXT_Nome_Completo")
        self.TXT_Nome_Completo.setGeometry(QRect(5, 35, 395, 25))
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.TXT_Nome_Completo.sizePolicy().hasHeightForWidth())
        self.TXT_Nome_Completo.setSizePolicy(sizePolicy4)
        self.TXT_Nome_Completo.setMinimumSize(QSize(6, 6))
        self.TXT_Nome_Completo.setMaximumSize(QSize(16777215, 16777206))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        self.TXT_Nome_Completo.setFont(font2)
        self.TXT_Nome_Completo.setCursor(QCursor(Qt.IBeamCursor))
        self.TXT_Nome_Completo.setMouseTracking(True)
        self.TXT_Nome_Completo.setFocusPolicy(Qt.StrongFocus)
        self.TXT_Nome_Completo.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_CPF = QLineEdit(self.widget_9)
        self.TXT_CPF.setObjectName(u"TXT_CPF")
        self.TXT_CPF.setGeometry(QRect(275, 65, 125, 25))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.TXT_CPF.setFont(font3)
        self.TXT_CPF.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_RG = QLineEdit(self.widget_9)
        self.TXT_RG.setObjectName(u"TXT_RG")
        self.TXT_RG.setGeometry(QRect(140, 65, 125, 25))
        self.TXT_RG.setFont(font3)
        self.TXT_RG.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Data_Nasc = QLineEdit(self.widget_9)
        self.TXT_Data_Nasc.setObjectName(u"TXT_Data_Nasc")
        self.TXT_Data_Nasc.setGeometry(QRect(5, 65, 125, 25))
        self.TXT_Data_Nasc.setFont(font3)
        self.TXT_Data_Nasc.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Municipio = QLineEdit(self.widget_9)
        self.TXT_Municipio.setObjectName(u"TXT_Municipio")
        self.TXT_Municipio.setGeometry(QRect(275, 195, 125, 25))
        self.TXT_Municipio.setFont(font3)
        self.TXT_Municipio.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Logradouro = QLineEdit(self.widget_9)
        self.TXT_Logradouro.setObjectName(u"TXT_Logradouro")
        self.TXT_Logradouro.setGeometry(QRect(5, 165, 330, 25))
        self.TXT_Logradouro.setFont(font3)
        self.TXT_Logradouro.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Complemento_Log = QLineEdit(self.widget_9)
        self.TXT_Complemento_Log.setObjectName(u"TXT_Complemento_Log")
        self.TXT_Complemento_Log.setGeometry(QRect(5, 195, 125, 25))
        self.TXT_Complemento_Log.setFont(font3)
        self.TXT_Complemento_Log.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(5, 135, 395, 25))
        self.label_7.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.TXT_CEP = QLineEdit(self.widget_9)
        self.TXT_CEP.setObjectName(u"TXT_CEP")
        self.TXT_CEP.setGeometry(QRect(140, 195, 125, 25))
        self.TXT_CEP.setFont(font3)
        self.TXT_CEP.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Cidade = QLineEdit(self.widget_9)
        self.TXT_Cidade.setObjectName(u"TXT_Cidade")
        self.TXT_Cidade.setGeometry(QRect(5, 225, 192, 25))
        self.TXT_Cidade.setFont(font3)
        self.TXT_Cidade.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Estado = QLineEdit(self.widget_9)
        self.TXT_Estado.setObjectName(u"TXT_Estado")
        self.TXT_Estado.setGeometry(QRect(208, 225, 192, 25))
        self.TXT_Estado.setFont(font3)
        self.TXT_Estado.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.label_8 = QLabel(self.widget_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(5, 260, 395, 25))
        self.label_8.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.TXT_Profissao = QLineEdit(self.widget_9)
        self.TXT_Profissao.setObjectName(u"TXT_Profissao")
        self.TXT_Profissao.setGeometry(QRect(5, 290, 192, 25))
        self.TXT_Profissao.setFont(font3)
        self.TXT_Profissao.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Nacionalidade = QLineEdit(self.widget_9)
        self.TXT_Nacionalidade.setObjectName(u"TXT_Nacionalidade")
        self.TXT_Nacionalidade.setGeometry(QRect(208, 290, 192, 25))
        self.TXT_Nacionalidade.setFont(font3)
        self.TXT_Nacionalidade.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Nome_Responsavel = QLineEdit(self.widget_9)
        self.TXT_Nome_Responsavel.setObjectName(u"TXT_Nome_Responsavel")
        self.TXT_Nome_Responsavel.setGeometry(QRect(5, 100, 192, 25))
        self.TXT_Nome_Responsavel.setFont(font3)
        self.TXT_Nome_Responsavel.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Data_Nasc_Responsavel = QLineEdit(self.widget_9)
        self.TXT_Data_Nasc_Responsavel.setObjectName(u"TXT_Data_Nasc_Responsavel")
        self.TXT_Data_Nasc_Responsavel.setGeometry(QRect(208, 100, 192, 25))
        self.TXT_Data_Nasc_Responsavel.setFont(font3)
        self.TXT_Data_Nasc_Responsavel.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.label_22 = QLabel(self.widget_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(5, 94, 395, 2))
        self.label_22.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(self.widget_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(5, 129, 395, 2))
        self.label_23.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_23.setAlignment(Qt.AlignCenter)
        self.TXT_Numero = QLineEdit(self.widget_9)
        self.TXT_Numero.setObjectName(u"TXT_Numero")
        self.TXT_Numero.setGeometry(QRect(340, 165, 60, 25))
        self.TXT_Numero.setFont(font3)
        self.TXT_Numero.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.widget_12 = QWidget(self.Frame_Dados_Pessoais_)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(5, 330, 405, 157))
        self.widget_12.setStyleSheet(u"border-radius:10px;")
        self.label_21 = QLabel(self.widget_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(5, 5, 395, 25))
        self.label_21.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.TXT_email_1 = QLineEdit(self.widget_12)
        self.TXT_email_1.setObjectName(u"TXT_email_1")
        self.TXT_email_1.setGeometry(QRect(5, 35, 192, 25))
        self.TXT_email_1.setFont(font3)
        self.TXT_email_1.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_email_3 = QLineEdit(self.widget_12)
        self.TXT_email_3.setObjectName(u"TXT_email_3")
        self.TXT_email_3.setGeometry(QRect(5, 95, 192, 25))
        self.TXT_email_3.setFont(font3)
        self.TXT_email_3.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_email_2 = QLineEdit(self.widget_12)
        self.TXT_email_2.setObjectName(u"TXT_email_2")
        self.TXT_email_2.setGeometry(QRect(5, 65, 192, 25))
        self.TXT_email_2.setFont(font3)
        self.TXT_email_2.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Cel_Contato_1 = QLineEdit(self.widget_12)
        self.TXT_Cel_Contato_1.setObjectName(u"TXT_Cel_Contato_1")
        self.TXT_Cel_Contato_1.setGeometry(QRect(208, 35, 192, 25))
        self.TXT_Cel_Contato_1.setFont(font3)
        self.TXT_Cel_Contato_1.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Cel_Contato_1.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.TXT_Cel_Contato_3 = QLineEdit(self.widget_12)
        self.TXT_Cel_Contato_3.setObjectName(u"TXT_Cel_Contato_3")
        self.TXT_Cel_Contato_3.setGeometry(QRect(208, 95, 192, 25))
        self.TXT_Cel_Contato_3.setFont(font3)
        self.TXT_Cel_Contato_3.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Cel_Contato_2 = QLineEdit(self.widget_12)
        self.TXT_Cel_Contato_2.setObjectName(u"TXT_Cel_Contato_2")
        self.TXT_Cel_Contato_2.setGeometry(QRect(208, 65, 192, 25))
        self.TXT_Cel_Contato_2.setFont(font3)
        self.TXT_Cel_Contato_2.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Cel_Contato_4 = QLineEdit(self.widget_12)
        self.TXT_Cel_Contato_4.setObjectName(u"TXT_Cel_Contato_4")
        self.TXT_Cel_Contato_4.setGeometry(QRect(208, 125, 192, 25))
        self.TXT_Cel_Contato_4.setFont(font3)
        self.TXT_Cel_Contato_4.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_email_4 = QLineEdit(self.widget_12)
        self.TXT_email_4.setObjectName(u"TXT_email_4")
        self.TXT_email_4.setGeometry(QRect(5, 125, 192, 25))
        self.TXT_email_4.setFont(font3)
        self.TXT_email_4.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.frame_4 = QFrame(self.Frame_Dados_Pessoais_)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 492, 415, 40))
        self.frame_4.setMaximumSize(QSize(415, 16777215))
        self.frame_4.setStyleSheet(u"border-radius:10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.BT_Descartar_D_P = QPushButton(self.frame_4)
        self.BT_Descartar_D_P.setObjectName(u"BT_Descartar_D_P")
        self.BT_Descartar_D_P.setMinimumSize(QSize(0, 20))
        self.BT_Descartar_D_P.setMaximumSize(QSize(125, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Lucida Calligraphy"])
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setItalic(False)
        self.BT_Descartar_D_P.setFont(font4)
        self.BT_Descartar_D_P.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Descartar_D_P.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Red.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_44.addWidget(self.BT_Descartar_D_P)

        self.BT_Alterar_D_P = QPushButton(self.frame_4)
        self.BT_Alterar_D_P.setObjectName(u"BT_Alterar_D_P")
        self.BT_Alterar_D_P.setMinimumSize(QSize(0, 20))
        self.BT_Alterar_D_P.setMaximumSize(QSize(125, 16777215))
        self.BT_Alterar_D_P.setFont(font4)
        self.BT_Alterar_D_P.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Alterar_D_P.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Yellow.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_44.addWidget(self.BT_Alterar_D_P)

        self.BT_Salvar_D_P = QPushButton(self.frame_4)
        self.BT_Salvar_D_P.setObjectName(u"BT_Salvar_D_P")
        self.BT_Salvar_D_P.setMinimumSize(QSize(0, 20))
        self.BT_Salvar_D_P.setMaximumSize(QSize(125, 16777215))
        self.BT_Salvar_D_P.setFont(font4)
        self.BT_Salvar_D_P.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Salvar_D_P.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Green.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_44.addWidget(self.BT_Salvar_D_P)


        self.horizontalLayout_73.addWidget(self.Frame_Dados_Pessoais_)

        self.Tbox_Cadastro.addWidget(self.Tbox_CadastroPage1)
        self.Tbox_CadastroPage2 = QWidget()
        self.Tbox_CadastroPage2.setObjectName(u"Tbox_CadastroPage2")
        self.horizontalLayout_66 = QHBoxLayout(self.Tbox_CadastroPage2)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.Frame_Historico_Medico_ = QFrame(self.Tbox_CadastroPage2)
        self.Frame_Historico_Medico_.setObjectName(u"Frame_Historico_Medico_")
        sizePolicy3.setHeightForWidth(self.Frame_Historico_Medico_.sizePolicy().hasHeightForWidth())
        self.Frame_Historico_Medico_.setSizePolicy(sizePolicy3)
        self.Frame_Historico_Medico_.setMaximumSize(QSize(415, 532))
        self.Frame_Historico_Medico_.setStyleSheet(u"QLineEdit{\n"
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
        self.Frame_Historico_Medico_.setFrameShape(QFrame.StyledPanel)
        self.Frame_Historico_Medico_.setFrameShadow(QFrame.Raised)
        self.frame_57 = QFrame(self.Frame_Historico_Medico_)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setGeometry(QRect(0, 492, 415, 40))
        self.frame_57.setMaximumSize(QSize(415, 16777215))
        self.frame_57.setStyleSheet(u"border-radius:10px;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.BT_Descartar_D_P_2 = QPushButton(self.frame_57)
        self.BT_Descartar_D_P_2.setObjectName(u"BT_Descartar_D_P_2")
        self.BT_Descartar_D_P_2.setMinimumSize(QSize(0, 20))
        self.BT_Descartar_D_P_2.setMaximumSize(QSize(125, 16777215))
        self.BT_Descartar_D_P_2.setFont(font4)
        self.BT_Descartar_D_P_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Descartar_D_P_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Red.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_50.addWidget(self.BT_Descartar_D_P_2)

        self.BT_Alterar_D_P_2 = QPushButton(self.frame_57)
        self.BT_Alterar_D_P_2.setObjectName(u"BT_Alterar_D_P_2")
        self.BT_Alterar_D_P_2.setMinimumSize(QSize(0, 20))
        self.BT_Alterar_D_P_2.setMaximumSize(QSize(125, 16777215))
        self.BT_Alterar_D_P_2.setFont(font4)
        self.BT_Alterar_D_P_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Alterar_D_P_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Yellow.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_50.addWidget(self.BT_Alterar_D_P_2)

        self.BT_Salvar_D_P_2 = QPushButton(self.frame_57)
        self.BT_Salvar_D_P_2.setObjectName(u"BT_Salvar_D_P_2")
        self.BT_Salvar_D_P_2.setMinimumSize(QSize(0, 20))
        self.BT_Salvar_D_P_2.setMaximumSize(QSize(125, 16777215))
        self.BT_Salvar_D_P_2.setFont(font4)
        self.BT_Salvar_D_P_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Salvar_D_P_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Green.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_50.addWidget(self.BT_Salvar_D_P_2)

        self.widget_13 = QWidget(self.Frame_Historico_Medico_)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(5, 5, 405, 482))
        self.widget_13.setStyleSheet(u"border-radius:10px;\n"
"")
        self.label_24 = QLabel(self.widget_13)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(5, 5, 395, 25))
        self.label_24.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_29 = QLabel(self.widget_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(5, 165, 395, 25))
        self.label_29.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_30 = QLabel(self.widget_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(5, 64, 395, 2))
        self.label_30.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_31 = QLabel(self.widget_13)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(5, 159, 395, 2))
        self.label_31.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.RBT_Alergia = QRadioButton(self.widget_13)
        self.RBT_Alergia.setObjectName(u"RBT_Alergia")
        self.RBT_Alergia.setGeometry(QRect(275, 35, 125, 25))
        self.RBT_Alergia.setCursor(QCursor(Qt.PointingHandCursor))
        self.RBT_Alergia.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.RBT_Enfermidade = QRadioButton(self.widget_13)
        self.RBT_Enfermidade.setObjectName(u"RBT_Enfermidade")
        self.RBT_Enfermidade.setGeometry(QRect(5, 35, 125, 25))
        self.RBT_Enfermidade.setFont(font3)
        self.RBT_Enfermidade.setCursor(QCursor(Qt.PointingHandCursor))
        self.RBT_Enfermidade.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.RBT_Medicamentos = QRadioButton(self.widget_13)
        self.RBT_Medicamentos.setObjectName(u"RBT_Medicamentos")
        self.RBT_Medicamentos.setGeometry(QRect(140, 35, 125, 25))
        self.RBT_Medicamentos.setCursor(QCursor(Qt.PointingHandCursor))
        self.RBT_Medicamentos.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.widget_18 = QWidget(self.widget_13)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setGeometry(QRect(0, 66, 405, 91))
        self.widget_18.setStyleSheet(u"border-radius:10px;")
        self.horizontalLayout_100 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 5, 0, 0)
        self.widget_2 = QWidget(self.widget_18)
        self.widget_2.setObjectName(u"widget_2")
        self.CB_Enf3 = QCheckBox(self.widget_2)
        self.CB_Enf3.setObjectName(u"CB_Enf3")
        self.CB_Enf3.setGeometry(QRect(5, 60, 25, 25))
        self.CB_Enf3.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Enfermidade3 = QLineEdit(self.widget_2)
        self.TXT_Enfermidade3.setObjectName(u"TXT_Enfermidade3")
        self.TXT_Enfermidade3.setEnabled(True)
        self.TXT_Enfermidade3.setGeometry(QRect(30, 60, 100, 25))
        self.TXT_Enfermidade3.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Verdana\";")
        self.CB_Enf2 = QCheckBox(self.widget_2)
        self.CB_Enf2.setObjectName(u"CB_Enf2")
        self.CB_Enf2.setGeometry(QRect(5, 30, 25, 25))
        self.CB_Enf2.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Enfermidade1 = QLineEdit(self.widget_2)
        self.TXT_Enfermidade1.setObjectName(u"TXT_Enfermidade1")
        self.TXT_Enfermidade1.setGeometry(QRect(30, 0, 100, 25))
        self.TXT_Enfermidade1.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Verdana\";")
        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(5, 0, 25, 25))
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Enfermidade2 = QLineEdit(self.widget_2)
        self.TXT_Enfermidade2.setObjectName(u"TXT_Enfermidade2")
        self.TXT_Enfermidade2.setGeometry(QRect(30, 30, 100, 25))
        self.TXT_Enfermidade2.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Verdana\";")

        self.horizontalLayout_100.addWidget(self.widget_2)

        self.widget_16 = QWidget(self.widget_18)
        self.widget_16.setObjectName(u"widget_16")
        self.CB_Rem3 = QCheckBox(self.widget_16)
        self.CB_Rem3.setObjectName(u"CB_Rem3")
        self.CB_Rem3.setGeometry(QRect(5, 60, 25, 25))
        self.CB_Rem3.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Medicamento3 = QLineEdit(self.widget_16)
        self.TXT_Medicamento3.setObjectName(u"TXT_Medicamento3")
        self.TXT_Medicamento3.setEnabled(True)
        self.TXT_Medicamento3.setGeometry(QRect(30, 60, 100, 25))
        self.TXT_Medicamento3.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Verdana\";")
        self.CB_Rem2 = QCheckBox(self.widget_16)
        self.CB_Rem2.setObjectName(u"CB_Rem2")
        self.CB_Rem2.setGeometry(QRect(5, 30, 25, 25))
        self.CB_Rem2.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Medicamento1 = QLineEdit(self.widget_16)
        self.TXT_Medicamento1.setObjectName(u"TXT_Medicamento1")
        self.TXT_Medicamento1.setGeometry(QRect(30, 0, 100, 25))
        self.TXT_Medicamento1.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Verdana\";")
        self.CB_Rem1 = QCheckBox(self.widget_16)
        self.CB_Rem1.setObjectName(u"CB_Rem1")
        self.CB_Rem1.setGeometry(QRect(5, 0, 25, 25))
        self.CB_Rem1.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Medicamento2 = QLineEdit(self.widget_16)
        self.TXT_Medicamento2.setObjectName(u"TXT_Medicamento2")
        self.TXT_Medicamento2.setGeometry(QRect(30, 30, 100, 25))
        self.TXT_Medicamento2.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Verdana\";")

        self.horizontalLayout_100.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_18)
        self.widget_17.setObjectName(u"widget_17")
        self.CB_Alerg3 = QCheckBox(self.widget_17)
        self.CB_Alerg3.setObjectName(u"CB_Alerg3")
        self.CB_Alerg3.setGeometry(QRect(5, 60, 25, 25))
        self.CB_Alerg3.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Medicamento3_2 = QLineEdit(self.widget_17)
        self.TXT_Medicamento3_2.setObjectName(u"TXT_Medicamento3_2")
        self.TXT_Medicamento3_2.setEnabled(True)
        self.TXT_Medicamento3_2.setGeometry(QRect(30, 60, 100, 25))
        self.TXT_Medicamento3_2.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Verdana\";")
        self.CB_Alerg2 = QCheckBox(self.widget_17)
        self.CB_Alerg2.setObjectName(u"CB_Alerg2")
        self.CB_Alerg2.setGeometry(QRect(5, 30, 25, 25))
        self.CB_Alerg2.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Alergia1 = QLineEdit(self.widget_17)
        self.TXT_Alergia1.setObjectName(u"TXT_Alergia1")
        self.TXT_Alergia1.setGeometry(QRect(30, 0, 100, 25))
        self.TXT_Alergia1.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Verdana\";")
        self.CB_Alerg1 = QCheckBox(self.widget_17)
        self.CB_Alerg1.setObjectName(u"CB_Alerg1")
        self.CB_Alerg1.setGeometry(QRect(5, 0, 25, 25))
        self.CB_Alerg1.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Alergia2 = QLineEdit(self.widget_17)
        self.TXT_Alergia2.setObjectName(u"TXT_Alergia2")
        self.TXT_Alergia2.setGeometry(QRect(30, 30, 100, 25))
        self.TXT_Alergia2.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Verdana\";")

        self.horizontalLayout_100.addWidget(self.widget_17)


        self.horizontalLayout_66.addWidget(self.Frame_Historico_Medico_)

        self.Tbox_Cadastro.addWidget(self.Tbox_CadastroPage2)
        self.Tbox_CadastroPage3 = QWidget()
        self.Tbox_CadastroPage3.setObjectName(u"Tbox_CadastroPage3")
        self.horizontalLayout_5 = QHBoxLayout(self.Tbox_CadastroPage3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_18 = QFrame(self.Tbox_CadastroPage3)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy3.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy3)
        self.frame_18.setMaximumSize(QSize(415, 532))
        self.frame_18.setStyleSheet(u"QLineEdit{\n"
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
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_18)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 492, 415, 40))
        self.frame_7.setMaximumSize(QSize(415, 16777215))
        self.frame_7.setStyleSheet(u"border-radius:10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.BT_Descartar_D_P_3 = QPushButton(self.frame_7)
        self.BT_Descartar_D_P_3.setObjectName(u"BT_Descartar_D_P_3")
        self.BT_Descartar_D_P_3.setMinimumSize(QSize(0, 20))
        self.BT_Descartar_D_P_3.setMaximumSize(QSize(125, 16777215))
        self.BT_Descartar_D_P_3.setFont(font4)
        self.BT_Descartar_D_P_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Descartar_D_P_3.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Red.jpg);\n"
"color:rgb(255,255,255);\n"
"border:15px;\n"
"}")

        self.horizontalLayout_60.addWidget(self.BT_Descartar_D_P_3)

        self.BT_Alterar_D_P_3 = QPushButton(self.frame_7)
        self.BT_Alterar_D_P_3.setObjectName(u"BT_Alterar_D_P_3")
        self.BT_Alterar_D_P_3.setMinimumSize(QSize(0, 20))
        self.BT_Alterar_D_P_3.setMaximumSize(QSize(125, 16777215))
        self.BT_Alterar_D_P_3.setFont(font4)
        self.BT_Alterar_D_P_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Alterar_D_P_3.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Yellow.jpg);\n"
"color:rgb(255,255,255);\n"
"border:10px;\n"
"}")

        self.horizontalLayout_60.addWidget(self.BT_Alterar_D_P_3)

        self.BT_Salvar_D_P_3 = QPushButton(self.frame_7)
        self.BT_Salvar_D_P_3.setObjectName(u"BT_Salvar_D_P_3")
        self.BT_Salvar_D_P_3.setMinimumSize(QSize(0, 20))
        self.BT_Salvar_D_P_3.setMaximumSize(QSize(125, 16777215))
        self.BT_Salvar_D_P_3.setFont(font4)
        self.BT_Salvar_D_P_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Salvar_D_P_3.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Green.jpg);\n"
"color:rgb(255,255,255);\n"
"border3px;\n"
"}")

        self.horizontalLayout_60.addWidget(self.BT_Salvar_D_P_3)

        self.widget_6 = QWidget(self.frame_18)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(5, 5, 405, 482))
        self.widget_6.setStyleSheet(u"border-radius:10px;")
        self.label_25 = QLabel(self.widget_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(5, 5, 395, 25))
        self.label_25.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.TXT_Nome_Razao = QLineEdit(self.widget_6)
        self.TXT_Nome_Razao.setObjectName(u"TXT_Nome_Razao")
        self.TXT_Nome_Razao.setGeometry(QRect(5, 35, 395, 25))
        self.TXT_Nome_Razao.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_CNPJ_CPF = QLineEdit(self.widget_6)
        self.TXT_CNPJ_CPF.setObjectName(u"TXT_CNPJ_CPF")
        self.TXT_CNPJ_CPF.setGeometry(QRect(207, 95, 192, 25))
        self.TXT_CNPJ_CPF.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Nome_Razao_2 = QLineEdit(self.widget_6)
        self.TXT_Nome_Razao_2.setObjectName(u"TXT_Nome_Razao_2")
        self.TXT_Nome_Razao_2.setGeometry(QRect(5, 95, 192, 25))
        self.TXT_Nome_Razao_2.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Instituicao = QLineEdit(self.widget_6)
        self.TXT_Instituicao.setObjectName(u"TXT_Instituicao")
        self.TXT_Instituicao.setGeometry(QRect(5, 65, 395, 25))
        self.TXT_Instituicao.setStyleSheet(u"font: 8pt \"Verdana\";")

        self.horizontalLayout_5.addWidget(self.frame_18)

        self.Tbox_Cadastro.addWidget(self.Tbox_CadastroPage3)
        self.Tbox_CadastroPage4 = QWidget()
        self.Tbox_CadastroPage4.setObjectName(u"Tbox_CadastroPage4")
        self.horizontalLayout_12 = QHBoxLayout(self.Tbox_CadastroPage4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_19 = QFrame(self.Tbox_CadastroPage4)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy5)
        self.frame_19.setMaximumSize(QSize(415, 532))
        self.frame_19.setStyleSheet(u"QLineEdit{\n"
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
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_59 = QFrame(self.frame_19)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setGeometry(QRect(0, 492, 415, 40))
        self.frame_59.setMaximumSize(QSize(415, 16777215))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.BT_Descartar_D_P_4 = QPushButton(self.frame_59)
        self.BT_Descartar_D_P_4.setObjectName(u"BT_Descartar_D_P_4")
        self.BT_Descartar_D_P_4.setMinimumSize(QSize(0, 20))
        self.BT_Descartar_D_P_4.setMaximumSize(QSize(125, 16777215))
        self.BT_Descartar_D_P_4.setFont(font4)
        self.BT_Descartar_D_P_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Descartar_D_P_4.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Red.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_67.addWidget(self.BT_Descartar_D_P_4)

        self.BT_Alterar_D_P_4 = QPushButton(self.frame_59)
        self.BT_Alterar_D_P_4.setObjectName(u"BT_Alterar_D_P_4")
        self.BT_Alterar_D_P_4.setMinimumSize(QSize(0, 20))
        self.BT_Alterar_D_P_4.setMaximumSize(QSize(125, 16777215))
        self.BT_Alterar_D_P_4.setFont(font4)
        self.BT_Alterar_D_P_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Alterar_D_P_4.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Yellow.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_67.addWidget(self.BT_Alterar_D_P_4)

        self.BT_Salvar_D_P_4 = QPushButton(self.frame_59)
        self.BT_Salvar_D_P_4.setObjectName(u"BT_Salvar_D_P_4")
        self.BT_Salvar_D_P_4.setMinimumSize(QSize(0, 20))
        self.BT_Salvar_D_P_4.setMaximumSize(QSize(125, 16777215))
        self.BT_Salvar_D_P_4.setFont(font4)
        self.BT_Salvar_D_P_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Salvar_D_P_4.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Green.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_67.addWidget(self.BT_Salvar_D_P_4)

        self.widget_14 = QWidget(self.frame_19)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setGeometry(QRect(5, 5, 405, 482))
        self.widget_14.setStyleSheet(u"border-radius:10px;")
        self.label_32 = QLabel(self.widget_14)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(5, 5, 395, 25))
        self.label_32.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_32.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.widget_14)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(5, 35, 395, 442))
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 70, 192, 121))
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.label_34 = QLabel(self.widget_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 25))
        self.label_34.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_34)

        self.TXT_Nome_Razao_3 = QLineEdit(self.widget_3)
        self.TXT_Nome_Razao_3.setObjectName(u"TXT_Nome_Razao_3")
        self.TXT_Nome_Razao_3.setMinimumSize(QSize(192, 25))
        self.TXT_Nome_Razao_3.setMaximumSize(QSize(192, 25))
        self.TXT_Nome_Razao_3.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Nome_Razao_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.TXT_Nome_Razao_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(202, 70, 192, 121))
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.label_35 = QLabel(self.widget_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 25))
        self.label_35.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_35)

        self.TXT_Nome_Razao_4 = QLineEdit(self.widget_5)
        self.TXT_Nome_Razao_4.setObjectName(u"TXT_Nome_Razao_4")
        self.TXT_Nome_Razao_4.setMinimumSize(QSize(192, 25))
        self.TXT_Nome_Razao_4.setMaximumSize(QSize(192, 25))
        self.TXT_Nome_Razao_4.setStyleSheet(u"font: 8pt \"Verdana\";")
        self.TXT_Nome_Razao_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.TXT_Nome_Razao_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_12.addWidget(self.frame_19)

        self.Tbox_Cadastro.addWidget(self.Tbox_CadastroPage4)
        self.Tbox_CadastroPage5 = QWidget()
        self.Tbox_CadastroPage5.setObjectName(u"Tbox_CadastroPage5")
        self.horizontalLayout_2 = QHBoxLayout(self.Tbox_CadastroPage5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_39 = QFrame(self.Tbox_CadastroPage5)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy5.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy5)
        self.frame_39.setMaximumSize(QSize(415, 532))
        self.frame_39.setStyleSheet(u"QLineEdit{\n"
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
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.frame_60 = QFrame(self.frame_39)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setGeometry(QRect(0, 492, 415, 40))
        self.frame_60.setMaximumSize(QSize(415, 16777215))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.BT_Descartar_D_P_5 = QPushButton(self.frame_60)
        self.BT_Descartar_D_P_5.setObjectName(u"BT_Descartar_D_P_5")
        self.BT_Descartar_D_P_5.setMinimumSize(QSize(0, 20))
        self.BT_Descartar_D_P_5.setMaximumSize(QSize(125, 16777215))
        self.BT_Descartar_D_P_5.setFont(font4)
        self.BT_Descartar_D_P_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Descartar_D_P_5.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Red.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_77.addWidget(self.BT_Descartar_D_P_5)

        self.BT_Alterar_D_P_5 = QPushButton(self.frame_60)
        self.BT_Alterar_D_P_5.setObjectName(u"BT_Alterar_D_P_5")
        self.BT_Alterar_D_P_5.setMinimumSize(QSize(0, 20))
        self.BT_Alterar_D_P_5.setMaximumSize(QSize(125, 16777215))
        self.BT_Alterar_D_P_5.setFont(font4)
        self.BT_Alterar_D_P_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Alterar_D_P_5.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Yellow.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_77.addWidget(self.BT_Alterar_D_P_5)

        self.BT_Salvar_D_P_5 = QPushButton(self.frame_60)
        self.BT_Salvar_D_P_5.setObjectName(u"BT_Salvar_D_P_5")
        self.BT_Salvar_D_P_5.setMinimumSize(QSize(0, 20))
        self.BT_Salvar_D_P_5.setMaximumSize(QSize(125, 16777215))
        self.BT_Salvar_D_P_5.setFont(font4)
        self.BT_Salvar_D_P_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_Salvar_D_P_5.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 85, 255);\n"
"font: 9pt \"Lucida Calligraphy\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Green.jpg);\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_77.addWidget(self.BT_Salvar_D_P_5)

        self.widget_15 = QWidget(self.frame_39)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(5, 5, 405, 482))
        self.widget_15.setStyleSheet(u"border-radius:10px;")
        self.label_33 = QLabel(self.widget_15)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(5, 5, 395, 25))
        self.label_33.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_33.setAlignment(Qt.AlignCenter)
        self.fontComboBox = QFontComboBox(self.widget_15)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setGeometry(QRect(5, 35, 111, 21))

        self.horizontalLayout_2.addWidget(self.frame_39)

        self.Tbox_Cadastro.addWidget(self.Tbox_CadastroPage5)

        self.gridLayout_5.addWidget(self.Tbox_Cadastro, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.Frame_USER)

        self.frame_Progresso_Cadastro = QFrame(Form_dadosPessoais)
        self.frame_Progresso_Cadastro.setObjectName(u"frame_Progresso_Cadastro")
        self.frame_Progresso_Cadastro.setEnabled(False)
        sizePolicy.setHeightForWidth(self.frame_Progresso_Cadastro.sizePolicy().hasHeightForWidth())
        self.frame_Progresso_Cadastro.setSizePolicy(sizePolicy)
        self.frame_Progresso_Cadastro.setMinimumSize(QSize(40, 100))
        self.frame_Progresso_Cadastro.setMaximumSize(QSize(40, 16777215))
        self.frame_Progresso_Cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_Progresso_Cadastro.setFrameShadow(QFrame.Raised)
        self.LBL_ProgressoON_1 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_ProgressoON_1.setObjectName(u"LBL_ProgressoON_1")
        self.LBL_ProgressoON_1.setEnabled(False)
        self.LBL_ProgressoON_1.setGeometry(QRect(15, 0, 10, 150))
        self.LBL_ProgressoON_1.setMinimumSize(QSize(10, 150))
        self.LBL_ProgressoON_1.setMaximumSize(QSize(10, 150))
        self.LBL_ProgressoON_1.setStyleSheet(u"")
        self.LBL_ProgressoON_2 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_ProgressoON_2.setObjectName(u"LBL_ProgressoON_2")
        self.LBL_ProgressoON_2.setEnabled(False)
        self.LBL_ProgressoON_2.setGeometry(QRect(15, 150, 10, 150))
        self.LBL_ProgressoON_2.setMinimumSize(QSize(10, 150))
        self.LBL_ProgressoON_2.setMaximumSize(QSize(10, 150))
        self.LBL_ProgressoON_2.setStyleSheet(u"")
        self.LBL_ProgressoOFF_1 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_ProgressoOFF_1.setObjectName(u"LBL_ProgressoOFF_1")
        self.LBL_ProgressoOFF_1.setEnabled(False)
        self.LBL_ProgressoOFF_1.setGeometry(QRect(15, 0, 10, 150))
        self.LBL_ProgressoOFF_1.setMinimumSize(QSize(10, 150))
        self.LBL_ProgressoOFF_1.setMaximumSize(QSize(10, 150))
        self.LBL_ProgressoOFF_1.setStyleSheet(u"")
        self.LBL_ProgressoOFF_2 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_ProgressoOFF_2.setObjectName(u"LBL_ProgressoOFF_2")
        self.LBL_ProgressoOFF_2.setEnabled(False)
        self.LBL_ProgressoOFF_2.setGeometry(QRect(15, 150, 10, 150))
        self.LBL_ProgressoOFF_2.setMinimumSize(QSize(10, 150))
        self.LBL_ProgressoOFF_2.setMaximumSize(QSize(10, 150))
        self.LBL_ProgressoOFF_2.setStyleSheet(u"")
        self.LBL_ProgressoON_3 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_ProgressoON_3.setObjectName(u"LBL_ProgressoON_3")
        self.LBL_ProgressoON_3.setEnabled(False)
        self.LBL_ProgressoON_3.setGeometry(QRect(15, 300, 10, 150))
        self.LBL_ProgressoON_3.setMinimumSize(QSize(10, 150))
        self.LBL_ProgressoON_3.setMaximumSize(QSize(10, 150))
        self.LBL_ProgressoON_3.setStyleSheet(u"")
        self.LBL_ProgressoOFF_3 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_ProgressoOFF_3.setObjectName(u"LBL_ProgressoOFF_3")
        self.LBL_ProgressoOFF_3.setEnabled(False)
        self.LBL_ProgressoOFF_3.setGeometry(QRect(15, 300, 10, 150))
        self.LBL_ProgressoOFF_3.setMinimumSize(QSize(10, 150))
        self.LBL_ProgressoOFF_3.setMaximumSize(QSize(10, 150))
        self.LBL_ProgressoOFF_3.setStyleSheet(u"")
        self.LBL_ProgressoON_4 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_ProgressoON_4.setObjectName(u"LBL_ProgressoON_4")
        self.LBL_ProgressoON_4.setEnabled(False)
        self.LBL_ProgressoON_4.setGeometry(QRect(15, 450, 10, 150))
        self.LBL_ProgressoON_4.setMinimumSize(QSize(10, 150))
        self.LBL_ProgressoON_4.setMaximumSize(QSize(10, 150))
        self.LBL_ProgressoON_4.setStyleSheet(u"")
        self.LBL_ProgressoOFF_4 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_ProgressoOFF_4.setObjectName(u"LBL_ProgressoOFF_4")
        self.LBL_ProgressoOFF_4.setEnabled(False)
        self.LBL_ProgressoOFF_4.setGeometry(QRect(15, 450, 10, 150))
        self.LBL_ProgressoOFF_4.setMinimumSize(QSize(10, 150))
        self.LBL_ProgressoOFF_4.setMaximumSize(QSize(10, 150))
        self.LBL_ProgressoOFF_4.setStyleSheet(u"")
        self.LBL_StageON_1 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_StageON_1.setObjectName(u"LBL_StageON_1")
        self.LBL_StageON_1.setEnabled(False)
        self.LBL_StageON_1.setGeometry(QRect(0, 130, 40, 30))
        self.LBL_StageON_1.setMinimumSize(QSize(40, 0))
        self.LBL_StageON_1.setMaximumSize(QSize(40, 30))
        self.LBL_StageON_1.setStyleSheet(u"")
        self.LBL_StageON_2 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_StageON_2.setObjectName(u"LBL_StageON_2")
        self.LBL_StageON_2.setEnabled(False)
        self.LBL_StageON_2.setGeometry(QRect(0, 280, 40, 30))
        self.LBL_StageON_2.setMinimumSize(QSize(40, 0))
        self.LBL_StageON_2.setMaximumSize(QSize(40, 30))
        self.LBL_StageON_2.setStyleSheet(u"")
        self.LBL_StageON_3 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_StageON_3.setObjectName(u"LBL_StageON_3")
        self.LBL_StageON_3.setEnabled(False)
        self.LBL_StageON_3.setGeometry(QRect(0, 430, 40, 30))
        self.LBL_StageON_3.setMinimumSize(QSize(40, 0))
        self.LBL_StageON_3.setMaximumSize(QSize(40, 30))
        self.LBL_StageON_3.setStyleSheet(u"")
        self.LBL_StageON_4 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_StageON_4.setObjectName(u"LBL_StageON_4")
        self.LBL_StageON_4.setEnabled(False)
        self.LBL_StageON_4.setGeometry(QRect(0, 580, 40, 30))
        self.LBL_StageON_4.setMinimumSize(QSize(40, 0))
        self.LBL_StageON_4.setMaximumSize(QSize(40, 30))
        self.LBL_StageON_4.setStyleSheet(u"")
        self.LBL_StageOFF_1 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_StageOFF_1.setObjectName(u"LBL_StageOFF_1")
        self.LBL_StageOFF_1.setEnabled(False)
        self.LBL_StageOFF_1.setGeometry(QRect(0, 130, 40, 30))
        self.LBL_StageOFF_1.setMinimumSize(QSize(40, 0))
        self.LBL_StageOFF_1.setMaximumSize(QSize(40, 30))
        self.LBL_StageOFF_1.setStyleSheet(u"background-image: url(:/Info/Icons/Infos/Andamento_OFF.png);")
        self.LBL_StageOFF_2 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_StageOFF_2.setObjectName(u"LBL_StageOFF_2")
        self.LBL_StageOFF_2.setEnabled(False)
        self.LBL_StageOFF_2.setGeometry(QRect(0, 280, 40, 30))
        self.LBL_StageOFF_2.setMinimumSize(QSize(40, 0))
        self.LBL_StageOFF_2.setMaximumSize(QSize(40, 30))
        self.LBL_StageOFF_2.setStyleSheet(u"background-image: url(:/Info/Icons/Infos/Andamento_OFF.png);")
        self.LBL_StageOFF_3 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_StageOFF_3.setObjectName(u"LBL_StageOFF_3")
        self.LBL_StageOFF_3.setEnabled(False)
        self.LBL_StageOFF_3.setGeometry(QRect(0, 430, 40, 30))
        self.LBL_StageOFF_3.setMinimumSize(QSize(40, 0))
        self.LBL_StageOFF_3.setMaximumSize(QSize(40, 30))
        self.LBL_StageOFF_3.setStyleSheet(u"background-image: url(:/Info/Icons/Infos/Andamento_OFF.png);")
        self.LBL_StageOFF_4 = QLabel(self.frame_Progresso_Cadastro)
        self.LBL_StageOFF_4.setObjectName(u"LBL_StageOFF_4")
        self.LBL_StageOFF_4.setEnabled(False)
        self.LBL_StageOFF_4.setGeometry(QRect(0, 580, 40, 30))
        self.LBL_StageOFF_4.setMinimumSize(QSize(40, 0))
        self.LBL_StageOFF_4.setMaximumSize(QSize(40, 30))
        self.LBL_StageOFF_4.setStyleSheet(u"background-image: url(:/Info/Icons/Infos/Andamento_OFF.png);")

        self.horizontalLayout.addWidget(self.frame_Progresso_Cadastro)


        self.retranslateUi(Form_dadosPessoais)

        self.Tbox_Cadastro.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form_dadosPessoais)
    # setupUi

    def retranslateUi(self, Form_dadosPessoais):
        Form_dadosPessoais.setWindowTitle(QCoreApplication.translate("Form_dadosPessoais", u"Form", None))
        self.btCad_Left_LIG_01.setText("")
        self.btCad_Left_DESL_01.setText("")
        self.btCad_Left_LIG_02.setText("")
        self.btCad_Left_DESL_02.setText("")
        self.btCad_Left_LIG_03.setText("")
        self.btCad_Left_DESL_03.setText("")
        self.btCad_Left_LIG_04.setText("")
        self.btCad_Left_DESL_04.setText("")
        self.btCad_Left_LIG_05.setText("")
        self.btCad_Left_DESL_05.setText("")
        self.BT_Cad_Left_LIGAR.setText("")
        self.BT_Cad_Left_DESLIGAR.setText("")
        self.LBL_AddCadastro.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_NovoCadastro.png\"/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.Tbox_Cadastro.setToolTip(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Tbox_Cadastro.setWhatsThis(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.Tela_Inicio.setWhatsThis(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p><img src=\":/Backgrounds/Icons/Backgrounds/Imagem4.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Tela_Inicio.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Backgrounds/Icons/Logos/Icon_Menu2.png\"/></p></body></html>", None))
        self.BT_sexo_Fem.setText(QCoreApplication.translate("Form_dadosPessoais", u"Feminino", None))
        self.BT_sexo_Outros.setText(QCoreApplication.translate("Form_dadosPessoais", u"Outros", None))
        self.BT_sexo_Masc.setText(QCoreApplication.translate("Form_dadosPessoais", u"Masculino", None))
        self.label_5.setText(QCoreApplication.translate("Form_dadosPessoais", u"G\u00eanero ", None))
        self.BT_sexo_Ocultar.setText(QCoreApplication.translate("Form_dadosPessoais", u"N/A", None))
        self.label_6.setText(QCoreApplication.translate("Form_dadosPessoais", u"Dados Pessoais", None))
        self.TXT_Nome_Completo.setText("")
        self.TXT_Nome_Completo.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Nome Completo...", None))
        self.TXT_CPF.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"CPF...", None))
        self.TXT_RG.setText("")
        self.TXT_RG.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"RG...", None))
        self.TXT_Data_Nasc.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Data Nascimento...", None))
        self.TXT_Municipio.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Munic\u00edpio...", None))
        self.TXT_Logradouro.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Logradouro...", None))
        self.TXT_Complemento_Log.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Complemento...", None))
        self.label_7.setText(QCoreApplication.translate("Form_dadosPessoais", u"Endere\u00e7o", None))
        self.TXT_CEP.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"CEP...", None))
        self.TXT_Cidade.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Cidade...", None))
        self.TXT_Estado.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Estado...", None))
        self.label_8.setText(QCoreApplication.translate("Form_dadosPessoais", u"Outros ", None))
        self.TXT_Profissao.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Profiss\u00e3o...", None))
        self.TXT_Nacionalidade.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Nacionalidade...", None))
        self.TXT_Nome_Responsavel.setText("")
        self.TXT_Nome_Responsavel.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Nome do respons\u00e1vel...", None))
        self.TXT_Data_Nasc_Responsavel.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Data Nascimento...", None))
        self.label_22.setText("")
        self.label_23.setText("")
        self.TXT_Numero.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"n\u00b0...", None))
        self.label_21.setText(QCoreApplication.translate("Form_dadosPessoais", u"Contato ", None))
        self.TXT_email_1.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Email...", None))
        self.TXT_email_3.setText("")
        self.TXT_email_3.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Email...", None))
        self.TXT_email_2.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Email...", None))
        self.TXT_Cel_Contato_1.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"55(xx) - 9xxxx-xxxx", None))
        self.TXT_Cel_Contato_3.setText("")
        self.TXT_Cel_Contato_3.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"55(xx) - 9xxxx-xxxx", None))
        self.TXT_Cel_Contato_2.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"55(xx) - 9xxxx-xxxx", None))
        self.TXT_Cel_Contato_4.setText("")
        self.TXT_Cel_Contato_4.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"55(xx) - 9xxxx-xxxx", None))
        self.TXT_email_4.setText("")
        self.TXT_email_4.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Email...", None))
        self.BT_Descartar_D_P.setText(QCoreApplication.translate("Form_dadosPessoais", u"Descartar", None))
        self.BT_Alterar_D_P.setText(QCoreApplication.translate("Form_dadosPessoais", u"Alterar", None))
        self.BT_Salvar_D_P.setText(QCoreApplication.translate("Form_dadosPessoais", u"Salvar", None))
        self.BT_Descartar_D_P_2.setText(QCoreApplication.translate("Form_dadosPessoais", u"Descartar", None))
        self.BT_Alterar_D_P_2.setText(QCoreApplication.translate("Form_dadosPessoais", u"Alterar", None))
        self.BT_Salvar_D_P_2.setText(QCoreApplication.translate("Form_dadosPessoais", u"Salvar", None))
        self.label_24.setText(QCoreApplication.translate("Form_dadosPessoais", u"Hist\u00f3rico m\u00e9dico", None))
        self.label_29.setText(QCoreApplication.translate("Form_dadosPessoais", u"Outros ", None))
        self.label_30.setText("")
        self.label_31.setText("")
        self.RBT_Alergia.setText(QCoreApplication.translate("Form_dadosPessoais", u"Alergia", None))
        self.RBT_Enfermidade.setText(QCoreApplication.translate("Form_dadosPessoais", u"Enfermidade", None))
        self.RBT_Medicamentos.setText(QCoreApplication.translate("Form_dadosPessoais", u"Medicamento", None))
        self.CB_Enf3.setText("")
        self.TXT_Enfermidade3.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Enfermidade 3", None))
        self.CB_Enf2.setText("")
        self.TXT_Enfermidade1.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Enfermidade 1", None))
        self.checkBox.setText("")
        self.TXT_Enfermidade2.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Enfermidade 2", None))
        self.CB_Rem3.setText("")
        self.TXT_Medicamento3.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Medicamento 3", None))
        self.CB_Rem2.setText("")
        self.TXT_Medicamento1.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Medicamento 1", None))
        self.CB_Rem1.setText("")
        self.TXT_Medicamento2.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Medicamento 2", None))
        self.CB_Alerg3.setText("")
        self.TXT_Medicamento3_2.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Medicamento 3", None))
        self.CB_Alerg2.setText("")
        self.TXT_Alergia1.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Medicamento 1", None))
        self.CB_Alerg1.setText("")
        self.TXT_Alergia2.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Medicamento 2", None))
        self.BT_Descartar_D_P_3.setText(QCoreApplication.translate("Form_dadosPessoais", u"Descartar", None))
        self.BT_Alterar_D_P_3.setText(QCoreApplication.translate("Form_dadosPessoais", u"Alterar", None))
        self.BT_Salvar_D_P_3.setText(QCoreApplication.translate("Form_dadosPessoais", u"Salvar", None))
        self.label_25.setText(QCoreApplication.translate("Form_dadosPessoais", u"Conv\u00eanio associado", None))
        self.TXT_Nome_Razao.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Nome / Raz\u00e3o", None))
        self.TXT_CNPJ_CPF.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"CPF / CNPJ", None))
        self.TXT_Nome_Razao_2.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Plano", None))
        self.TXT_Instituicao.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Institui\u00e7\u00e3o", None))
        self.BT_Descartar_D_P_4.setText(QCoreApplication.translate("Form_dadosPessoais", u"Or\u00e7amentos", None))
        self.BT_Alterar_D_P_4.setText(QCoreApplication.translate("Form_dadosPessoais", u"Recibos", None))
        self.BT_Salvar_D_P_4.setText(QCoreApplication.translate("Form_dadosPessoais", u"Boletos", None))
        self.label_32.setText(QCoreApplication.translate("Form_dadosPessoais", u"Financeiro", None))
        self.label_34.setText(QCoreApplication.translate("Form_dadosPessoais", u"Ordem de Servi\u00e7o", None))
        self.TXT_Nome_Razao_3.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Nome / Raz\u00e3o", None))
        self.label_35.setText(QCoreApplication.translate("Form_dadosPessoais", u"Boletos", None))
        self.TXT_Nome_Razao_4.setPlaceholderText(QCoreApplication.translate("Form_dadosPessoais", u"Nome / Raz\u00e3o", None))
        self.BT_Descartar_D_P_5.setText(QCoreApplication.translate("Form_dadosPessoais", u"Or\u00e7amentos", None))
        self.BT_Alterar_D_P_5.setText(QCoreApplication.translate("Form_dadosPessoais", u"Recibos", None))
        self.BT_Salvar_D_P_5.setText(QCoreApplication.translate("Form_dadosPessoais", u"Boletos", None))
        self.label_33.setText(QCoreApplication.translate("Form_dadosPessoais", u"Pesquisa", None))
        self.LBL_ProgressoON_1.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Progresso_ON.png\"/></p></body></html>", None))
        self.LBL_ProgressoON_2.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Progresso_ON.png\"/></p></body></html>", None))
        self.LBL_ProgressoOFF_1.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Progresso_OFF.png\"/></p></body></html>", None))
        self.LBL_ProgressoOFF_2.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Progresso_OFF.png\"/></p></body></html>", None))
        self.LBL_ProgressoON_3.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Progresso_ON.png\"/></p></body></html>", None))
        self.LBL_ProgressoOFF_3.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Progresso_OFF.png\"/></p></body></html>", None))
        self.LBL_ProgressoON_4.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Progresso_ON.png\"/></p></body></html>", None))
        self.LBL_ProgressoOFF_4.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Progresso_OFF.png\"/></p></body></html>", None))
        self.LBL_StageON_1.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Andamento_ON.png\"/></p></body></html>", None))
        self.LBL_StageON_2.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Andamento_ON.png\"/></p></body></html>", None))
        self.LBL_StageON_3.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Andamento_ON.png\"/></p></body></html>", None))
        self.LBL_StageON_4.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><img src=\":/Info/Icons/Infos/Andamento_ON.png\"/></p></body></html>", None))
        self.LBL_StageOFF_1.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.LBL_StageOFF_2.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.LBL_StageOFF_3.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.LBL_StageOFF_4.setText(QCoreApplication.translate("Form_dadosPessoais", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

