# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:13:25 2015

@author: pccb
"""


dados_usuario= open("usuario.csv","r+")
leitura=dados_usuario.readlines()

def CalculaTaxaMetabolismoBasal(peso,altura,idade):
    TMB= 88.36+(13.4*weight)+(4.8*height)-(5.7*age)
    return TMB

def CalculaTMBmultAF():
    taoccd=CalculaTaxaMetabolismoBasal(weight,height,age)*1.725
    return taoccd

def ReturnWeight():
    Weight = weight
    return Weight
    
def ReturnHeight2():
    Height2 = height**2
    return Height2
    

def CalculaBMI(ReturnWeight,ReturnHeight2):
    BMI=(ReturnWeight())/(ReturnHeight2())  
    return BMI

def ReturnTypeBMI():
    if CalculaBMI(ReturnWeight,ReturnHeight2)<18.5:
        print("Você está abaixo do peso")
    elif 18.5<=CalculaBMI(ReturnWeight,ReturnHeight2)<25:
        print("Você tem peso ideal")
    elif 25<=CalculaBMI(ReturnWeight,ReturnHeight2)<30:
        print("Você esta ligeiramente acima do peso")
    else:
        print("Você esta muito acima do peso")
    
UserDietWeek={}

userpeaces = leitura[1].split(",")

name = userpeaces[0]
age = int(userpeaces[1])
weight = float(userpeaces[2])
sex = userpeaces[3]
height = float(userpeaces[4])
fator = userpeaces[5]

x=0
for linha in leitura[3:]:
    x+=1
    userpeaces = linha.split(',')
#    print(userpeaces)
    
    

    usergramsamount=int(userpeaces[2])
    #print(type(usergramsamount))
 
    food=userpeaces[1]
    calories=int(userpeaces[2])
    
    UserDietWeek[food]=calories
#print(UserDietWeek)
   
print("Sua taxa de metabolismo basal é ",CalculaTaxaMetabolismoBasal(weight,height,sex))
print("Seu gasto calorico diário é de ",CalculaTMBmultAF()," calorias.")
print("O seu índice de massa corporal é de ",CalculaBMI(ReturnWeight,ReturnHeight2), "Kg/m2")
ReturnTypeBMI()