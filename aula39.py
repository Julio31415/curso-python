'''
Iterando strings com while
'''

nome = 'Luiz Otavio'

nome_modificado = ''

cont = 0
cont2 = 2*len(nome)

while cont < len(nome):
    if cont2%2 != 0:
        nome_modificado += nome[cont]
        cont += 1
        cont2-= 1
    else:
        nome_modificado += '*'
        cont2-= 1
print(nome_modificado)
