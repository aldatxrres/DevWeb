soma = 0

for num in range(1, 101):
    if num % 2 != 0:
        soma += num

    print(f"A soma dos números ímpares de 1 a 100 é {soma}")