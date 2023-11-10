# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_Tela_05.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import Title_rc
import Logo_rc
import BT_s_rc
import Infos_rc
import Background_rc

class Ui_Form_Pacientes(object):
    def setupUi(self, Form_Pacientes):
        if not Form_Pacientes.objectName():
            Form_Pacientes.setObjectName(u"Form_Pacientes")
        Form_Pacientes.resize(909, 644)
        Form_Pacientes.setStyleSheet(u"background-color: rgb(193, 237, 255);")
        self.horizontalLayout_6 = QHBoxLayout(Form_Pacientes)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_8 = QWidget(Form_Pacientes)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.frameAgenda_BTs_1 = QFrame(self.widget_8)
        self.frameAgenda_BTs_1.setObjectName(u"frameAgenda_BTs_1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameAgenda_BTs_1.sizePolicy().hasHeightForWidth())
        self.frameAgenda_BTs_1.setSizePolicy(sizePolicy)
        self.frameAgenda_BTs_1.setMinimumSize(QSize(0, 0))
        self.frameAgenda_BTs_1.setMaximumSize(QSize(180, 16777215))
        self.frameAgenda_BTs_1.setStyleSheet(u"border-radius:20px;")
        self.frameAgenda_BTs_1.setFrameShape(QFrame.StyledPanel)
        self.frameAgenda_BTs_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameAgenda_BTs_1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.fCadastro_Left_Opened_2 = QFrame(self.frameAgenda_BTs_1)
        self.fCadastro_Left_Opened_2.setObjectName(u"fCadastro_Left_Opened_2")
        sizePolicy.setHeightForWidth(self.fCadastro_Left_Opened_2.sizePolicy().hasHeightForWidth())
        self.fCadastro_Left_Opened_2.setSizePolicy(sizePolicy)
        self.fCadastro_Left_Opened_2.setMinimumSize(QSize(60, 500))
        self.fCadastro_Left_Opened_2.setMaximumSize(QSize(0, 16777215))
        self.fCadastro_Left_Opened_2.setStyleSheet(u"")
        self.fCadastro_Left_Opened_2.setFrameShape(QFrame.StyledPanel)
        self.fCadastro_Left_Opened_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.fCadastro_Left_Opened_2)
        self.verticalLayout_56.setSpacing(5)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(5, 5, 5, 0)
        self.fCad_Left_2 = QFrame(self.fCadastro_Left_Opened_2)
        self.fCad_Left_2.setObjectName(u"fCad_Left_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.fCad_Left_2.sizePolicy().hasHeightForWidth())
        self.fCad_Left_2.setSizePolicy(sizePolicy1)
        self.fCad_Left_2.setMinimumSize(QSize(0, 0))
        self.fCad_Left_2.setMaximumSize(QSize(50, 50))
        self.fCad_Left_2.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.fCad_Left_2)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_13 = QFrame(self.fCad_Left_2)
        self.fCad_Left_13.setObjectName(u"fCad_Left_13")
        sizePolicy1.setHeightForWidth(self.fCad_Left_13.sizePolicy().hasHeightForWidth())
        self.fCad_Left_13.setSizePolicy(sizePolicy1)
        self.fCad_Left_13.setMinimumSize(QSize(0, 0))
        self.fCad_Left_13.setMaximumSize(QSize(0, 50))
        self.fCad_Left_13.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.fCad_Left_13)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_2 = QPushButton(self.fCad_Left_13)
        self.btCad_Left_LIG_2.setObjectName(u"btCad_Left_LIG_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btCad_Left_LIG_2.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_2.setSizePolicy(sizePolicy2)
        self.btCad_Left_LIG_2.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_2.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_2.setStyleSheet(u"\n"
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

        self.horizontalLayout_73.addWidget(self.btCad_Left_LIG_2)


        self.horizontalLayout_48.addWidget(self.fCad_Left_13)

        self.fCad_Left_14 = QFrame(self.fCad_Left_2)
        self.fCad_Left_14.setObjectName(u"fCad_Left_14")
        sizePolicy1.setHeightForWidth(self.fCad_Left_14.sizePolicy().hasHeightForWidth())
        self.fCad_Left_14.setSizePolicy(sizePolicy1)
        self.fCad_Left_14.setMinimumSize(QSize(40, 0))
        self.fCad_Left_14.setMaximumSize(QSize(0, 50))
        self.fCad_Left_14.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.fCad_Left_14)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_2 = QPushButton(self.fCad_Left_14)
        self.btCad_Left_DESL_2.setObjectName(u"btCad_Left_DESL_2")
        sizePolicy2.setHeightForWidth(self.btCad_Left_DESL_2.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_2.setSizePolicy(sizePolicy2)
        self.btCad_Left_DESL_2.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_2.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Patient_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Patient_2.png);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_77.addWidget(self.btCad_Left_DESL_2)


        self.horizontalLayout_48.addWidget(self.fCad_Left_14)


        self.verticalLayout_56.addWidget(self.fCad_Left_2)

        self.fCad_Left_3 = QFrame(self.fCadastro_Left_Opened_2)
        self.fCad_Left_3.setObjectName(u"fCad_Left_3")
        sizePolicy1.setHeightForWidth(self.fCad_Left_3.sizePolicy().hasHeightForWidth())
        self.fCad_Left_3.setSizePolicy(sizePolicy1)
        self.fCad_Left_3.setMinimumSize(QSize(0, 0))
        self.fCad_Left_3.setMaximumSize(QSize(50, 50))
        self.fCad_Left_3.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.fCad_Left_3)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_23 = QFrame(self.fCad_Left_3)
        self.fCad_Left_23.setObjectName(u"fCad_Left_23")
        sizePolicy1.setHeightForWidth(self.fCad_Left_23.sizePolicy().hasHeightForWidth())
        self.fCad_Left_23.setSizePolicy(sizePolicy1)
        self.fCad_Left_23.setMinimumSize(QSize(0, 0))
        self.fCad_Left_23.setMaximumSize(QSize(0, 50))
        self.fCad_Left_23.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.fCad_Left_23)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_3 = QPushButton(self.fCad_Left_23)
        self.btCad_Left_LIG_3.setObjectName(u"btCad_Left_LIG_3")
        sizePolicy2.setHeightForWidth(self.btCad_Left_LIG_3.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_3.setSizePolicy(sizePolicy2)
        self.btCad_Left_LIG_3.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_3.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_3.setStyleSheet(u"\n"
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

        self.horizontalLayout_78.addWidget(self.btCad_Left_LIG_3)


        self.horizontalLayout_58.addWidget(self.fCad_Left_23)

        self.fCad_Left_24 = QFrame(self.fCad_Left_3)
        self.fCad_Left_24.setObjectName(u"fCad_Left_24")
        sizePolicy1.setHeightForWidth(self.fCad_Left_24.sizePolicy().hasHeightForWidth())
        self.fCad_Left_24.setSizePolicy(sizePolicy1)
        self.fCad_Left_24.setMinimumSize(QSize(40, 0))
        self.fCad_Left_24.setMaximumSize(QSize(0, 50))
        self.fCad_Left_24.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.fCad_Left_24)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_3 = QPushButton(self.fCad_Left_24)
        self.btCad_Left_DESL_3.setObjectName(u"btCad_Left_DESL_3")
        sizePolicy2.setHeightForWidth(self.btCad_Left_DESL_3.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_3.setSizePolicy(sizePolicy2)
        self.btCad_Left_DESL_3.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_3.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_3.setStyleSheet(u"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Statistics_1.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Statistics_2.png);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_79.addWidget(self.btCad_Left_DESL_3)


        self.horizontalLayout_58.addWidget(self.fCad_Left_24)


        self.verticalLayout_56.addWidget(self.fCad_Left_3)

        self.fCad_Left_4 = QFrame(self.fCadastro_Left_Opened_2)
        self.fCad_Left_4.setObjectName(u"fCad_Left_4")
        sizePolicy1.setHeightForWidth(self.fCad_Left_4.sizePolicy().hasHeightForWidth())
        self.fCad_Left_4.setSizePolicy(sizePolicy1)
        self.fCad_Left_4.setMinimumSize(QSize(0, 0))
        self.fCad_Left_4.setMaximumSize(QSize(50, 50))
        self.fCad_Left_4.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.fCad_Left_4)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_33 = QFrame(self.fCad_Left_4)
        self.fCad_Left_33.setObjectName(u"fCad_Left_33")
        sizePolicy1.setHeightForWidth(self.fCad_Left_33.sizePolicy().hasHeightForWidth())
        self.fCad_Left_33.setSizePolicy(sizePolicy1)
        self.fCad_Left_33.setMinimumSize(QSize(0, 0))
        self.fCad_Left_33.setMaximumSize(QSize(0, 50))
        self.fCad_Left_33.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.fCad_Left_33)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_4 = QPushButton(self.fCad_Left_33)
        self.btCad_Left_LIG_4.setObjectName(u"btCad_Left_LIG_4")
        sizePolicy2.setHeightForWidth(self.btCad_Left_LIG_4.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_4.setSizePolicy(sizePolicy2)
        self.btCad_Left_LIG_4.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_4.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_4.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_historyHealt3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icons_historyHealt_2.png);\n"
"}")

        self.horizontalLayout_66.addWidget(self.btCad_Left_LIG_4)


        self.horizontalLayout_60.addWidget(self.fCad_Left_33)

        self.fCad_Left_34 = QFrame(self.fCad_Left_4)
        self.fCad_Left_34.setObjectName(u"fCad_Left_34")
        sizePolicy1.setHeightForWidth(self.fCad_Left_34.sizePolicy().hasHeightForWidth())
        self.fCad_Left_34.setSizePolicy(sizePolicy1)
        self.fCad_Left_34.setMinimumSize(QSize(40, 0))
        self.fCad_Left_34.setMaximumSize(QSize(0, 50))
        self.fCad_Left_34.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.fCad_Left_34)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_4 = QPushButton(self.fCad_Left_34)
        self.btCad_Left_DESL_4.setObjectName(u"btCad_Left_DESL_4")
        sizePolicy2.setHeightForWidth(self.btCad_Left_DESL_4.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_4.setSizePolicy(sizePolicy2)
        self.btCad_Left_DESL_4.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_4.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_4.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Bills_1.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Bills_2.png);\n"
