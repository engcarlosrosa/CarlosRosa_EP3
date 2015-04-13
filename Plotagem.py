# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:32:39 2015

@author: Carlos
"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from Funcoes import CalculaTMBmultAF
from Funcoes import sumgmultcperg

# Example data
categoria = ('Calorias consumidas','calorias recomendadas', 'Proteinas consumidas','Proteinas recomendada', 'Carboidratos consumidos', 'Carboidratos recomendado', ' Gorduras consumidas','Gorduras recomendada')
y_pos = np.arange(len(categoria))
quantidade = [CalculaTMBmultAF(),sumgmultcperg(),(0.2*CalculaTMBmultAF()),(0.2*sumgmultcperg()),(0.5*CalculaTMBmultAF()),(0.5*sumgmultcperg()),(0.3*CalculaTMBmultAF()),(0.3*sumgmultcperg())]


plt.barh(y_pos, quantidade, align='center', alpha=0.4)
plt.yticks(y_pos, categoria)
plt.xlabel('Quantidade (calorias)')
plt.title('Quantidade diaria recomendada vs consumida')

plt.show()