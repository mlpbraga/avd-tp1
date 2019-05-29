
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import itertools as it
import math as m


# In[2]:


def um_menos_um(valor, maximo):
    if (valor == maximo):
        return 1
    else: 
        return -1


# In[3]:


def calcula_q(resultados_y, matriz_uns, nomes_fatores, num_fatores):
    q = [ 0 for x in range(0,matriz_uns.shape[0])]
    q[0] = sum(resultados_y)
    aux = 0
    for i in range(0, len(nomes_fatores)):
        for c, r in matriz_uns.iterrows():
            q[i+1] += r[i]*r['Y']
            aux = i+2

    comb = anagramas(nomes_fatores,num_fatores)
    qtd_comb = len(comb)

    while qtd_comb > 0:
        essa_comb = comb[qtd_comb-1]
        for c, r in matriz_uns.iterrows():
            pre = 1
            for index in essa_comb:
                pre*=r[index]
            q[aux] += pre*r['Y']
        aux += 1
        qtd_comb -= 1
    return list(map(lambda x : (1/4)*x,q))

# calcula_q(resultados_y, n, nomes_fatores, num_fatores)


# In[4]:


def gera_sistema_eq(matriz_uns,q,nomes_fatores,num_fatores):
    fatores = []
    comb = anagramas(nomes_fatores,num_fatores)

    for c, r in matriz_uns.iterrows():
        fator = [q[0]]
        for i in range(0,len(nomes_fatores)):
            temp = r[nomes_fatores[i]]*q[i+1]
            fator.append(temp)
            aux = i+2

        qtd_comb = 0  

        while qtd_comb < len(comb):
            atual = comb[qtd_comb]
            pre = q[aux]
            for index in atual:
                pre*=r[index]
            fator.append(pre)
            aux += 1
            qtd_comb += 1

        fatores.append(fator)

    return fatores

# gera_sistema_eq(n,q,nomes_fatores,num_fatores)


# In[5]:


def anagramas(lista_nomes, num_fatores):
    i = num_fatores
    combinacoes = []
    while i > 1:
        aux = [" ".join(perm).split(' ') for perm in it.combinations(lista_nomes[:i],i)]
        combinacoes += aux
        i-=1
    return combinacoes


# In[6]:


def dois_fatores(lista_fatores):
    #2 fatores

    fatorA = lista_fatores[0]
    fatorB = lista_fatores[1]

    valores = []
    for a in fatorA:
        for b in fatorB:
            valores.append([a,b])
            
    uns = []
    for a in fatorA:
        a0 = um_menos_um(a, max(fatorA))
        for b in fatorB:
            b0 = um_menos_um(b, max(fatorB))
            uns.append([a0,b0])
    
    return pd.DataFrame(valores, columns = ['A', 'B']), pd.DataFrame(uns, columns = ['A', 'B'])

# matriz_valores, matriz_uns = dois_fatores([[1,2],[4,16]])


# In[7]:


def tres_fatores(lista_fatores):
    #3 fatores
    fatorA = lista_fatores[0]
    fatorB = lista_fatores[1]
    fatorC = lista_fatores[2]

    valores = []
    for a in fatorA:
        for b in fatorB:
            for c in fatorC:
                valores.append([a,b,c])
    
    uns = []
    for a in fatorA:
        a0 = um_menos_um(a, max(fatorA))
        for b in fatorB:
            b0 = um_menos_um(b, max(fatorB))
            for c in fatorC:
                c0 = um_menos_um(c, max(fatorC))
                uns.append([a0,b0,c0])
                
    return pd.DataFrame(valores, columns=['A','B','C']), pd.DataFrame(uns, columns = ['A', 'B', 'C'])

# matriz_valores, matriz_uns = tres_fatores([[1,2],[4,16], [2,8]])


# In[8]:


def quatro_fatores(lista_fatores):
    #4 fatores

    fatorA = lista_fatores[0]
    fatorB = lista_fatores[1]
    fatorC = lista_fatores[2]
    fatorD = lista_fatores[3]

    valores = []
    for a in fatorA:
        for b in fatorB:
            for c in fatorC:
                for d in fatorD:
                    valores.append([a,b,c,d])
                    
    uns = []
    for a in fatorA:
        a0 = um_menos_um(a, max(fatorA))
        for b in fatorB:
            b0 = um_menos_um(b, max(fatorB))
            for c in fatorC:
                c0 = um_menos_um(c, max(fatorC))
                for d in fatorD:
                    d0 = um_menos_um(d, max(fatorD))
                    uns.append([a0,b0,c0,d0])
    
    return pd.DataFrame(valores, columns=['A','B','C','D']), pd.DataFrame(uns, columns=['A','B','C','D'])

# matriz_valores, matriz_uns = quatro_fatores([[1,2],[4,16],[2,8],[19,1]])


