'''
Listas em Python
Tipo List - Mutável
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamentos
Metodos uteis:
append, insert, pop, del, clear, extende + CRUD

CRUD -> CREATE/READ/UPDATE/DELETE

'''
lista = [10,20,30,40]
print(lista)
lista[2] = 300
print(lista)
del lista[1]
print(lista)
print(lista[1])
lista.append(50)
lista.append(90)
print(lista)
ultimo_valor = lista.pop()
print(ultimo_valor)
print(lista)
lista.append(1233333)
print(lista)
del lista[-1]
print(lista)
lista.insert(0,150)
print(lista)
lista.clear()
print(lista)

lista_b = ['z','y','x']

lista_concatenada = lista + lista_b
print(lista_concatenada)
lista.extend(lista_b)
print(lista)
