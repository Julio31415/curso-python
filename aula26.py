'''
Formatação básica de strings
.<número de digitos>f
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: 0 >- 100, .1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: ^10}')
print(f'{100.4873648123746:+,.1f}')