# In[9]:


def recebe_y(matriz, nomes_fatores):
    ys = []
    for i, r in matriz.iterrows():
        print('\33[94mQual o valor de Y para os seguintes valores: ')
        for nome in nomes_fatores:
            print('\33[93m{0} = {1} '.format(nome,r[nome]), end='; ')    
        y = int(input('\33[95mY : '))
        ys.append(y)
    return ys


# In[10]:


def recebe_ys(matriz, nomes_fatores):
    ys = []
    for i, r in matriz.iterrows():
        print('\33[94mQuais os 3 valores de Y (y0,y1,y2) para os seguinte experimento: ')
        for nome in nomes_fatores:
            print('\33[93m{0} = {1} '.format(nome,r[nome]), end='; ')    
        y = int(input('\33[95mY : '))
        y = y.strip('[').strip(']').strip('(').strip(')').split(',')
        y = (int(y[0]), int(y[1]), int(y[2]))
        ys.append(y)
    return ys


# In[11]:


def importancias(lista, nomes_fatores):
    print('\33[92mO desempenho médio é: {0} MIPS'.format(lista[0]))
    indice = 1
    for nome in nomes_fatores:
        print('\33[92mO efeito do fator {0} é: {1} MIPS'.format(nome, lista[indice]))
        indice+=1
    comb = anagramas(nomes_fatores,len(nomes_fatores))
    for co in comb:
        print('\33[92mO a interação entre {0} contribuí com: {1} MIPS'.format(co, lista[indice]))
# importancias([40,20,10,5], ['A', 'B'])


# In[12]:


def sst(q, num_fatores, e=0):
    porcoes = q[1:]
    partes = []
    soma = 0 + e
    doisk = 2**num_fatores
    for q in porcoes:
        soma += doisk*q*q
        partes.append(doisk*q*q)
    return soma,partes


# In[13]:


def valor_porcentagens(ssx, sst):
    return (ssx*100)/sst


# In[14]:


def teto_chao (a):
    decimal = a%int(a)
    if decimal >= 0.5:
        return (m.ceil(a))
    else:
        return (m.floor(a))


# In[15]:


def calcula_porcentagens(q, num_fatores):
    ssts = sst(q,num_fatores)
    p = []

    for each in ssts[1]:
        aux = teto_chao((each*100)/ssts[0])
        p.append(aux)

    return p


# In[16]:


def calcula_porcentagens_erro(q, num_fatores, e):
    ssts = sst(q,num_fatores)+e
    p = []

    for each in ssts[1]:
        aux = teto_chao((each*100)/ssts[0])
        p.append(aux)

    return p


# In[17]:


def imprime_porcentagens(porcentags, nomes_fatores):
    print('\33[92mA porcentagem de relevância de cada fator é:')
    indice = 0
    for nome in nomes_fatores:
        print('\33[92m- Fator {0} : {1}%'.format(nome, porcentags[indice]))
        indice+=1
    comb = anagramas(nomes_fatores,len(nomes_fatores))
    for co in comb:
        print('\33[92m- Combinação {0} : {1}%'.format(co, porcentags[indice]))


# In[18]:


def calcula_porcentagens_erro(q, num_fatores, e):
    ssts = sst(q,num_fatores,e)
    p = []

    for each in ssts[1]:
        aux = teto_chao((each*100)/ssts[0])
        p.append(aux)

    return p


# In[19]:


def erro(lista, num):
    valores = []
    for elemento in lista:
        valores.append(elemento-num)
    return valores


# In[20]:


def calcula_erros(obtido, esperados):
    i = 0
    erros = []
    for conjunto in obtido:
        erros.append(erro(conjunto,esperados[i]))
        i+=1
    return erros


# In[21]:


def sse(erros):
    soma = 0
    for l in erros:
        for c in l:
            soma += c**2
    return soma


# In[22]:


def recebe_ys(matriz, nomes_fatores):
    ys = []
    esperado = []
    for i, r in matriz.iterrows():
       
        print('\33[94mQuais os 3 valores de Y (y0,y1,y2) para os seguinte experimento: ')
        for nome in nomes_fatores:
            print('\33[93m{0} = {1} '.format(nome,r[nome]), end='; ')    
        y = input('\33[95mY : ')
        y = y.strip('[').strip(']').strip('(').strip(')').split(',')
        y = (int(y[0]), int(y[1]), int(y[2]))
        ys.append(y)
        print('\33[94mQual era o Y esperado para esse experimento: ')
        y = int(input('\33[95mY : '))
        esperado.append(y)
    return ys, esperado


# In[23]:


def aplica_media_y(lista_ys):
    medias = []
    for ys in lista_ys:
        medias.append(sum(ys)/len(ys))
    return medias

