import re

def verificar_cpf(cpf):
    expressao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    
    if re.match(expressao, cpf):
        print("CPF válido")
    else:
        print("CPF inválido")

cpf = input("Digite seu CPF: ")
verificar_cpf(cpf)