"}")

        self.horizontalLayout_49.addWidget(self.btCad_Left_DESL_4)


        self.horizontalLayout_60.addWidget(self.fCad_Left_34)


        self.verticalLayout_56.addWidget(self.fCad_Left_4)

        self.fCad_Left_7 = QFrame(self.fCadastro_Left_Opened_2)
        self.fCad_Left_7.setObjectName(u"fCad_Left_7")
        sizePolicy1.setHeightForWidth(self.fCad_Left_7.sizePolicy().hasHeightForWidth())
        self.fCad_Left_7.setSizePolicy(sizePolicy1)
        self.fCad_Left_7.setMinimumSize(QSize(0, 0))
        self.fCad_Left_7.setMaximumSize(QSize(50, 50))
        self.fCad_Left_7.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.fCad_Left_7)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.fCad_Left_53 = QFrame(self.fCad_Left_7)
        self.fCad_Left_53.setObjectName(u"fCad_Left_53")
        sizePolicy1.setHeightForWidth(self.fCad_Left_53.sizePolicy().hasHeightForWidth())
        self.fCad_Left_53.setSizePolicy(sizePolicy1)
        self.fCad_Left_53.setMinimumSize(QSize(0, 0))
        self.fCad_Left_53.setMaximumSize(QSize(0, 50))
        self.fCad_Left_53.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.fCad_Left_53)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_LIG_6 = QPushButton(self.fCad_Left_53)
        self.btCad_Left_LIG_6.setObjectName(u"btCad_Left_LIG_6")
        sizePolicy2.setHeightForWidth(self.btCad_Left_LIG_6.sizePolicy().hasHeightForWidth())
        self.btCad_Left_LIG_6.setSizePolicy(sizePolicy2)
        self.btCad_Left_LIG_6.setMinimumSize(QSize(40, 0))
        self.btCad_Left_LIG_6.setMaximumSize(QSize(0, 50))
        self.btCad_Left_LIG_6.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Find_3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icon_Find_2.png);\n"
