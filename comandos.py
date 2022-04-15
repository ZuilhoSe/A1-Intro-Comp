def Agrupar(arquivo):
    #Criação da variável que vai receber o texto final
    texto_editado = ""

    #Laço que itera sobre as linhas para edição
    for i in range(len(arquivo)):
        arquivo[i] = arquivo[i].replace("\n", "")
        linha_arquivo_editada = arquivo[i].replace(" ", "")
        texto_editado = texto_editado + linha_arquivo_editada

    #Resultados da função
    print(texto_editado)
    return texto_editado

def Maior(arquivo):
    print("Estou vendo o maior")
    print(arquivo[0])

def Preguiça(arquivo):
    texto_editado = []
    for i in range(len(arquivo)):
        arquivo[i] = arquivo[i].replace("\n", "")
        palavras_da_linha = arquivo[i].split(" ")
        palavras_menores = []
        for palavra in palavras_da_linha:
            if len(palavra) < 5:
                palavras_menores.append(palavra)
        linha_editada = ""
        for palavra_menor in palavras_menores:
            linha_editada = linha_editada + " " + palavra_menor
        texto_editado.append(linha_editada)
    print(arquivo)
    print(texto_editado)

def Contar(arquivo, texto):
    print("Estou contando", texto)
    print(arquivo[0])

def Buscar(arquivo, texto):
    print("Estou buscando", texto)
    print(arquivo[0])

def Substituir(arquivo, texto_antigo, texto_novo):
    print("Estou substituindo", texto_antigo, "por", texto_novo)
    print(arquivo[0])