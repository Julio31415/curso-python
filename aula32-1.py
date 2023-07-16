'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horario descrito, eciba a saudação apropriada. EX.: Bom dia 0-11, Boa tarde 12 - 17 e Boa noite 18 - 23
'''
hora_usuario = input('Que horas são agora? ')
if hora_usuario.isdigit():
    hora_usuario_int = int(hora_usuario)
    if hora_usuario_int >= 0 and hora_usuario_int <= 11 :
        print("Bom dia!")
    elif hora_usuario_int >= 12 and hora_usuario_int <= 17:
        print("Boa tarde")
    elif hora_usuario_int >= 18 and hora_usuario_int<= 23:
        print('Boa Noite')
else:
    print('Horario incorreto')
