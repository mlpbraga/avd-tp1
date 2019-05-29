
# coding: utf-8

# ## Projeto de Experimento 2ˆk Fatorial
# 
# O intuito desse algoritmo é mostrar qual a relevância de cada fator utilizado para realizar os experimentos. 

# In[1]:


import pandas as pd
import numpy as np
import itertools as it
from uteis import *

s = {
    2:['A', 'B'],
    3:['A', 'B', 'C'],
    4:['A', 'B', 'C', 'D']
}


# In[2]:


def main_interativa():
    num_fatores = int(input('\33[94mInsira o número de fatores utilizados: '))
    print('')
    nomes_fatores = []

    if num_fatores in s:
        nomes_fatores = s[num_fatores]
    
    valores_fatores = []
    for nome in nomes_fatores:
        print('\33[94mLista de valores [max,min] utilizados para o fator {0}\33[0m'.format(nome))
        fator = input(': ')
        fator = fator.strip('[').strip(']').split(',')
        fator = [int(x) for x in fator]
        valores_fatores.append(fator)
    
    print('')
    
    if num_fatores == 2:
        matriz_valores, matriz_uns = dois_fatores(valores_fatores)
    elif num_fatores == 3:
        matriz_valores, matriz_uns = tres_fatores(valores_fatores)
    elif num_fatores == 4:
        matriz_valores, matriz_uns = quatro_fatores(valores_fatores)
        
    resultados_y = recebe_y(matriz_valores, nomes_fatores)
    print('')
    
    matriz_valores['Y'] = resultados_y
    matriz_uns['Y'] = resultados_y
    
    q = calcula_q(resultados_y, matriz_uns, nomes_fatores, num_fatores)  
     
    sistema_eq = gera_sistema_eq(matriz_uns,q,nomes_fatores,num_fatores)
    
    importancias(q, nomes_fatores)
    print('')
    porcents = calcula_porcentagens(q, num_fatores)
    
    imprime_porcentagens(porcents, nomes_fatores)
    print('\33[0m')
    return matriz_valores, matriz_uns, q, sistema_eq

m, n, q, seq = main_interativa()


# In[3]:


n


# In[4]:


q


# In[5]:


seq

