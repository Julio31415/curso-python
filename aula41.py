'''While/else'''
string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    if letra == ' ':
        break
    print(letra)
    i += 1
else:
    print('não encontri um espaço')
print('fora do while')
