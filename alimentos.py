# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:37:09 2015

@author: pccb
"""


def alimentoscsv():
    alimentos=open("alimentos.csv","r")
    leitura_a=alimentos.readlines()
    NutritionFacts ={}
    for contador,linha in enumerate(leitura_a[1:]):
        #print(("linha %d = %s"%(contador,linha)))
        #print(type(linha))
        
        partes = linha.split(',')
        #print(type(partes))
        #print(partes)
        ahundredgrams=int(partes[1])
        calories=float(partes[2])
        proteins=float(partes[3])
        carboidrates=float(partes[4])
        fat=float(partes[5])
        #print(type(ahundredgrams))
        #print(type(calories))    
        #print(proteins)
        #print(carboidrates)
        #print(fat)
        NutritionFacts[partes[0]]=calories/ahundredgrams
    return NutritionFacts
alimentoscsv()

'''
SearchNutritionFacts = NutritionFacts.get('PATE')
print(SearchNutritionFacts)
'''
