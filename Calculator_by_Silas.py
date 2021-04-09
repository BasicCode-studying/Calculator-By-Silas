# -- coding: utf-8 --
"""
calculadora
autor: Silas
Função: Fazer Contar: soma. multiplicação, divisão, subtração e exponecial
"""
nome = "Sildosbarcos"
pi = 3.14
print("Bem vindo" + nome)
print("--Desafio--")


def str2py(*vals):
    result = ''
    for val in vals:
        if val.isnumeric():
            pass
        elif val.lower() == 'x':
            val = '*'
        elif val.lower() == '^':
            val = '**'
        result += val
    return eval(result)


operacao = 1
while operacao != 0:

    operacao = input("Digite a operação inteira: ")
    if str(operacao) in '0':
        break

    print(f"Resultado: {str2py(*operacao)}")

