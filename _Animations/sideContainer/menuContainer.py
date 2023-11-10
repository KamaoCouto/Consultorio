from PySide6 import QtCore

#==============================================================================================
# Ativando Animações dos frames dos menus internos 
#==============================================================================================

def containerMenu (self, 
                    Qframe1, 

                    ):

#=================================================
#Variáveis
#=================================================

    largura1 = Qframe1.width ()

    #=================================================
    #Ativando frame1
    #=================================================

    if largura1 == 0:
        novaLargura1 = 200

    else:
        novaLargura1 = 0

    self.animation = QtCore.QPropertyAnimation(Qframe1, b"maximumWidth")
    self.animation.setDuration(500) 
    self.animation.setStartValue(largura1)
    self.animation.setEndValue(novaLargura1)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start() 



