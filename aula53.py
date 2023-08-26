'''
enumerate - enumera iteráveis (indices)
'''
lista = ['Maria','Helena','Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))

print(f'O que tem na lista enumerada {lista_enumerada}')

for indice, nome in lista_enumerada:
    print(indice, nome)

print(f'O que tem na lista enumerada {lista_enumerada}')