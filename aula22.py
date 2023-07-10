#Or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
#Se qualquer valor for considerado verdadeiro, a ecpressão interia será avaliada naquele valor.

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')