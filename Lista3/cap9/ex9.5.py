def lerArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except PermissionError:
        print("Não é possível ler o arquivo")

nomeArquivo = input("Digite o nome do arquivo a ser lido: ")
lerArquivo(nomeArquivo)