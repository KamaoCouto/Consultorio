from PySide6 import QtCore
    
#==============================================================================================
# Ativando Animações dos frames dos menus internos 

#00/40/00 == 00=>40
#==============================================================================================
def Show_sideButton_OFF (self, Qframe1,):#Qframe
    
    largura1 = Qframe1.width ()
    
    #=================================================
    #Ativando frame1
    #self.BT_CadastroLEFT_1.width
    #=================================================
        
    if largura1 == 0:
        novaLargura1 = 40

    else:
        novaLargura1 = 0

    self.animation = QtCore.QPropertyAnimation(Qframe1, b"minimumWidth")
    self.animation.setDuration(500) 
    self.animation.setStartValue(largura1)
    self.animation.setEndValue(novaLargura1)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()