numero = int(input("Digite um número: "))

print(f"Tabuada do {numero}:")
for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")