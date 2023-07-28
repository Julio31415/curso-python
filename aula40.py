'''Calculadora com While'''
print("Calculadora com While")
valor_1 = 0
valor_2 = 0
operador = ''
resultado = 0
continuar = True
opção = 'sim'
while True:
    valor_1 = float(input("Digite um valor \n"))
    valor_2 = float(input("Digite outro valor \n"))
    print('Digite: "+" para adição \n "-" para subtração \n "x" para multiplicação \n "/" para divisão')
    operador = input("Digite a operação a ser realizada: \n")
    if operador == '+':
        resultado = valor_1 + valor_2
        print(f'O resultado da soma é {resultado}')
    elif operador == '-':
        resultado = valor_1 - valor_2
        print(f'O resultado da subtração é {resultado}')
    elif operador == 'x':
        resultado = valor_1 * valor_2
        print(f'O resultado da multiplicação é {resultado}')
    elif operador == '/':
        resultado = valor_1/valor_2
        print(f'O resultado da divisão é {resultado}')
    else:
        print("Operador incorreto")
    opção = input('Deseja continuar? Responda com "sim" ou "não"\n')
    if opção == 'não':
        print('Calculadora finalizada')
        break
