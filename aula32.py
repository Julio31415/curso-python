'''
Faça um programa que peça oa usuario para digitar um numero inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''

numero_usuario = input('Digite um número inteiro: ')
if numero_usuario.isdigit():
    numero_usuario_inteiro = int(numero_usuario)
    if numero_usuario_inteiro%2 == 0:
        print(f'O numero digitado {numero_usuario_inteiro}é par')
    elif numero_usuario_inteiro%2 != 0:
        print(f'O numero digitado {numero_usuario_inteiro} é impar')
else:
    print('Você não digitou um número inteiro')
