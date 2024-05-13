import math

angulo = float(input("Insira um ângulo entre 0 e 360 graus: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"Seno: {seno}")
print(f"Cosseno: {cosseno}")
print(f"Tangente: {tangente}")