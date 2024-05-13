nomes = input("Digite uma lista de nomes separados por vírgula: ")

lista_nomes = nomes.split(",")
nomes_caixa_alta = list(map(str.upper, lista_nomes))
print(nomes_caixa_alta)