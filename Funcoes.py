# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:49:53 2015

@author: Carlos
"""


from dados_do_usuario import UserDayCaloriesWeek
from dados_do_usuario import UserFoodGramsWeek
from dados_do_usuario import CalculaTMBmultAF

#{k : v * NutritionFacts[k] for k, v in UserFoodGramsWeek.items() if k in NutritionFacts}



def CalculaGramsCaloriesGrams(d1, d2):
    d3 = dict()
    for k in d1:
        if k in d2:
            d3[k] = d1[k] * d2[k]
    return d3

def CalculaSumUserDayCaloriesWeek():
    a=(sum(UserDayCaloriesWeek.values()))
    return a
    #print("O total de calorias consumidas é de ",a, "calorias por dia.")



def CalculasumgmultcpergsubtraiCalculaTMBmultAF():
    f=(CalculaSumUserDayCaloriesWeek()-CalculaTMBmultAF())
    return f
    

print("O seu balanço calórico diario é de ", CalculasumgmultcpergsubtraiCalculaTMBmultAF()," calorias")
print(CalculaSumUserDayCaloriesWeek())