from PySide6 import QtCore

#==============================================================================================
# Ativando Animações dos Botões dos menus internos 

#    40/0/40 == 40=>0 
#==============================================================================================

def Show_sideButton_ON  (self,
                       
                        Qframe1, 
                        
                        ):#Qframe    



    largura1 = Qframe1.width ()

    #=================================================
    #Ativando frame1
    #self.BT_CadastroLEFT_1.width
    #=================================================    

    if largura1 == 40:
        novaLargura1 = 0

    else:
        novaLargura1 = 40

    self.animation = QtCore.QPropertyAnimation(Qframe1, b"minimumWidth")
    self.animation.setDuration(500) 
    self.animation.setStartValue(largura1)
    self.animation.setEndValue(novaLargura1)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()