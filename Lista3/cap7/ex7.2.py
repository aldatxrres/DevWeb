with open('arquivoTeste.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

print(f'O arquivo possui {len(linhas)} linhas.')