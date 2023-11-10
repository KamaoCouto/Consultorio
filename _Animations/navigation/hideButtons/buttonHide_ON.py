
from PySide6 import QtCore

#================================================================================
# Ativando Animações dos frames dos menus internos 
#================================================================================
#================================================================================
def Cad_Buttons_ON (self, 
                    
    Qframe1,        # self.fCad_Left_12,             # Open           # 00/40
    
    Qframe2,        # self.fCad_Left_11,             # Close          # 40/00
    Qframe3,        # self.fCad_Left_21,             # Close          # 40/00
    Qframe4,        # self.fCad_Left_31,             # Close          # 40/00
    Qframe5,        # self.fCad_Left_41,             # Close          # 40/00 
    
    ):

#================================================================================
    #Variáveis
#================================================================================

    Largura1 = Qframe1.width ()     # self.fCad_Left_12,    # Open      # 00/40
    
    Largura2 = Qframe2.width ()     # self.fCad_Left_11,    # Close     # 40/00
    Largura3 = Qframe3.width ()     # self.fCad_Left_21,    # Close     # 40/00
    Largura4 = Qframe4.width ()     # self.fCad_Left_31,    # Close     # 40/00
    Largura5 = Qframe5.width ()     # self.fCad_Left_41,    # Close     # 40/00

            

#================================================================================
            # self.fCad_Left_41,             # Close          # 40/00
#================================================================================    
    if Largura5 == 40:
        novaLargura5 = 0

    else:
        novaLargura5 = 40

    self.animation = QtCore.QPropertyAnimation  (Qframe5, b"minimumWidth")
    self.animation.setDuration                  (500) 
    self.animation.setStartValue                (novaLargura5)
    self.animation.setEndValue                  (Largura5)
    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
    self.animation.start                        ()
    
#================================================================================
            # self.fCad_Left_31,    # Close     # 40/00
#================================================================================    
    if Largura4 == 40:
        novaLargura4 = 0

    else:
        novaLargura4 = 40

    self.animation = QtCore.QPropertyAnimation  (Qframe4, b"minimumWidth")
    self.animation.setDuration                  (500) 
    self.animation.setStartValue                (novaLargura4)
    self.animation.setEndValue                  (Largura4)
    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
    self.animation.start                        ()
    
#================================================================================
            # self.fCad_Left_21,    # Close     # 40/00
#================================================================================    
    if Largura3 == 40:
        novaLargura3 = 0

    else:
        novaLargura3 = 40

    self.animation = QtCore.QPropertyAnimation  (Qframe3, b"minimumWidth")
    self.animation.setDuration                  (500) 
    self.animation.setStartValue                (novaLargura3)
    self.animation.setEndValue                  (Largura3)
    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
    self.animation.start                        ()
    
#================================================================================
            # self.fCad_Left_11,    # Close     # 40/00
#================================================================================    
    if Largura2 == 40:
        novaLargura2 = 0

    else:
        novaLargura2 = 40

    self.animation = QtCore.QPropertyAnimation  (Qframe2, b"minimumWidth")
    self.animation.setDuration                  (500) 
    self.animation.setStartValue                (novaLargura2)
    self.animation.setEndValue                  (Largura2)
    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
    self.animation.start                        ()
    
#================================================================================
            # self.fCad_Left_12,    # Open      # 00/40
#================================================================================    
    if Largura1 == 0:
        novaLargura1 = 40

    else:
        novaLargura1 = 0

    self.animation = QtCore.QPropertyAnimation  (Qframe1, b"minimumWidth")
    self.animation.setDuration                  (500) 
    self.animation.setStartValue                (Largura1)
    self.animation.setEndValue                  (novaLargura1)
    self.animation.setEasingCurve               (QtCore.QEasingCurve.InOutQuart)
    self.animation.start                        ()    