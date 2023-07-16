'''
Faça um programa que peça o primeiro do usuario. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
'''
nome_usuario = input("Digite seu nome: ")
if len(nome_usuario) > 1 and len(nome_usuario) <=4:
    print(f'Seu nome {nome_usuario} é curto')
elif len(nome_usuario) >= 5 and len(nome_usuario) <=6:
    print(f'Seu nome {nome_usuario} é normal')
else :
    print('Seu nome é bitelo')
    