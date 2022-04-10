import sys
import comandos

#Função que lê o arquivo de texto e retorna as linhas do arquivo em forma de lista;
def ler_arquivo_texto(arquivo):
    arq = open(arquivo) 
    linhas = arq.readlines()
    return linhas

#Função que lê o arquivo de comandos e retorna os comandos em forma de lista, todos em letras minúsculas;
def ler_arquivo_comandos(arquivo):
    arq = open(arquivo) 
    linhas = arq.readlines()

    #Iterando em cima de cada linha para pegar cada comando especifico;
    lista_de_comandos = []
    for linha in linhas:
        linha = linha.lower()
        palavras = linha.split(" ")
        lista_de_comandos.extend(palavras)
        
    #Um problema que pode acontecer é se tiver um enter entre as palavras que aparece um \n, aqui tratamos isso;
    for i in range(len(lista_de_comandos)):
        tem_enter = lista_de_comandos[i].endswith("\n")
        if tem_enter == True:
            lista_de_comandos[i] = lista_de_comandos[i].replace('\n', '')
    return lista_de_comandos