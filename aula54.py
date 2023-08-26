'''
Faça uma lisya de compras com listas
O usuario deve ter a possibilidade de inserir, apagar e lisyar valores de sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista
'''

import os
lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar')
    if opcao == 'i':
        os.system('cls')
        valor = input('Item : ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolah o indice para apagar : ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número inteiro')
        except IndexError:
            print('indice não exite na lista')
        except Exception:
            print('ERRO DESCONHECIDO')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
            print(i,valor)


