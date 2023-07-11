'''
Fatiamento de strings
012345678
Olá mundo

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
'''
variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[:5])
print(variavel[1:5])
#geralmente o ultimo indice é desconsiderado
print(len(variavel))
print(variavel[0:len(variavel):4])
print(variavel[::-1])