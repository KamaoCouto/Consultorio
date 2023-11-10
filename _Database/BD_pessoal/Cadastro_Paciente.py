#==========================================================================================================
#======>    Imports
#==========================================================================================================

import mysql.connector

Conexão = mysql.connector.connect (

host        = 'localhost',
user        = 'root',
password    = '',
database    = 'cadastro',
    
)
#==========================================================================================================
#======>    Variáveis
#==========================================================================================================  

    
def Novo_Paciente (self,
                      
    Qframe1,  # TXT_Nome_Completo
    Qframe2,  # TXT_Data_Nasc
    Qframe3,  # TXT_RG
    Qframe4,  # TXT_CPF
    Qframe5,  # self.TXT_Nome_Responsavel, 
    Qframe6,  # self.TXT_Data_Nasc_Responsavel,
    Qframe7,  # TXT_Logradouro, 
    Qframe8,  # self.TXT_Numero, 
    Qframe9,  # TXT_Complemento_Log,
    Qframe10,  # TXT_CEP, 
    Qframe11, # TXT_Municipio, 
    Qframe12, # self.TXT_Cidade, 
    Qframe13, # self.TXT_Estado, 
    Qframe14, # self.TXT_Profissao, 
    Qframe15, # self.TXT_Nacionalidade, 
    Qframe16, # TXT_email_1,
    Qframe17, # TXT_Cel_Contato_1
    Qframe18, # TXT_email_2,
    Qframe19, # TXT_Cel_Contato_2,
    Qframe20, # TXT_email_3,
    Qframe21, # TXT_Cel_Contato_3,
    Qframe22, # TXT_email_4,
    Qframe23, # TXT_Cel_Contato_4,
    
#    QframeBT1, # self.BT_sexo_Fem,
#    QframeBT2, # self.BT_sexo_Masc,
#    QframeBT3, # self.BT_sexo_Outros,
#    QframeBT4, # self.BT_sexo_Ocultar, 
         
    ):
    
#==========================================================================================================
#======>    Variáveis
#==========================================================================================================
    
    
    linha_1     = Qframe1.text  ()  # TXT_Nome_Completo
    linha_2     = Qframe2.text  ()  # TXT_Data_Nasc
    linha_3     = Qframe3.text  ()  # TXT_RG
    linha_4     = Qframe4.text  ()  # TXT_CPF
    linha_5     = Qframe5.text  ()  # self.TXT_Nome_Responsavel, 
    linha_6     = Qframe6.text  ()  # self.TXT_Data_Nasc_Responsavel,
    linha_7     = Qframe7.text  ()  # TXT_Logradouro, 
    linha_8     = Qframe8.text  ()  # self.TXT_Numero, 
    linha_9     = Qframe9.text  ()  # TXT_Complemento_Log,
    linha_10    = Qframe10.text ()  # TXT_CEP, 
    linha_11    = Qframe11.text ()  # TXT_Municipio, 
    linha_12    = Qframe12.text ()  # self.TXT_Cidade, 
    linha_13    = Qframe13.text ()  # self.TXT_Estado, 
    linha_14    = Qframe14.text ()  # self.TXT_Profissao, 
    linha_15    = Qframe15.text () # self.TXT_Nacionalidade,    
    linha_16    = Qframe16.text  () # TXT_email_1,
    linha_17    = Qframe17.text  () # TXT_Cel_Contato_1
    linha_18    = Qframe18.text  () # TXT_email_2,
    linha_19    = Qframe19.text  () # TXT_Cel_Contato_2,
    linha_20    = Qframe20.text  () # TXT_email_3,
    linha_21    = Qframe21.text  () # TXT_Cel_Contato_3,
    linha_22    = Qframe22.text  () # TXT_email_4,
    linha_23    = Qframe23.text  () # TXT_Cel_Contato_4,
    
#    Qbt1    = QframeBT1  () # self.BT_sexo_Fem,
#    Qbt2    = QframeBT2  () # self.BT_sexo_Masc,
#    Qbt3    = QframeBT3  () # self.BT_sexo_Outros,
#    Qbt4    = QframeBT4  () # self.BT_sexo_Ocultar,  

#==========================================================================================================
#======>    Configurando Gênero
#==========================================================================================================
#    Config_Genero = ""
    
#    if Qbt1 == True :
#        Config_Genero = "Feminino"
        
#    elif Qbt2 == True :
#        Config_Genero = "Masculino"
        
#    elif Qbt3 == True :
#        Config_Genero = "Outros"
        
#    elif Qbt4 == True :
#        Config_Genero = "N/A"              

#    else :
#        Config_Genero = "Não_Informado"

#==========================================================================================================
#======>   (COMANDO_SQL) = {Form_UI} <---> {dados_pessoais} 
#==========================================================================================================

    Cursor = Conexão.cursor()
    Key_SQL = "INSERT INTO Dados_Pessoais (Nome,Data_de_Nascimento,RG,CPF,Nome_Responsavel,Data_Nasc_Responsavel,Logradouro,Numero,Complemento,CEP,Municipio,Cidade,Estado,Profissao,Nacionalidade,Email_1,Contato_1,Email_2,Contato_2,Email_3,Contato_3,Email_4,Contato_4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    Data_Cadastro = (       
        linha_1,
        linha_2,
        linha_3,
        linha_4,
        linha_5,
        linha_6,
        linha_7,
        linha_8,
        linha_9,
        linha_10,
        linha_11,
        linha_12,
        linha_13,
        linha_14,
        linha_15,
        linha_16,
        linha_17,
        linha_18,
        linha_19,
        linha_20,
        linha_21,
        linha_22,
        linha_23,        
        )

#==========================================================================================================
#======>    (UP_TO_BD) = {dados_pessoais}
#==========================================================================================================
        
    Cursor.execute      (Key_SQL,Data_Cadastro)
    Conexão.commit      ()
    
#==========================================================================================================
#======>    (LIMPAR_CAMPOS) = {Form_UI}
#==========================================================================================================
    
#    Qframe1.setText     ("")
#    Qframe2.setText     ("")
#    Qframe3.setText     ("")
#    Qframe4.setText     ("")
#    Qframe5.setText     ("")
#    Qframe6.setText     ("")
#    Qframe7.setText     ("")
#    Qframe8.setText     ("")
#    Qframe9.setText     ("")
#    Qframe10.setText    ("")
#    Qframe11.setText    ("")
#    Qframe12.setText    ("")
#    Qframe13.setText    ("")
#    Qframe14.setText    ("")
#    Qframe15.setText    ("")
#    Qframe16.setText    ("")
#    Qframe17.setText    ("")
#    Qframe18.setText    ("")
#    Qframe19.setText    ("")
#    Qframe20.setText    ("")
#    Qframe21.setText    ("")
#    Qframe22.setText    ("")
#    Qframe23.setText    ("")
    
    