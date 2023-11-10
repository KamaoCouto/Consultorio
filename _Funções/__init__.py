



#==========================================================================================================
#======> Imports de classe Forms ( [func] [Ui_Form_Login] )
#==========================================================================================================
from ._Telas    .Tela_Login     .Func_Abrir_NovoUsuario     import Open_newUser

#==============================================================================
# (SHOW_PROGRESSO_STATUS) --- Criando Imports de Animações de abertura de frame
#==============================================================================
#Open_Barra_de_Progresso
from ._CadastroStatus   .statusCadastro         import  statusProgresso

#==================================================================
# (OPENPAGES) --- Criando Imports de Animações de abertura de telas
#==================================================================
#Open_PAGES
from .showPages         .openPage               import  pageOpen   

#===============================================================
# (SIDEBAR) --- Criando Imports de Animações da tela "Cadastro"
#===============================================================
#Funcionamento_BT's
from .DadosPessoais  .Open_dadosPessoais        import   dadosPessoais_Open
#Funcionamento_BT's
from .DadosPessoais  .Close__dadosPessoais       import   dadosPessoais_Close

