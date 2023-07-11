'''
EXERCICIO

Peça oa usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se nome e idade forem digitado:
    Exiba:
        Seu nome é{nome}
        Seu nome invertido é{nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é{letra}
        A ultima letra do seu nome é{letra}
se nada dor digitado em nome ou idade:
    exiba 'Voce não digitou nada.'
'''
nome = input('Digite o seu nome')
idade = int(input('Digite a sua idade'))
if nome != '' and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome [::-1]}')
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[len(nome)-1]}')
else:
    print('Você não digitou nome e idade corretamente.')