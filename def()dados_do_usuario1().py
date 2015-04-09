# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:13:25 2015

@author: pccb
"""

dados_usuario= open("usuario.csv","r+")
leitura=dados_usuario.readlines()

for contador, linha in enumerate(leitura):
    print("linha %d = %s"%(contador,linha))
    
    partes = linha.split(',')

    for p in partes:
        print(p)
    
    #contador+=1
    
