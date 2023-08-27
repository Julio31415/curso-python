'''
Valores padrão para parametros
Ao definir uma função, os parametro podem ter valores padrão. Caso o valor não seja enviado para o parametro, o valor padrão sera usado.
Refatorar: editar o seu código
'''
def soma(x,y,z=0):
    print(f'{x=} {y=} {z=}',x+y+z)
soma(1,2,3)
