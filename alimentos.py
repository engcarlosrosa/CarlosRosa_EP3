# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:37:09 2015

@author: pccb
"""

alimentos=open("alimentos.csv","r+")
leitura_a=alimentos.readlines()

for contador,linha in enumerate(leitura_a):
    print(("linha %d = %s"%(contador,linha)))
    print(type(linha))
    
    partes = linha.split(',')
    print(type(partes))
    print(partes)
    for p in partes:
        print(p)
        