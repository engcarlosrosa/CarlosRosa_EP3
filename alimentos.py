# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:37:09 2015

@author: pccb
"""

def alimentoscsv():
    alimentos=open("alimentos.csv","r")
    leitura_a=alimentos.readlines()
    NutritionFactsCalPerGram ={}
    for contador,linha in enumerate(leitura_a[1:]):
        #print(("linha %d = %s"%(contador,linha)))
        #print(type(linha))
        
        partes = linha.split(',')
        #print(type(partes))
        #print(partes)
        ahundredgrams=int(partes[1])
        calories=float(partes[2])
        carboidrates=float(partes[4])
        fat=float(partes[5])
        #print(type(ahundredgrams))
        #print(type(calories))    
        #print(proteins)
        #print(carboidrates)
        #print(fat)
        NutritionFactsCalPerGram[partes[0]]=calories/ahundredgrams
    return NutritionFactsCalPerGram
alimentoscsv()

def alimentosproteinascsv():
    alimentos=open("alimentos.csv","r")
    leitura_a=alimentos.readlines()
    NutritionFactsProteinPerGram={}
    for contador,linha in enumerate(leitura_a[1:]):
        partes=linha.split(',')
        ahundredgrams=int(partes[1])
        proteins=float(partes[3])
        NutritionFactsProteinPerGram[partes[0]]=proteins/ahundredgrams
    return NutritionFactsProteinPerGram
alimentosproteinascsv()
print(alimentosproteinascsv())

def proteins():
    alimentos=open("alimentos.csv","r")
    leitura_a=alimentos.readlines()
    for contador,linha in enumerate(leitura_a[1:]):
        partes=linha.split(',')
        proteins=float(partes[3])
        return proteins
proteins()

'''
SearchNutritionFactsCalPerGram = NutritionFactsCalPerGram.get('PATE')
print(SearchNutritionFactsCalPerGram)
'''
