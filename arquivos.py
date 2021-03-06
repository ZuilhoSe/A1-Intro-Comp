import comandos
import re
from datetime import datetime

#Função que recolhe o caminho do arquivo;
def caminho_arquivo():
    arquivo_txt = False
    #Tratamento do caso onde o arquivo não é um .txt;
    while arquivo_txt != True:
        caminho_do_arquivo = input()
        if re.search(".txt\Z", caminho_do_arquivo):
            arquivo_txt = True
            print("Arquivo .txt! É válido!")
        else:
            print("Não é um .txt! Coloque um arquivo válido!\n")
    return caminho_do_arquivo

#Função que lê o arquivo de texto e retorna as linhas do arquivo em forma de lista;
def ler_arquivo_texto(arquivo):
    #Tratamento do caso onde o arquivo não é encontrado;
    try: 
        arq = open(arquivo, "r", encoding='utf-8') 
    except FileNotFoundError:
        print("Arquivo de texto não encontrado. Feche essa janela e rode o app.py com o caminho correto!")
        input("Pressione qualquer tecla pra finalizar.")
        quit()
    linhas = arq.readlines()

    return linhas

#Função que lê o arquivo de comandos e retorna os comandos em forma de lista;
def ler_arquivo_comandos(arquivo):
    #Tratamento do caso onde o arquivo não é encontrado;
    try: 
        arq = open(arquivo, "r", encoding='utf-8') 
    except FileNotFoundError:
        print("Arquivo de comandos não encontrado. Feche essa janela e rode o app.py com o caminho correto!.")
        input("Pressione qualquer tecla pra finalizar.")
        quit()
    linhas = arq.readlines()

    #Criação do arquivo que será editado;
    arquivo_editavel = ""
    for linha in linhas:
        arquivo_editavel = arquivo_editavel + linha

    #Lista que recebe os comandos separados;
    lista_de_comandos = []

    #Expressão RegEx para procurar cada um dos comandos no texto;
    if re.search("Agrupar\s|Agrupar\Z|Maior\s|Maior\Z|Preguiça\s|Preguiça\Z|Contar\s|Buscar\s|Substituir\s", arquivo_editavel):
        comandos_por_linha = re.findall("Agrupar\s|Agrupar\Z|Maior\s|Maior\Z|Preguiça\s|Preguiça\Z|Contar\s+.*?(?=\s)|Buscar\s+.*?(?=\s)|Substituir\s+.*?(?=\s)\s*.*?(?=\s)", arquivo_editavel)
        lista_de_comandos.extend(comandos_por_linha)

    #Tratamento dos comandos para que fiquem com apenas espaços e sem enteres;
    lista_de_comandos_final = []

    for comando in lista_de_comandos:
        comando_junto = ""
        comando_separado = re.split("\s", comando)
        while "" in comando_separado:
            comando_separado.remove("")
        for item in comando_separado:
            comando_junto = f"{comando_junto} {item}"
        lista_de_comandos_final.append(comando_junto)

    return lista_de_comandos_final

#Função que retorna a hora quando é chamada;
def data_agora():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string	

#Criação do nome do arquivo log que sera editado durante a execução do programa;
def criar_arquivo_log():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H_%M_%S")
    nome_do_arquivo = "log_" + dt_string
    return nome_do_arquivo

#Função que escreve no arquivo de logs;
def escrever_log(nome_do_arquivo, resultado, comando, horario):
    log = open(nome_do_arquivo + ".txt", "a", encoding='utf-8')
    log.writelines(str(comando) + " " + str(horario) + "\n")
    if isinstance(resultado, str):
        log.writelines(resultado)
        log.writelines("\n\n\n")
    else:
        for linha in resultado:
            log.writelines(linha)
            log.writelines("\n")
        log.writelines("\n\n\n")

    log.close()

#Função que executa os comandos na ordem que aparecem no arquivo;
def execucao_dos_comandos(arquivo, lista_de_comandos):
    #Arquivo log que será editado no momento;
    nome_log = criar_arquivo_log()

    #Executa cada um dos comandos na ordem;
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
            maior_palavra = comandos.Maior(arquivo)
            print("\n\n")
            escrever_log(nome_log, maior_palavra, "Maior", data_agora())
        
        #Caso onde o comando é PREGUIÇA;
        elif re.search("Preguiça", lista_de_comandos[i]):
            print("Preguiça")
            arquivo_editado = comandos.Preguiça(arquivo)
            print("\n\n")
            escrever_log(nome_log, arquivo_editado, "Preguiça", data_agora())
       
        #Caso onde o comando é CONTAR;
        elif re.search("Contar", lista_de_comandos[i]):
            print("Contar")
            palavra_contada = lista_de_comandos[i].split(" ")
            print("\n\n")
            resultado = str(comandos.Contar(arquivo, palavra_contada[2]))
            escrever_log(nome_log, resultado, f"Contar {palavra_contada[2]}", data_agora())
       
        #Caso onde o comando é BUSCAR;
        elif re.search("Buscar", lista_de_comandos[i]):
            print("Buscar")
            palavra_buscada = lista_de_comandos[i].split(" ")
            print("\n\n")
            linhas_buscadas = comandos.Buscar(arquivo, palavra_buscada[2])
            escrever_log(nome_log, linhas_buscadas, f"Buscar {palavra_buscada[2]}", data_agora())
       
        #Caso onde o comando é SUBSTITUIR;
        elif re.search("Substituir", lista_de_comandos[i]):
            print("Substituir")
            palavras = lista_de_comandos[i].split(" ")
            print("\n\n")
            arquivo_substituido = comandos.Substituir(arquivo, palavras[2], palavras[3])
            escrever_log(nome_log, arquivo_substituido, f"Substituir {palavras[2]} {palavras[3]}", data_agora())