from PySide6 import QtCore
    
#==============================================================================================
# Ativando Animações dos frames dos menus internos 
#==============================================================================================
def Animation_sidebar_Left (self, 

   #==============================================================
       
    # Qframe1,   # 40/00     # self.BT_Cad_Left_LIGAR, 
     Qframe2,   # 60/00     # self.fCadastro_Left_On,
   
   #==============================================================
     
    # Qframe3,   # 00/40     # self.BT_Cad_Left_DESLIGAR,
     Qframe4,   # 00/60     # self.fCad_Left_Off,
   
   #==============================================================
    
     Qframe5,   # 00/60     # self.fCadastro_Left_Opened,
    
   #============================================================== 
   
    # Qframe6,   # 50/00     # self.fCad_Left_01,
    # Qframe7,   # 40/00     # self.btCad_Left_DESL_01,
    # Qframe8,   # 40/00     # self.btCad_Left_LIG_01,
    
   #==============================================================
   
    # Qframe9,   # 50/00     # self.fCad_Left_02,
    # Qframe10,  # 40/00     # self.btCad_Left_DESL_02,
    # Qframe11,  # 40/00     # self.btCad_Left_LIG_02,
   
   #==============================================================
    
    # Qframe12,  # 40/00     # self.fCad_Left_03,
    # Qframe13,  # 40/00     # self.btCad_Left_DESL_03,
    # Qframe14,  # 40/00     # self.btCad_Left_LIG_03,
   
   #==============================================================
    
    # Qframe15,  # 50/00     # self.fCad_Left_04,
    # Qframe16,  # 40/00     # self.btCad_Left_DESL_04,
    # Qframe17,  # 40/00     # self.btCad_Left_LIG_04,

   #==============================================================
        
    ):

    #=================================================
    #Variáveis
    #=================================================
    #largura1  =     Qframe1.width   ()
    largura2  =     Qframe2.width   ()
    #================================
    #largura3  =     Qframe3.width   ()
    largura4  =     Qframe4.width   ()
    #================================
    largura5  =     Qframe5.width   ()
    #================================
    #largura6  =     Qframe6.width   ()
    #largura7  =     Qframe7.width   ()
    # largura8  =    Qframe8.width   ()
    #================================
    # largura9  =    Qframe9.width   ()   
    # largura10 =    Qframe10.width  () 
    # largura11 =    Qframe11.width  ()
    #================================
    # largura12 =    Qframe12.width  ()
    # largura13 =    Qframe13.width  ()
    # largura14 =    Qframe14.width  ()
    #================================
    # largura15 =    Qframe15.width  ()
    # largura16 =    Qframe16.width  ()
    # largura17 =    Qframe17.width  ()
   
    #===================================================================================
    # self.BT_Cad_Left_LIGAR,               # Close         # 40/00
    #===================================================================================       
    
#    if largura1 == 40:
#        novaLargura1 = 0

#    else: novaLargura1 = 40

#    self.animation = QtCore.QPropertyAnimation  (Qframe1, b"minimumWidth")
#    self.animation.setDuration                  (1000) 
#    self.animation.setStartValue                (novaLargura1)
#    self.animation.setEndValue                  (largura1)
#    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
#    self.animation.start                        ()

    #===================================================================================
    # self.fCadastro_Left_On,               # Close         # 60/00
    #===================================================================================
    
    if largura2 == 60:
        novaLargura2 = 0

    else: 
        novaLargura2 = 60

    self.animation = QtCore.QPropertyAnimation  (Qframe2, b"minimumWidth")
    self.animation.setDuration                  (500) 
    self.animation.setStartValue                (novaLargura2)
    self.animation.setEndValue                  (largura2)
    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
    self.animation.start                        ()

    #===================================================================================
    # self.BT_Cad_Left_DESLIGAR,            # Open          # 00/40
    #===================================================================================
    
#    if largura3 == 0:
#        novaLargura3 = 40

#    else:
#        novaLargura3 = 0

