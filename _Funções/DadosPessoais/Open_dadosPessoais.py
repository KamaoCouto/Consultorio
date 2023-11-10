#from PySide6 import QtCore  
    
#==============================================================================================
# Ativando Animações dos frames dos menus internos 
#===============================================================================================
def dadosPessoais_Open (self,
                    
                        #=======================================================================

                        Qframe1,        # self.Tbox_Cadastro,
                        Qframe2,        # self.Tbox_CadastroPage2,

                        #=======================================================================

                        Qframe3,       # self.fCad_Left_12,             # Open           # 00/40
                                             
                        Qframe4,       # self.fCad_Left_11,             # Close          # 40/00
                        Qframe5,       # self.fCad_Left_21,             # Close          # 40/00
                        Qframe6,       # self.fCad_Left_31,             # Close          # 40/00
                        Qframe7,       # self.fCad_Left_41,             # Close          # 40/00  

                        #=======================================================================
                    ):
    
    #=====================================
    #Lógica para apresentação de Progresso
    #=====================================
    #self.statusProgresso   (Qframe5)
         
    #=================================================
    #Lógica para acionamento de Página
    #=================================================
    
    self.pageOpen       (Qframe1,Qframe2)

    #==================================
    #Lógica para apresentação de Botões
    #==================================
        
    #=================================================
        
    self.Cad_Buttons_ON (
         
         Qframe3,             # Open           # 00/40
        
         Qframe4,             # Close          # 40/00
         Qframe5,             # Close          # 40/00
         Qframe6,             # Close          # 40/00
         Qframe7,             # Close          # 40/00
         
    )

    #=================================================
    
    #self.Show_sideButton_ON     (Qframe4)

    #=================================================
    #Lógica para apresentação de Frame
    #=================================================
    #Close 
#    self. OFF_sideFrame_CLOSE   (Qframe5)   #60/00/60 == 60=>00
    #Open
#    self. OFF_sideFrame_OPEN    (Qframe6)   #00/60/00 == 00=>60 

