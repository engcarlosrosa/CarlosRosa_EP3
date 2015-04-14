# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:32:39 2015

@author: Carlos
"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from dados_do_usuario import UserDayCaloriesWeek


from Funcoes import CalculaTMBmultAF
from Funcoes import CalculaSumUserDayCaloriesWeek

# Example data
categoria = ('Calorias consumidas','calorias recomendadas',)
y_pos = np.arange(len(categoria))
quantidade = [CalculaSumUserDayCaloriesWeek(),CalculaTMBmultAF()]
plt.barh(y_pos, quantidade, align='center', alpha=0.4)
plt.yticks(y_pos, categoria)
plt.xlabel('Quantidade (calorias)')
plt.title('Quantidade diaria recomendada vs consumida')
plt.show()


print(list(UserDayCaloriesWeek.keys()))
print(UserDayCaloriesWeek.values())
num_days = len(list(UserDayCaloriesWeek.keys()))

plt.plot(list(range(num_days)),list(UserDayCaloriesWeek.values()))
#plt.axis([0,UserDayCaloriesWeek[10],0,UserDayCaloriesWeek[10]])
plt.xlabel("Dias da semana]")
plt.ylabel("Calories")
plt.title("Quantidade de Calorias ao longo da semana")
plt.show()
