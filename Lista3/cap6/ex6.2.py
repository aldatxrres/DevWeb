frase = input("Digite uma frase qualquer: ")

lista_palavras = [palavra.replace("a", "o") for palavra in frase.split() if "a" in palavra]
print(lista_palavras)