#    self.animation = QtCore.QPropertyAnimation  (Qframe3, b"minimumWidth")
#    self.animation.setDuration                  (1000) 
#    self.animation.setStartValue                (novaLargura3) 
#    self.animation.setEndValue                  (largura3)
#    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
#    self.animation.start                        ()

    #===================================================================================
    # self.fCadastro_Left_Opened,           # Open          # 00/60
    #===================================================================================

    if largura4 == 0:
        novaLargura4 = 60

    else:
        novaLargura4 = 0

    self.animation = QtCore.QPropertyAnimation  (Qframe4, b"minimumWidth")
    self.animation.setDuration                  (500) 
    self.animation.setStartValue                (novaLargura4)
    self.animation.setEndValue                  (largura4) 
    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
    self.animation.start                        ()

    #===================================================================================
    # self.fCadastro_Left_Opened,            # Open          # 00/60 
    #===================================================================================
    
    if largura5 == 0:
        novaLargura5 = 60

    else:
        novaLargura5 = 0

    self.animation = QtCore.QPropertyAnimation  (Qframe5, b"minimumWidth")
    self.animation.setDuration                  (500) 
    self.animation.setStartValue                (largura5) 
    self.animation.setEndValue                  (novaLargura5)
    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
    self.animation.start                        ()
    
    #===================================================================================
    # self.fCad_Left_01,                    # Open          # 50/00
    #===================================================================================
    
#    if largura6 == 0:
#        novaLargura6 = 50

#    else:
#        novaLargura6 = 0

#    self.animation = QtCore.QPropertyAnimation (Qframe6, b"minimumWidth")
#    self.animation.setDuration                 (500) 
#   self.animation.setStartValue                (largura6)
#    self.animation.setEndValue                 (novaLargura6) 
#    self.animation.setEasingCurve              (QtCore.QEasingCurve.InOutQuart)
#    self.animation.start                       ()


    #===================================================================================
     # self.btCad_Left_DESL_01,              # Open          # 40/00
    #===================================================================================
    
#    if largura7 == 0:
#        novaLargura7 = 40

#    else:
#        novaLargura7 = 0

#    self.animation = QtCore.QPropertyAnimation (Qframe7, b"minimumWidth")
#    self.animation.setDuration                 (500) 
#    self.animation.setStartValue               (largura7)
#    self.animation.setEndValue                 (novaLargura7) 
#    self.animation.setEasingCurve              (QtCore.QEasingCurve.InOutQuart)
#    self.animation.start                       ()

    #===================================================================================
    # self.btCad_Left_LIG_01,               # Open          # 40/00
    #===================================================================================
    
    #if largura8 == 40:
    #    novaLargura8 = 0

    #else:
    #    novaLargura8 = 40

    #self.animation = QtCore.QPropertyAnimation(Qframe8, b"minimumWidth")
    #self.animation.setDuration(500) 
    #self.animation.setStartValue(largura8)
    #self.animation.setEndValue(novaLargura8) 
    #self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    #self.animation.start()

    #===================================================================================
    # self.fCad_Left_02,                    # Open          # 50/00
    #===================================================================================
    
#    if largura9 == 0:
#        novaLargura9 = 50

#    else:
#        novaLargura9 = 0

#    self.animation = QtCore.QPropertyAnimation  (Qframe9, b"minimumWidth")
#    self.animation.setDuration                  (250) 
#    self.animation.setStartValue                (largura9)
#    self.animation.setEndValue                  (novaLargura9) 
#    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
#    self.animation.start                        ()
   
    #===================================================================================
    # self.btCad_Left_DESL_02,              # Open          # 40/00
    #===================================================================================
    
#    if largura10 == 0:
#        novaLargura10 = 40

#    else:
#        novaLargura10 = 0

