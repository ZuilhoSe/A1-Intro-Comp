import sys
import comandos
import re

#Função que lê o arquivo de texto e retorna as linhas do arquivo em forma de lista;
def ler_arquivo_texto(arquivo):
    arq = open(arquivo) 
    linhas = arq.readlines()
    return linhas

#Função que lê o arquivo de comandos e retorna os comandos em forma de lista, todos em letras minúsculas;
def ler_arquivo_comandos(arquivo, encoding="cp1252"):
    arq = open(arquivo) 
    linhas = arq.readlines()
    
    lista_de_comandos = []

    #Aqui temos uma expressão em RegEx para procurar cada um dos comandos no texto. Cada expressão terá um regex próprio 
    for i in range(len(linhas)):
        if re.search("Agrupar|Maior|Preguiça", linhas[i]):
            lista_de_apagar = re.findall("Agrupar\s|Maior\s|Preguiça", linhas[i])
            lista_de_comandos.append(lista_de_apagar)

    return lista_de_comandos