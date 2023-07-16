'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
'''
print(1234)
print(456)
int('a')
'''
try:
    numero_str = input('Vou dobrar o número que vc digitar: ')
    numero_float = float(numero_str)
    print(numero_str.isdigit())
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
except:
    print('Isso não é um número')
    

