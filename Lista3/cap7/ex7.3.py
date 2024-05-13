with open('arquivoTeste.txt', 'r') as arquivoEntrada:
    linhas = arquivoEntrada.readlines()

linhasInvertidas = [linha[::-1] for linha in linhas]

with open('arquivoSaida.txt', 'w') as arquivoSaida:
    arquivoSaida.writelines(linhasInvertidas)

print("Conteúdo invertido salvo no arquivo arquivoSaida.txt.")