# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:13:25 2015

@author: pccb
"""

dados_usuario= open("usuario.csv","r+")
leitura=dados_usuario.readlines()

def CalculaTaxaMetabolismoBasal(peso,altura,idade):
    TMB= 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)
    return TMB
    
Dieta_Semana={}

'''
for contador, linha in enumerate(leitura):
    print("linha %d = %s"%(contador,linha))
    
    partes = linha.split(',')

    for p in partes:
        print(p)
'''    


partes = leitura[1].split(",")

nome = partes[0]
idade = int(partes[1])
peso = float(partes[2])
sexo = partes[3]
altura = float(partes[4])
fator = partes[5]

x=0
for linha in leitura[3:]:
    '''    
    print("linha %d = %s"%(x,linha))
    '''
    x+=1
    
    partes = linha.split(',')

    '''    
    for p in partes:
    '''
    
    print(partes)
    
print("Sua taxa de metabolismo basal é ",CalculaTaxaMetabolismoBasal(peso,altura,idade))

'''
for linha in leitura[3:]:
    if linha
    '''