"}")

        self.horizontalLayout_82.addWidget(self.btCad_Left_LIG_6)


        self.horizontalLayout_81.addWidget(self.fCad_Left_53)

        self.fCad_Left_54 = QFrame(self.fCad_Left_7)
        self.fCad_Left_54.setObjectName(u"fCad_Left_54")
        sizePolicy1.setHeightForWidth(self.fCad_Left_54.sizePolicy().hasHeightForWidth())
        self.fCad_Left_54.setSizePolicy(sizePolicy1)
        self.fCad_Left_54.setMinimumSize(QSize(40, 0))
        self.fCad_Left_54.setMaximumSize(QSize(0, 50))
        self.fCad_Left_54.setFrameShape(QFrame.StyledPanel)
        self.fCad_Left_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.fCad_Left_54)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.btCad_Left_DESL_6 = QPushButton(self.fCad_Left_54)
        self.btCad_Left_DESL_6.setObjectName(u"btCad_Left_DESL_6")
        sizePolicy2.setHeightForWidth(self.btCad_Left_DESL_6.sizePolicy().hasHeightForWidth())
        self.btCad_Left_DESL_6.setSizePolicy(sizePolicy2)
        self.btCad_Left_DESL_6.setMinimumSize(QSize(40, 0))
        self.btCad_Left_DESL_6.setMaximumSize(QSize(0, 50))
        self.btCad_Left_DESL_6.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Find_1.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_Find_2.png);\n"
"}")

        self.horizontalLayout_83.addWidget(self.btCad_Left_DESL_6)


        self.horizontalLayout_81.addWidget(self.fCad_Left_54)


        self.verticalLayout_56.addWidget(self.fCad_Left_7)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_12)


        self.horizontalLayout_3.addWidget(self.fCadastro_Left_Opened_2)

        self.frameAgenda_Left_4 = QFrame(self.frameAgenda_BTs_1)
        self.frameAgenda_Left_4.setObjectName(u"frameAgenda_Left_4")
        sizePolicy.setHeightForWidth(self.frameAgenda_Left_4.sizePolicy().hasHeightForWidth())
        self.frameAgenda_Left_4.setSizePolicy(sizePolicy)
        self.frameAgenda_Left_4.setMinimumSize(QSize(60, 0))
        self.frameAgenda_Left_4.setMaximumSize(QSize(0, 16777215))
        self.frameAgenda_Left_4.setStyleSheet(u"border-radius:20px;\n"
"")
        self.frameAgenda_Left_4.setFrameShape(QFrame.StyledPanel)
        self.frameAgenda_Left_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frameAgenda_Left_4)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.BT_Agenda_Left_3 = QPushButton(self.frameAgenda_Left_4)
        self.BT_Agenda_Left_3.setObjectName(u"BT_Agenda_Left_3")
        self.BT_Agenda_Left_3.setMinimumSize(QSize(40, 50))
        self.BT_Agenda_Left_3.setMaximumSize(QSize(0, 95))
        self.BT_Agenda_Left_3.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_RIGHT.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-image: url(:/Bts/Icons/BT_s/Icon_RIGHT_2.png);\n"
