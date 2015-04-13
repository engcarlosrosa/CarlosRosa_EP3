# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:37:09 2015

@author: pccb
"""

alimentos=open("alimentos.csv","r+")
leitura_a=alimentos.readlines()

NutritionFacts ={}

for contador,linha in enumerate(leitura_a[1:]):
#    print(("linha %d = %s"%(contador,linha)))
#    print(type(linha))
    
    partes = linha.split(',')
#    print(type(partes))
#    print(partes)
    ahundredgrams=int(partes[1])
    calories=float(partes[2])
#    print(type(ahundredgrams))
#    print(type(calories))    
    
    NutritionFacts[partes[0]]=calories/ahundredgrams
    
'''
    for p in partes:
        print(p)     


print(NutritionFacts)
'''
print(leitura_a)
'''
SearchNutritionFacts = NutritionFacts.get('PATE')
print(SearchNutritionFacts)
'''