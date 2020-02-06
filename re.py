# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:54:40 2020

@author: MICHAEL
"""

import pandas as pd
import numpy as np
import re

df = pd.read_csv("C:/Users/MICHAEL/Desktop/Python/Pasta1.csv", encoding='latin-1', error_bad_lines=False, warn_bad_lines=False, sep=r'[()]') #Checar processo de entrada do arquivo. Alterar esse trecho se necessário!
## encoding='latin-1', error_bad_lines=False, warn_bad_lines=False

lista_valores_minimos = [] #Lista que conterá todos os valores mínimos (valor mínimo de cada linha da tabela, ou seja, por mensagem)

for i in range(len(df)):
    
    lista_valores_string = []  #Lista que conterá os valores por mensagem 
    lista_valores_string = re.findall(r"(?:[\£\$\€]{1}[,\d]+.?\d*)[-+]?\d*\,?\d+", df["Mensagem_Personalizada"][i])  #Lista dos valores monetários por mensagem
    
    for i in range(len(lista_valores_string)): #Tratando a lista com os valores por mensagem
        
        if lista_valores_string[i].find("$") == 0:
            
            lista_valores_string[i] = lista_valores_string[i].replace("$", "")
            lista_valores_string[i] = lista_valores_string[i].replace(',', '.')
            i = i + 1  
            
    array_valores_string = np.array(lista_valores_string) #transformando a lista dos valores em array
    array_valores_string = array_valores_string.astype(np.float) #convertendo para float
    try:
        minimo_string = np.amin(array_valores_string) #dos valores, verificando qual é o menor
    except ValueError:
        pass
    lista_valores_minimos.append(minimo_string) #adicionando o valor mínimo das respectivas mensagens em ordem (linha por linha)
    
 
array_valores_minimos = np.array(lista_valores_minimos) #valores minimos em array
df["Valores Minimos"] = array_valores_minimos #adicionando coluna no dataframe com os respectivos valores minimos por linha.

## IMPEDIMENTOS   
  ## Se existir espaço entre o cifrão e o valor monetário nas strings.
  ## Valores monetários faltantes na coluna mensagem, por exemplo, uma linha sem a mensagem. 
           

## TESTES

string = "OFERTACO ARCOMIX/FORTBRASIL Cordao de file ou Picanha suina congelada R$19,99kg cada, Salsichao TONY ou Filezinho sassami AURORA R$10,99 kg cada Val:31/12"
string2 = "19.99"
string3 = "Leve com seu BanBan Card, o presente para toda a familia. Tenis Infantil Feminino- R$59,99.Val 27/12"

a = re.findall(r"(?:[\£\$\€]{1}[,\d]+.?\d*)[-+]?\d*\,?\d+", string3)
(?:[\£\$\€]{1}[,\d]+.?\d*)

for i in range(len(a)):
    
    if a[i].find("$") == 0:
        a[i] = "R" + a[i]
    i = i + 1   

teste = teste.replace(',', '.')  ##virgula para ponto (precisamos trabalhar com valores mometarios float)
teste2 = teste2.replace("$", "") ##tirar o cifrão real 

for i in range(len(a)):
    
    if a[i].find("$") == 0:
        a[i] = a[i].replace("$", "")
        a[i] = a[i].replace(',', '.')
    i = i + 1  
    
b = np.array(a)
b = b.astype(np.float)
minimo = np.amin(b)


