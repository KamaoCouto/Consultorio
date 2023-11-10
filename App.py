#import mysql.connector

from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication,QMainWindow,QWidget)

import sys


#==========================================================================================================
#======> Imports de Forms/Telas (ui_.py)
#==========================================================================================================

from _Screens   import Ui_Form_Login
from _Screens   import Ui_Form_novoUsuario
from _Screens   import Ui_Tela_Inicial 
from _Screens   import Ui_Form_dadosPessoais
from _Screens   import Ui_Form_Agenda
from _Screens   import Ui_Form_Pacientes

#==========================================================================================================
#======> Definição de classe Forms ( Ui_Form_Login )
#==========================================================================================================
    
class Form_Login (QWidget,      Ui_Form_Login):

#==========================================================================================================
#======> Imports de classe Forms ( [func] [Ui_Form_Login] ) 
#==========================================================================================================    

    from _Funções   ._Telas     .Tela_Login     .Func_Abrir_NovoUsuario     import Open_newUser
  
    def __init__(self):
        super                           (Form_Login, self)      .__init__()
        self.setupUi                    (self)
        self.setWindowTitle             ("Login do Sistema")
        appIcon = QIcon                 (u"")
        self.setWindowIcon              (appIcon)
    #    self.Tela_00 = Form_Login       ()
        self.Tela_01 = Form_novoUsuario ()

        
        self.BT_NewUser.clicked.connect(
            
            lambda: self.Open_newUser(
                
    #            self.Tela_00,
                self.Tela_01,
                            
            ))


                        
#==========================================================================================================
#======> Definição de classe Forms ( Ui_Form_novoUsuario )
#==========================================================================================================

class Form_novoUsuario (QWidget,    Ui_Form_novoUsuario):
  
    def __init__(self):
        super                           (Form_novoUsuario, self).__init__()
        self.setupUi                    (self)
        self.setWindowTitle             ("Novo Cadastro")
        appIcon = QIcon                 (u"")
        self.setWindowIcon              (appIcon)
    #    self.Tela_00 = Form_Login       ()

#==========================================================================================================
#======> Definição de classe Forms ( Ui_Form_dadosPessoais )
#==========================================================================================================

class Main_telaInicial (QMainWindow,    Ui_Tela_Inicial):
  
    def __init__(self):
        super                           (Main_telaInicial, self).__init__()
        self.setupUi                    (self)
        self.setWindowTitle             ("Gerenciamento de operações")
        appIcon = QIcon                 (u"")
        self.setWindowIcon              (appIcon)

#==========================================================================================================
#======> Definição de classe Forms ( Ui_Form_dadosPessoais )
#==========================================================================================================

class Form_novoPaciente (QWidget,    Ui_Form_dadosPessoais):
  
    def __init__(self):
        super                           (Form_novoPaciente, self).__init__()
        self.setupUi                    (self)
        self.setWindowTitle             ("Cadastro de Paciente")
        appIcon = QIcon                 (u"")
        self.setWindowIcon              (appIcon)

#==========================================================================================================
#======> Definição de classe Forms ( Ui_Form_dadosPessoais )
#==========================================================================================================

class Form_controleAgenda (QWidget,    Ui_Form_Agenda):
  
    def __init__(self):
        super                           (Form_controleAgenda, self).__init__()
        self.setupUi                    (self)
        self.setWindowTitle             ("Cadastro de Paciente")
        appIcon = QIcon                 (u"")
        self.setWindowIcon              (appIcon)
        
#==========================================================================================================
#======> Definição de classe Forms ( Ui_Form_dadosPessoais )
#==========================================================================================================

class Form_controleProntuarios (QWidget,    Ui_Form_Pacientes):
  
    def __init__(self):
        super                           (Form_controleProntuarios, self).__init__()
        self.setupUi                    (self)
        self.setWindowTitle             ("Prontuários de Pacientes")
        appIcon = QIcon                 (u"")
        self.setWindowIcon              (appIcon)        

#==========================================================================================================
#======>    Executando a Classe "MainWwindow"
#==========================================================================================================
if __name__ ==  "__main__":

    app = QApplication              (sys.argv)
    Tela_00 = Form_Login            () 
    Tela_00.show                    ()
    app.exec                        () 
        
            
