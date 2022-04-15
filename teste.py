import arquivos
import comandos


lista_de_comandos = arquivos.ler_arquivo_comandos("comandos.txt")
lista_de_linhas = arquivos.ler_arquivo_texto("texto.txt")

palavra1 = ""
palavra2 = ""

""""Para utilizar basta descomentar a função que voce quer utilizar"""

#comandos.Agrupar(lista_de_linhas)

#comandos.Maior(lista_de_linhas)

#comandos.Preguiça(lista_de_linhas)

#comandos.Contar(lista_de_linhas, palavra1)

#comandos.Buscar(lista_de_linhas, palavra1)

#comandos.Substituir(lista_de_linhas, palavra1, palavra2)