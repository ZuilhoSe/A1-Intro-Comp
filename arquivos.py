import sys
import comandos
import re
from datetime import datetime

#Função que lê o arquivo de texto e retorna as linhas do arquivo em forma de lista;
def ler_arquivo_texto(arquivo):
    arq = open(arquivo, encoding='utf-8') 
    linhas = arq.readlines()
    return linhas

#Função que lê o arquivo de comandos e retorna os comandos em forma de lista, todos em letras minúsculas;
def ler_arquivo_comandos(arquivo):
    arq = open(arquivo, "r", encoding='utf-8') 
    linhas = arq.readlines()
    
    lista_de_comandos = []

    #Aqui temos uma expressão em RegEx para procurar cada um dos comandos no texto. Cada expressão terá um regex próprio 
    for i in range(len(linhas)):
        if re.search("Agrupar\s|Maior\s|Preguiça\s|Contar\s|Buscar\s|Substituir\s", linhas[i]):
            comandos_por_linha = re.findall("Agrupar\s|Maior\s|Preguiça\s|Contar\s.\w+|Buscar\s.\w+|Substituir\s.\w+\s\w+", linhas[i])
            lista_de_comandos.extend(comandos_por_linha)

    return lista_de_comandos

def data_agora():
    #Aqui temos a definição do horário na hora que o comando e chamado
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string	

def execucao_dos_comandos(arquivo, lista_de_comandos):
    
    for i in range(len(lista_de_comandos)):
        if re.search("Agrupar", lista_de_comandos[i]):
            comandos.Agrupar(arquivo)
        elif re.search("Maior", lista_de_comandos[i]):
            comandos.Maior(arquivo)
        elif re.search("Preguiça", lista_de_comandos[i]):
            comandos.Preguiça(arquivo)
        elif re.search("Contar", lista_de_comandos[i]):
            x = lista_de_comandos[i].split(" ")
            comandos.Contar(arquivo, x[1])
        elif re.search("Buscar", lista_de_comandos[i]):
            x = lista_de_comandos[i].split(" ")
            comandos.Buscar(arquivo, x[1])
        elif re.search("Substituir", lista_de_comandos[i]):
            x = lista_de_comandos[i].split(" ")
            comandos.Substituir(arquivo, x[1], x[2])