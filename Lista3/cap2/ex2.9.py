num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3

if media >= 6:
    print("Aprovado")
    if media == 10:
        print("Parabéns")
else:
    print("Reprovado")