"}")

        self.verticalLayout_54.addWidget(self.BT_Agenda_Left_3)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_54.addItem(self.verticalSpacer_20)


        self.horizontalLayout_3.addWidget(self.frameAgenda_Left_4)

        self.frameAgenda_Left_5 = QFrame(self.frameAgenda_BTs_1)
        self.frameAgenda_Left_5.setObjectName(u"frameAgenda_Left_5")
        sizePolicy.setHeightForWidth(self.frameAgenda_Left_5.sizePolicy().hasHeightForWidth())
        self.frameAgenda_Left_5.setSizePolicy(sizePolicy)
        self.frameAgenda_Left_5.setMinimumSize(QSize(0, 0))
        self.frameAgenda_Left_5.setMaximumSize(QSize(0, 16777215))
        self.frameAgenda_Left_5.setStyleSheet(u"border-radius:20px;\n"
"")
        self.frameAgenda_Left_5.setFrameShape(QFrame.StyledPanel)
        self.frameAgenda_Left_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frameAgenda_Left_5)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.BT_Agenda_Left_4 = QPushButton(self.frameAgenda_Left_5)
        self.BT_Agenda_Left_4.setObjectName(u"BT_Agenda_Left_4")
        self.BT_Agenda_Left_4.setMinimumSize(QSize(40, 50))
        self.BT_Agenda_Left_4.setMaximumSize(QSize(0, 95))
        self.BT_Agenda_Left_4.setStyleSheet(u"\n"
"QPushButton{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_LEFT_2.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Bts/Icons/BT_s/Icon_LEFT_1.png);\n"
"}")

        self.verticalLayout_67.addWidget(self.BT_Agenda_Left_4)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_67.addItem(self.verticalSpacer_21)


        self.horizontalLayout_3.addWidget(self.frameAgenda_Left_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_2.addWidget(self.frameAgenda_BTs_1)


        self.horizontalLayout_6.addWidget(self.widget_8)

        self.widget = QWidget(Form_Pacientes)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 10, 0, 0)
        self.widget_10 = QWidget(self.widget)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(725, 0))
        self.widget_10.setMaximumSize(QSize(625, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.widget_10)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 9, 0, 0)
        self.LBL_ListaPacientes = QLabel(self.widget_10)
        self.LBL_ListaPacientes.setObjectName(u"LBL_ListaPacientes")
        self.LBL_ListaPacientes.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/Imagem3.jpg);\n"
