import math

numero = float(input("Insira um número: "))
raiz_quadrada = math.sqrt(numero)
valor_monetario = f"R${raiz_quadrada:.2f}"

print("Resultado: ", valor_monetario)