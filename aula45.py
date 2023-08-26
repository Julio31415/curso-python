'''
Iterável -> str,range,etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entrgue seu iterador
'''
texto = iter('Luiz')
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

texto = 'Luiz' #iterável
iterador = iter(texto) #iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