"border-radius:20px;")

        self.verticalLayout_17.addWidget(self.LBL_ListaPacientes)

        self.Tbox_Pacientes = QStackedWidget(self.widget_10)
        self.Tbox_Pacientes.setObjectName(u"Tbox_Pacientes")
        self.Tbox_Pacientes.setMinimumSize(QSize(725, 0))
        self.Tbox_Pacientes.setMaximumSize(QSize(725, 16777215))
        self.Tbox_PacientesHome = QWidget()
        self.Tbox_PacientesHome.setObjectName(u"Tbox_PacientesHome")
        self.horizontalLayout_5 = QHBoxLayout(self.Tbox_PacientesHome)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.Tbox_PacientesHome)
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

        self.horizontalLayout_5.addWidget(self.label)

        self.Tbox_Pacientes.addWidget(self.Tbox_PacientesHome)
        self.Tbox_PacientesPage1 = QWidget()
        self.Tbox_PacientesPage1.setObjectName(u"Tbox_PacientesPage1")
        self.horizontalLayout_9 = QHBoxLayout(self.Tbox_PacientesPage1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Frame_Dados_Pessoais_ = QFrame(self.Tbox_PacientesPage1)
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
        self.GENERO_2 = QWidget(self.Frame_Dados_Pessoais_)
        self.GENERO_2.setObjectName(u"GENERO_2")
        self.GENERO_2.setGeometry(QRect(5, 330, 0, 157))
        self.GENERO_2.setStyleSheet(u"border-radius:10px;")
        self.BT_sexo_Fem_2 = QCheckBox(self.GENERO_2)
        self.BT_sexo_Fem_2.setObjectName(u"BT_sexo_Fem_2")
        self.BT_sexo_Fem_2.setEnabled(True)
        self.BT_sexo_Fem_2.setGeometry(QRect(5, 35, 80, 25))
        font = QFont()
        font.setFamilies([u"Verdana"])
        self.BT_sexo_Fem_2.setFont(font)
        self.BT_sexo_Outros_2 = QCheckBox(self.GENERO_2)
        self.BT_sexo_Outros_2.setObjectName(u"BT_sexo_Outros_2")
        self.BT_sexo_Outros_2.setEnabled(True)
        self.BT_sexo_Outros_2.setGeometry(QRect(5, 95, 80, 25))
        self.BT_sexo_Outros_2.setFont(font)
        self.BT_sexo_Masc_2 = QCheckBox(self.GENERO_2)
        self.BT_sexo_Masc_2.setObjectName(u"BT_sexo_Masc_2")
        self.BT_sexo_Masc_2.setGeometry(QRect(5, 65, 80, 25))
        self.BT_sexo_Masc_2.setFont(font)
        self.label_9 = QLabel(self.GENERO_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(5, 5, 80, 25))
        self.label_9.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.BT_sexo_Ocultar_2 = QCheckBox(self.GENERO_2)
        self.BT_sexo_Ocultar_2.setObjectName(u"BT_sexo_Ocultar_2")
        self.BT_sexo_Ocultar_2.setGeometry(QRect(5, 125, 80, 25))
        self.BT_sexo_Ocultar_2.setFont(font)
        self.widget_11 = QWidget(self.Frame_Dados_Pessoais_)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(5, 5, 405, 481))
        self.widget_11.setStyleSheet(u"border-radius:10px;")
        self.label_10 = QLabel(self.widget_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(5, 5, 395, 25))
        self.label_10.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(5, 260, 395, 25))
        self.label_12.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.widget_11)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(5, 35, 125, 25))
        self.comboBox_2 = QComboBox(self.widget_11)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(5, 95, 125, 25))
        self.comboBox_3 = QComboBox(self.widget_11)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(5, 65, 125, 25))
        self.tableWidget = QTableWidget(self.widget_11)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(5, 290, 395, 181))
        self.comboBox_4 = QComboBox(self.widget_11)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(5, 125, 125, 25))
        self.frame_5 = QFrame(self.Frame_Dados_Pessoais_)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 492, 415, 40))
        self.frame_5.setMaximumSize(QSize(415, 16777215))
        self.frame_5.setStyleSheet(u"border-radius:10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.BT_Descartar_D_P_2 = QPushButton(self.frame_5)
        self.BT_Descartar_D_P_2.setObjectName(u"BT_Descartar_D_P_2")
        self.BT_Descartar_D_P_2.setMinimumSize(QSize(0, 20))
        self.BT_Descartar_D_P_2.setMaximumSize(QSize(125, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Lucida Calligraphy"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.BT_Descartar_D_P_2.setFont(font1)
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
"border:15px;\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_45.addWidget(self.BT_Descartar_D_P_2)

        self.BT_Alterar_D_P_2 = QPushButton(self.frame_5)
        self.BT_Alterar_D_P_2.setObjectName(u"BT_Alterar_D_P_2")
        self.BT_Alterar_D_P_2.setMinimumSize(QSize(0, 20))
        self.BT_Alterar_D_P_2.setMaximumSize(QSize(125, 16777215))
        self.BT_Alterar_D_P_2.setFont(font1)
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

        self.horizontalLayout_45.addWidget(self.BT_Alterar_D_P_2)

        self.BT_Salvar_D_P_2 = QPushButton(self.frame_5)
        self.BT_Salvar_D_P_2.setObjectName(u"BT_Salvar_D_P_2")
        self.BT_Salvar_D_P_2.setMinimumSize(QSize(0, 20))
        self.BT_Salvar_D_P_2.setMaximumSize(QSize(125, 16777215))
        self.BT_Salvar_D_P_2.setFont(font1)
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

        self.horizontalLayout_45.addWidget(self.BT_Salvar_D_P_2)


        self.horizontalLayout_9.addWidget(self.Frame_Dados_Pessoais_)

        self.Tbox_Pacientes.addWidget(self.Tbox_PacientesPage1)
        self.Tbox_PacientesPage2 = QWidget()
        self.Tbox_PacientesPage2.setObjectName(u"Tbox_PacientesPage2")
        self.Tbox_PacientesPage2.setMinimumSize(QSize(725, 0))
        self.Tbox_PacientesPage2.setMaximumSize(QSize(725, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.Tbox_PacientesPage2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Frame_Dados_Pessoais_1 = QFrame(self.Tbox_PacientesPage2)
        self.Frame_Dados_Pessoais_1.setObjectName(u"Frame_Dados_Pessoais_1")
        sizePolicy3.setHeightForWidth(self.Frame_Dados_Pessoais_1.sizePolicy().hasHeightForWidth())
        self.Frame_Dados_Pessoais_1.setSizePolicy(sizePolicy3)
        self.Frame_Dados_Pessoais_1.setMinimumSize(QSize(715, 532))
        self.Frame_Dados_Pessoais_1.setMaximumSize(QSize(715, 532))
        self.Frame_Dados_Pessoais_1.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Verdana\";\n"
"placeHolder-text-align: Center;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QFrame{\n"
"border-radius:10px;\n"
"background-image: url(:/Backgrounds/Icons/Backgrounds/Sorriso.jpg);\n"
"}")
        self.Frame_Dados_Pessoais_1.setFrameShape(QFrame.StyledPanel)
        self.Frame_Dados_Pessoais_1.setFrameShadow(QFrame.Raised)
        self.GENERO = QWidget(self.Frame_Dados_Pessoais_1)
        self.GENERO.setObjectName(u"GENERO")
        self.GENERO.setGeometry(QRect(5, 330, 0, 157))
        self.GENERO.setStyleSheet(u"border-radius:10px;")
        self.BT_sexo_Fem = QCheckBox(self.GENERO)
        self.BT_sexo_Fem.setObjectName(u"BT_sexo_Fem")
        self.BT_sexo_Fem.setEnabled(True)
        self.BT_sexo_Fem.setGeometry(QRect(5, 35, 80, 25))
        self.BT_sexo_Fem.setFont(font)
        self.BT_sexo_Outros = QCheckBox(self.GENERO)
        self.BT_sexo_Outros.setObjectName(u"BT_sexo_Outros")
        self.BT_sexo_Outros.setEnabled(True)
        self.BT_sexo_Outros.setGeometry(QRect(5, 95, 80, 25))
        self.BT_sexo_Outros.setFont(font)
        self.BT_sexo_Masc = QCheckBox(self.GENERO)
        self.BT_sexo_Masc.setObjectName(u"BT_sexo_Masc")
        self.BT_sexo_Masc.setGeometry(QRect(5, 65, 80, 25))
        self.BT_sexo_Masc.setFont(font)
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
        self.BT_sexo_Ocultar.setFont(font)
        self.widget_9 = QWidget(self.Frame_Dados_Pessoais_1)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(5, 5, 705, 482))
        self.widget_9.setMinimumSize(QSize(705, 0))
        self.widget_9.setMaximumSize(QSize(705, 16777215))
        self.widget_9.setStyleSheet(u"border-radius:10px;")
        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(5, 5, 695, 25))
        self.label_6.setMinimumSize(QSize(695, 0))
        self.label_6.setMaximumSize(QSize(695, 16777215))
        self.label_6.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Calligraphy\";\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_38 = QLabel(self.widget_9)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(260, 30, 201, 441))
        self.label_38.setMaximumSize(QSize(300, 16777215))
        self.label_38.setStyleSheet(u"border-radius:10px;")
        self.verticalLayoutWidget_3 = QWidget(self.widget_9)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 30, 252, 445))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.verticalLayoutWidget_3)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 200))
        self.widget_14.setMaximumSize(QSize(250, 200))
        self.verticalLayout_4 = QVBoxLayout(self.widget_14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.widget_26 = QWidget(self.widget_14)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.widget_26)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(175, 25))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Verdana\";\n"
