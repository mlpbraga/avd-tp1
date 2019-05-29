
# coding: utf-8

# ## Projeto de Experimento 2ˆ(k)r Fatorial¶
# Busca estimar erros experimentais que o Projeto 2^k Fatorial não consegue estimar.

# In[1]:


import pandas as pd
import numpy as np
import itertools as it
import math as m
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
        
    resultados_ys_obtidos, resultados_ys_esperados = recebe_ys(matriz_valores, nomes_fatores)
    print('')
    
    erros = calcula_erros(resultados_ys_obtidos,resultados_ys_esperados)
    sses = sse(erros)
    medias_y = aplica_media_y(resultados_ys_obtidos)
    
    matriz_valores['Y'] = medias_y
    matriz_uns['Y'] = medias_y
    matriz_valores['Y^'] = medias_y
    matriz_uns['Y^'] = medias_y
    
    
    q = calcula_q(medias_y, matriz_uns, nomes_fatores, num_fatores)  
     
    sistema_eq = gera_sistema_eq(matriz_uns,q,nomes_fatores,num_fatores)
    
    importancias(q, nomes_fatores)
    print('')
    
    porcentags = calcula_porcentagens_erro(q, num_fatores, sses)
    imprime_porcentagens(porcentags, nomes_fatores)
    print('\33[0m')
    return matriz_valores, matriz_uns, q, sistema_eq


m, n, q, seq = main_interativa()


# In[3]:


# 75, 75, 81 
# 77
# 45, 48, 51
# 48
# 25, 28, 19
# 24
# 15, 18, 12
# 15

