'''
split e join com list e str
split - divide um string
join - une uma string
'''

frase = 'Olha só que coisa interessante'
lista_palavras = frase.split()
print(lista_palavras)
frase_2 = 'Agora dividindo, na virgula'
lista_palavras_2 = frase_2.split(',')
print(lista_palavras_2)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())

frase_unida = '-'.join(lista_palavras)
print(frase_unida)