"")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_40)


        self.verticalLayout_4.addWidget(self.widget_26)

        self.widget_22 = QWidget(self.widget_14)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(0, 40))
        self.widget_22.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMaximumSize(QSize(30, 30))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget_23)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(30, 30))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Plus.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Plus_2.png);\n"
"}")

        self.horizontalLayout_20.addWidget(self.pushButton_4)


        self.horizontalLayout_19.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMaximumSize(QSize(225, 16777215))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.CB_Numero_4 = QComboBox(self.widget_24)
        self.CB_Numero_4.addItem("")
        self.CB_Numero_4.setObjectName(u"CB_Numero_4")
        self.CB_Numero_4.setMinimumSize(QSize(0, 0))
        self.CB_Numero_4.setMaximumSize(QSize(50, 16777215))
        self.CB_Numero_4.setMaxVisibleItems(16)

        self.horizontalLayout_21.addWidget(self.CB_Numero_4)

        self.CB_Prodedimento_4 = QComboBox(self.widget_24)
        self.CB_Prodedimento_4.addItem("")
        self.CB_Prodedimento_4.setObjectName(u"CB_Prodedimento_4")
        self.CB_Prodedimento_4.setMinimumSize(QSize(100, 25))
        self.CB_Prodedimento_4.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_21.addWidget(self.CB_Prodedimento_4)


        self.horizontalLayout_19.addWidget(self.widget_24)

        self.widget_32 = QWidget(self.widget_22)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMaximumSize(QSize(65, 30))
        self.horizontalLayout_32 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_32.setSpacing(5)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.widget_32)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 0))
        self.pushButton_9.setMaximumSize(QSize(30, 30))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Title/Icons/BT_s/Icon_CheckNegative_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_CheckNegative_2.png);\n"
"}")

        self.horizontalLayout_32.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_32)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 0))
        self.pushButton_10.setMaximumSize(QSize(30, 30))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Title/Icons/BT_s/Icon_CheckPositive_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_CheckPositive_2.png);\n"