#    self.animation = QtCore.QPropertyAnimation  (Qframe10, b"minimumWidth")
#    self.animation.setDuration                  (250) 
#    self.animation.setStartValue                (largura10)
#    self.animation.setEndValue                  (novaLargura10) 
#    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
#    self.animation.start                        ()
   
    #===================================================================================
    # self.btCad_Left_LIG_02,               # Open          # 40/00
    #===================================================================================
    
   # if largura11 == 40:
   #     novaLargura11 = 0

   # else:
   #     novaLargura11 = 40

   # self.animation = QtCore.QPropertyAnimation (Qframe11, b"minimumWidth")
   # self.animation.setDuration                 (250) 
   # self.animation.setStartValue               (largura11)
   # self.animation.setEndValue                 (novaLargura11) 
   # self.animation.setEasingCurve              (QtCore.QEasingCurve.InOutQuart)
   # self.animation.start                       () 
   
    #===================================================================================
    # self.fCad_Left_03,                    # Open          # 50/00
    #===================================================================================
    
#    if largura12 == 0:
#        novaLargura12 = 50

#    else:
#        novaLargura12 = 0

#    self.animation = QtCore.QPropertyAnimation  (Qframe12, b"minimumWidth")
#    self.animation.setDuration                  (250) 
#    self.animation.setStartValue                (largura12)
#    self.animation.setEndValue                  (novaLargura12) 
#    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
#    self.animation.start                        () 
   
    #===================================================================================
     # self.btCad_Left_DESL_03,              # Open          # 40/00
    #===================================================================================
    
#    if largura13 == 0:
#        novaLargura13 = 40

#    else:
#        novaLargura13 = 0

#    self.animation = QtCore.QPropertyAnimation  (Qframe13, b"minimumWidth")
#    self.animation.setDuration                  (250) 
#    self.animation.setStartValue                (largura13)
#    self.animation.setEndValue                  (novaLargura13) 
#    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
#    self.animation.start                        () 
   
    #===================================================================================
    # self..btCad_Left_LIG_03,              # Open          # 40/00
    #===================================================================================
    
   # if largura14 == 40:
   #     novaLargura14 = 0

   # else:
   #     novaLargura14 = 40

   # self.animation = QtCore.QPropertyAnimation (Qframe14, b"minimumWidth")
   # self.animation.setDuration                 (250) 
   # self.animation.setStartValue               (largura14)
   # self.animation.setEndValue                 (novaLargura14) 
   # self.animation.setEasingCurve              (QtCore.QEasingCurve.InOutQuart)
   # self.animation.start                       ()                  

    #===================================================================================
    # self.fCad_Left_04,                    # Open          # 50/00
    #===================================================================================
    
#    if largura15 == 50:
#        novaLargura15  = 0

#    else:
#        novaLargura15  = 50

#    self.animation = QtCore.QPropertyAnimation  (Qframe15 , b"minimumWidth")
#    self.animation.setDuration                  (250) 
#    self.animation.setStartValue                (largura15)
#    self.animation.setEndValue                  (novaLargura15) 
#    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
#    self.animation.start                        () 
   
    #===================================================================================
    # self.btCad_Left_DESL_04,              # Open          # 40/00
    #===================================================================================
    
#    if largura16  == 0:
#        novaLargura16  = 40

#    else:
#        novaLargura16  = 0

#   self.animation = QtCore.QPropertyAnimation  (Qframe16 , b"minimumWidth")
#   self.animation.setDuration                  (250) 
#   self.animation.setStartValue                (largura16)
#   self.animation.setEndValue                  (novaLargura16) 
#   self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
#   self.animation.start                        () 
   
    #===================================================================================
    # self..btCad_Left_LIG_04,              # Open          # 40/00
    #===================================================================================
    
   # if largura17 == 40:
   #     novaLargura17 = 0

   # else:
   #     novaLargura17 = 40

   # self.animation = QtCore.QPropertyAnimation (Qframe17, b"minimumWidth")
   # self.animation.setDuration                 (250) 
   # self.animation.setStartValue               (largura17)
   # self.animation.setEndValue                 (novaLargura17) 
   # self.animation.setEasingCurve              (QtCore.QEasingCurve.InOutQuart)
   # self.animation.start                       ()       