import arquivos
import comandos
import re

lista_de_comandos = arquivos.ler_arquivo_comandos("comandos.txt")
lista_de_linhas = arquivos.ler_arquivo_texto("texto.txt")

print(lista_de_comandos)
arquivos.execucao_dos_comandos(lista_de_linhas, lista_de_comandos)

input()