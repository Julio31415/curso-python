#if / elif /else
entrada = input("Você quer 'sair' ou 'entrar'?")

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')