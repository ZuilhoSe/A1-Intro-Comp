import comandos
import re
from datetime import datetime

#Função que recolhe o caminho do arquivo;
def caminho_arquivo():
    caminho_do_arquivo = input()
    return caminho_do_arquivo

#Função que lê o arquivo de texto e retorna as linhas do arquivo em forma de lista;
def ler_arquivo_texto(arquivo):
    try: 
        arq = open(arquivo, "r", encoding='utf-8') 
    except FileNotFoundError:
        print("Arquivo de texto não encontrado. Feche essa janela e rode o app.py novamente.")
        input("Pressione qualquer tecla pra finalizar.")
        quit()

    linhas = arq.readlines()
    return linhas

#Função que lê o arquivo de comandos e retorna os comandos em forma de lista, todos em letras minúsculas;
def ler_arquivo_comandos(arquivo):
    try: 
        arq = open(arquivo, "r", encoding='utf-8') 
    except FileNotFoundError:
        print("Arquivo de comandos não encontrado. Feche essa janela e rode o app.py novamente.")
        input("Pressione qualquer tecla pra finalizar.")
        quit()

    linhas = arq.readlines()
    lista_de_comandos = []

    #Aqui temos uma expressão em RegEx para procurar cada um dos comandos no texto.
    for i in range(len(linhas)):
        if re.search("Agrupar\s|Agrupar\Z|Maior\s|Maior\Z|Preguiça\s|Preguiça\Z|Contar\s|Buscar\s|Substituir\s", linhas[i]):
            comandos_por_linha = re.findall("Agrupar\s|Agrupar\Z|Maior\s|Maior\Z|Preguiça\s|Preguiça\Z|Contar\s.\w+|Buscar\s.\w+|Substituir\s.\w+\s\w+", linhas[i])
            lista_de_comandos.extend(comandos_por_linha)

    return lista_de_comandos

#Função que define a hora quando é chamada;
def data_agora():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string	

#Criação do nome do arquivo log que sera editado durante a execução;
def criar_arquivo_log():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H_%M_%S")
    nome_do_arquivo = "log_" + dt_string
    return nome_do_arquivo

#Função que escreve no arquivo de texto;
def escrever_log(nome_do_arquivo, resultado, comando, horario):
    log = open(nome_do_arquivo, "a", encoding='utf-8')
    log.writelines(str(comando) + " " + str(horario) + "\n")
    log.writelines(resultado)
    log.writelines("\n\n\n")
    log.close()

#Função que executa os comandos em ordem;
def execucao_dos_comandos(arquivo, lista_de_comandos):
    nome_log = criar_arquivo_log()
    #Executa cada uma das funções na ordem;
    for i in range(len(lista_de_comandos)):
        #Caso onde o comando é AGRUPAR;
        if re.search("Agrupar", lista_de_comandos[i]):
            print("Agrupar")
            arquivo_agrupado = comandos.Agrupar(arquivo)
            print("\n\n")
            escrever_log(nome_log, arquivo_agrupado, "Agrupar", data_agora())
        
        #Caso onde o comando é MAIOR;
        elif re.search("Maior", lista_de_comandos[i]):
            print("Maior")
            arquivo_agrupado = comandos.Maior(arquivo)
            print("\n\n")
            escrever_log(nome_log, arquivo_agrupado, "Maior", data_agora())
        
        #Caso onde o comando é PREGUIÇA;
        elif re.search("Preguiça", lista_de_comandos[i]):
            print("Preguiça")
            arquivo_agrupado = comandos.Preguiça(arquivo)
            print("\n\n")
            escrever_log(nome_log, arquivo_agrupado, "Preguiça", data_agora())
       
        #Caso onde o comando é CONTAR;
        elif re.search("Contar", lista_de_comandos[i]):
            print("Contar")
            x = lista_de_comandos[i].split(" ")
            print("\n\n")
            comandos.Contar(arquivo, x[1])
            escrever_log(nome_log, arquivo_agrupado, "Contar", data_agora())
       
        #Caso onde o comando é BUSCAR;
        elif re.search("Buscar", lista_de_comandos[i]):
            print("Buscar")
            x = lista_de_comandos[i].split(" ")
            print("\n\n")
            comandos.Buscar(arquivo, x[1])
            escrever_log(nome_log, arquivo_agrupado, "Buscar", data_agora())
       
        #Caso onde o comando é SUBSTITUIR;
        elif re.search("Substituir", lista_de_comandos[i]):
            print("Substituir")
            x = lista_de_comandos[i].split(" ")
            print("\n\n")
            comandos.Substituir(arquivo, x[1], x[2])
            escrever_log(nome_log, arquivo_agrupado, "Substituir", data_agora())