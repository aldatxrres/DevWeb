import random

def adivinhe():
    numeroAleatorio = random.randint(1, 10)
    tentativas = 0

    while True:
        try:
            chute = int(input("Chute um número entre 1 e 10: "))
            tentativas += 1

            if chute == numeroAleatorio:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                break
            elif chute < numeroAleatorio:
                print("O número é maior")
            else:
                print("O número é menor")
        except ValueError:
            print("Por favor, insira apenas números")

adivinhe()