"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variavel.
"""

def mult(*args):
    total = 1;
    for n in args:
        total = total*n
    return total

total = mult(1,2,3,4,5)
print(total)

'''
Crie uma função que fala se um numero é par ou impar.
Retorne se o numero é par ou impar
'''

def impar_par(n):
    if n%2 == 0:
        return "Par"
    elif n%2 != 0:
        return "Impar"
    else:
        return("Não foi informado um numero")

impar_par = impar_par("a")
print(impar_par)
