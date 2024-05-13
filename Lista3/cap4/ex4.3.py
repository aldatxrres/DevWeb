import math

angulo = float(input("Insira o ângulo em graus: "))
anguloRadianos = math.radians(angulo)

seno = math.sin(anguloRadianos)
cosseno = math.cos(anguloRadianos)
tangente = math.tan(anguloRadianos)

print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)