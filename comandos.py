def Agrupar(arquivo):
    #Criação da variável que vai receber o texto final;
    texto_editado = ""

    #Laço que itera sobre as linhas para edição;
    for i in range(len(arquivo)):
        arquivo[i] = arquivo[i].replace("\n", "")
        linha_arquivo_editada = arquivo[i].replace(" ", "")
        texto_editado = texto_editado + linha_arquivo_editada

    #Resultados da função;
    print(texto_editado)
    return texto_editado

def Maior(arquivo):
    #Variável que recebe a maior palavra;
    maior_palavra = ""

    #Laço que itera sobre as linhas para buscar a maior palavra;
    for linha in arquivo:
        palavras = linha.split(" ")
        for palavra in palavras:
            if len(palavra) > len( maior_palavra):      
                 maior_palavra = palavra

    #Resultados da função;            
    print (maior_palavra)
    return maior_palavra
    
def Preguiça(arquivo):
    #Criação da lista que receberá o arquivo editado;
    texto_editado = []

    #Itera sobre as linhas do arquivo para separar as palavras menores do que 5;
    for i in range(len(arquivo)):
        arquivo[i] = arquivo[i].replace("\n", "")
        palavras_da_linha = arquivo[i].split(" ")
        palavras_menores = []
        for palavra in palavras_da_linha:
            if len(palavra) < 5:
                palavras_menores.append(palavra)
        #Juntar as palavras em uma linha para acrescentar no arquivo editado;
        linha_editada = ""
        for palavra_menor in palavras_menores:
            linha_editada = linha_editada + " " + palavra_menor
        texto_editado.append(linha_editada)

    #Resultados da função;
    print(texto_editado)
    return texto_editado

def Contar(arquivo, texto):
    print("Estou contando", texto)
    return arquivo

def Buscar(arquivo,texto):
    lista_frase = []
    for frase in arquivo:
        if frase.split().count(texto) != 0 :
            lista_frase.append(frase)
        elif frase.split().count(texto+".") !=0:
            lista_frase.append(frase) 
        elif frase.split().count(frase+",") !=0: 
            lista_frase.append(frase)
        elif frase.split().count(frase+"-") !=0:
            lista_frase.append(frase)
        elif frase.split().count(frase+";") !=0:
            lista_frase.append(frase)
        elif frase.split().count(frase+":") !=0:
            lista_frase.append(frase)
        elif frase.split().count(frase+"!") !=0:
            lista_frase.append(frase)
        elif frase.split().count(frase+"?") !=0:
            lista_frase.append(frase)
        elif frase.split().count(frase+"@") !=0:
            lista_frase.append(frase)
        elif frase.split().count(frase+"<") !=0:
            lista_frase.append(frase)
        elif frase.split().count(frase+">") !=0:
            lista_frase.append(frase)
        elif frase.split().count(frase+"@") !=0:
            lista_frase.append(frase)
        elif frase.split().count(frase+"<") !=0:
            lista_frase.append(frase)


    print(lista_frase)
    return lista_frase

def Substituir(arquivo, texto_antigo, texto_novo):
    texto_editado = []
    for frase in arquivo:
        linha_editada = ""
        palavras = frase.split(" ")
        for palavra in palavras:
            if palavra == texto_antigo:
                palavra_editada = palavra.replace(f"{texto_antigo}",f"{texto_novo}")
            else:
                palavra_editada = palavra    
            linha_editada = linha_editada + " " + palavra_editada      
        texto_editado.append(linha_editada)
    print(texto_editado)
    return texto_editado