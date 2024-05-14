def calculadora():
    while True:
        try:
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
            operacao = input("Digite o símbolo da operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida")

            print("Resultado: ", resultado)
            break

        except ValueError as e:
            print("Erro:", e)
            print("Por favor, tente novamente.\n")

calculadora()