"}")

        self.horizontalLayout_32.addWidget(self.pushButton_10)


        self.horizontalLayout_19.addWidget(self.widget_32)


        self.verticalLayout_4.addWidget(self.widget_22)

        self.widget_25 = QWidget(self.widget_14)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_5 = QLineEdit(self.widget_25)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.lineEdit_5.setFont(font3)
        self.lineEdit_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_22.addWidget(self.lineEdit_5)


        self.verticalLayout_4.addWidget(self.widget_25)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.verticalLayout_5.addWidget(self.widget_14)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.widget_21 = QWidget(self.verticalLayoutWidget_3)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(0, 200))
        self.widget_21.setMaximumSize(QSize(250, 200))
        self.verticalLayout_8 = QVBoxLayout(self.widget_21)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 5, 0, 5)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.widget_27 = QWidget(self.widget_21)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.widget_27)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(175, 25))
        self.label_41.setFont(font2)
        self.label_41.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Verdana\";\n"
"")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_41)


        self.verticalLayout_8.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_21)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 40))
        self.widget_28.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(30, 30))
        self.horizontalLayout_26 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.widget_29)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(30, 30))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Plus.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_Plus_2.png);\n"
"}")

        self.horizontalLayout_26.addWidget(self.pushButton_5)


        self.horizontalLayout_25.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_28)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMaximumSize(QSize(225, 16777215))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.CB_Numero_5 = QComboBox(self.widget_30)
        self.CB_Numero_5.addItem("")
        self.CB_Numero_5.setObjectName(u"CB_Numero_5")
        self.CB_Numero_5.setMinimumSize(QSize(0, 0))
        self.CB_Numero_5.setMaximumSize(QSize(50, 16777215))
        self.CB_Numero_5.setMaxVisibleItems(16)

        self.horizontalLayout_27.addWidget(self.CB_Numero_5)

        self.CB_Prodedimento_5 = QComboBox(self.widget_30)
        self.CB_Prodedimento_5.addItem("")
        self.CB_Prodedimento_5.setObjectName(u"CB_Prodedimento_5")
        self.CB_Prodedimento_5.setMinimumSize(QSize(100, 25))
        self.CB_Prodedimento_5.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_27.addWidget(self.CB_Prodedimento_5)


        self.horizontalLayout_25.addWidget(self.widget_30)

        self.widget_33 = QWidget(self.widget_28)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMaximumSize(QSize(65, 30))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_33.setSpacing(5)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = QPushButton(self.widget_33)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 0))
        self.pushButton_19.setMaximumSize(QSize(30, 30))
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Title/Icons/BT_s/Icon_CheckNegative_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_CheckNegative_2.png);\n"
"}")

        self.horizontalLayout_33.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.widget_33)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 0))
        self.pushButton_20.setMaximumSize(QSize(30, 30))
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Title/Icons/BT_s/Icon_CheckPositive_1.png);\n"
"border:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:15px;\n"
"background-image: url(:/Title/Icons/BT_s/Icon_CheckPositive_2.png);\n"
"}")

        self.horizontalLayout_33.addWidget(self.pushButton_20)


        self.horizontalLayout_25.addWidget(self.widget_33)


        self.verticalLayout_8.addWidget(self.widget_28)

        self.widget_31 = QWidget(self.widget_21)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.widget_31)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 25))
        self.lineEdit_6.setFont(font3)
        self.lineEdit_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_28.addWidget(self.lineEdit_6)


        self.verticalLayout_8.addWidget(self.widget_31)


        self.verticalLayout_5.addWidget(self.widget_21)

        self.tableWidget_2 = QTableWidget(self.widget_9)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(9)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        icon = QIcon()
        iconThemeName = u"accessories-calculator"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"C:/Users/PC_VELHO/.designer/_Telas_UI", QSize(), QIcon.Normal, QIcon.Off)

        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        __qtablewidgetitem6.setIcon(icon);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(460, 30, 241, 439))
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy4)
        self.tableWidget_2.setStyleSheet(u"background-image: url(:/Backgrounds/Icons/Backgrounds/GreySorriso.jpg);")
        self.tableView = QTableView(self.widget_9)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(500, 150, 18, 30))
        self.frame_4 = QFrame(self.Frame_Dados_Pessoais_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(5, 492, 705, 40))
        self.frame_4.setMinimumSize(QSize(705, 0))
        self.frame_4.setMaximumSize(QSize(705, 16777215))
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
        self.BT_Descartar_D_P.setFont(font1)
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
        self.BT_Alterar_D_P.setFont(font1)
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
        self.BT_Salvar_D_P.setFont(font1)
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


        self.horizontalLayout_4.addWidget(self.Frame_Dados_Pessoais_1)

        self.Tbox_Pacientes.addWidget(self.Tbox_PacientesPage2)

        self.verticalLayout_17.addWidget(self.Tbox_Pacientes)


        self.horizontalLayout.addWidget(self.widget_10)


        self.horizontalLayout_6.addWidget(self.widget)


        self.retranslateUi(Form_Pacientes)

        self.Tbox_Pacientes.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form_Pacientes)
    # setupUi

    def retranslateUi(self, Form_Pacientes):
        Form_Pacientes.setWindowTitle(QCoreApplication.translate("Form_Pacientes", u"Form", None))
        self.btCad_Left_LIG_2.setText("")
        self.btCad_Left_DESL_2.setText("")
        self.btCad_Left_LIG_3.setText("")
        self.btCad_Left_DESL_3.setText("")
        self.btCad_Left_LIG_4.setText("")
        self.btCad_Left_DESL_4.setText("")
        self.btCad_Left_LIG_6.setText("")
        self.btCad_Left_DESL_6.setText("")
        self.BT_Agenda_Left_3.setText("")
        self.BT_Agenda_Left_4.setText("")
        self.LBL_ListaPacientes.setText(QCoreApplication.translate("Form_Pacientes", u"<html><head/><body><p align=\"center\"><img src=\":/Title/Icons/Titles/LBL_ListaDePaciente.png\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form_Pacientes", u"<html><head/><body><p align=\"center\"><img src=\":/Backgrounds/Icons/Logos/Icon_Menu2.png\"/></p></body></html>", None))
        self.BT_sexo_Fem_2.setText(QCoreApplication.translate("Form_Pacientes", u"Feminino", None))
        self.BT_sexo_Outros_2.setText(QCoreApplication.translate("Form_Pacientes", u"Outros", None))
        self.BT_sexo_Masc_2.setText(QCoreApplication.translate("Form_Pacientes", u"Masculino", None))
        self.label_9.setText(QCoreApplication.translate("Form_Pacientes", u"G\u00eanero ", None))
        self.BT_sexo_Ocultar_2.setText(QCoreApplication.translate("Form_Pacientes", u"N/A", None))
        self.label_10.setText(QCoreApplication.translate("Form_Pacientes", u"Dados Pessoais", None))
        self.label_12.setText(QCoreApplication.translate("Form_Pacientes", u"Hist\u00f3rico", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Form_Pacientes", u"Nome", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("Form_Pacientes", u"Pr\u00f3xima Consulta", None))
        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("Form_Pacientes", u"Ultima Consulta", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_Pacientes", u"Agendamentos", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_Pacientes", u"Procedimentos", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_Pacientes", u"Data", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_Pacientes", u"Pagamentos", None));
        self.comboBox_4.setPlaceholderText(QCoreApplication.translate("Form_Pacientes", u"Procedimentos", None))
        self.BT_Descartar_D_P_2.setText(QCoreApplication.translate("Form_Pacientes", u"Descartar", None))
        self.BT_Alterar_D_P_2.setText(QCoreApplication.translate("Form_Pacientes", u"Alterar", None))
        self.BT_Salvar_D_P_2.setText(QCoreApplication.translate("Form_Pacientes", u"Salvar", None))
        self.BT_sexo_Fem.setText(QCoreApplication.translate("Form_Pacientes", u"Feminino", None))
        self.BT_sexo_Outros.setText(QCoreApplication.translate("Form_Pacientes", u"Outros", None))
        self.BT_sexo_Masc.setText(QCoreApplication.translate("Form_Pacientes", u"Masculino", None))
        self.label_5.setText(QCoreApplication.translate("Form_Pacientes", u"G\u00eanero ", None))
        self.BT_sexo_Ocultar.setText(QCoreApplication.translate("Form_Pacientes", u"N/A", None))
        self.label_6.setText(QCoreApplication.translate("Form_Pacientes", u"Dados Cl\u00ednicos", None))
        self.label_38.setText(QCoreApplication.translate("Form_Pacientes", u"<html><head/><body><p align=\"center\"><img src=\":/Logos/Icons/Logos/Prontuario.png\"/></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("Form_Pacientes", u"Superior", None))
        self.pushButton_4.setText("")
        self.CB_Numero_4.setItemText(0, QCoreApplication.translate("Form_Pacientes", u"N\u00ba", None))

        self.CB_Prodedimento_4.setItemText(0, QCoreApplication.translate("Form_Pacientes", u"Procedimento", None))

        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form_Pacientes", u"Observa\u00e7\u00f5es : ...", None))
        self.label_41.setText(QCoreApplication.translate("Form_Pacientes", u"Inferior", None))
        self.pushButton_5.setText("")
        self.CB_Numero_5.setItemText(0, QCoreApplication.translate("Form_Pacientes", u"N\u00ba", None))

        self.CB_Prodedimento_5.setItemText(0, QCoreApplication.translate("Form_Pacientes", u"Procedimento", None))

        self.pushButton_19.setText("")
        self.pushButton_20.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form_Pacientes", u"Observa\u00e7\u00f5es : ...", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_Pacientes", u"N\u00ba", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_Pacientes", u"Procedimentos", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_Pacientes", u"Obs : ...", None));
        self.BT_Descartar_D_P.setText(QCoreApplication.translate("Form_Pacientes", u"Descartar", None))
        self.BT_Alterar_D_P.setText(QCoreApplication.translate("Form_Pacientes", u"Alterar", None))
        self.BT_Salvar_D_P.setText(QCoreApplication.translate("Form_Pacientes", u"Salvar", None))
    # retranslateUi

