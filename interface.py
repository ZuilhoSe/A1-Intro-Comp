import time
import arquivos
import sys
from textwrap import wrap
from turtle import width

#Função que cria a caixa delimitadora dos títulos;
def caixa(frase, width):
    print('+-' + '-' * width + '-+')
    for line in wrap(frase, width):
        print('| {0:^{1}} |'.format(line, width))
        print('+-' + '-'*(width) + '-+')

#Função que executa a interface e coleta o caminho dos arquivos;
def criar_interface():
    caixa("Olá! Digite o caminho para o arquivo alvo no qual as funções serão executadas (incluindo a extensão). Caso o arquivo esteja na pasta de execução apenas o nome do arquivo é suficiente mais extensão, caso contrário é ncessário colocar o caminho completo para o arquivo:", 100)
    arquivo_texto = arquivos.caminho_arquivo()

    caixa("Deseja saber quais funções estão disponíveis para execução? (1) Sim (2) Não", 100)
    resposta = int(input())

    if resposta == 1:
        print( "\n")
        caixa("Temos as seguintes funções disponíveis: ", 100)    
        print(" -Agrupar", "\n","-Buscar <Texto>", "\n", "-Contar <Texto>", "\n", "-Maior", "\n", "-Preguiça", "\n", "-Substituir <Texto Antigo> <Texto Novo>", "\n")
    else:
        print("Ok!")
    time.sleep(1)

    caixa("Digite agora o nome do arquivo de onde serão retiradas as funções para execução (incluindo a extensão). Caso o arquivo esteja na pasta de execução apenas o nome do arquivo é suficiente mais extensão, caso contrário é ncessário colocar o caminho completo para o arquivo:: ", 100)
    arquivo_comandos = arquivos.caminho_arquivo()

    print("\n")

    texto = "Processando..."
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.3)

    print("\n")
    time.sleep(1)
    
    return arquivo_texto, arquivo_comandos