import arquivos
import interface

#Chamando a interface;
arquivos_leitura = interface.criar_interface()

#Atribuindo os arquivos a variaveis para serem utilizados;
lista_de_linhas = arquivos.ler_arquivo_texto(arquivos_leitura[0])
lista_de_comandos = arquivos.ler_arquivo_comandos(arquivos_leitura[1])

#Execução dos comandos;
arquivos.execucao_dos_comandos(lista_de_linhas, lista_de_comandos)

input()