'''
Higher Order Functions
Funções de primeira classe
'''
def saudacao(msg):
    return msg
def executa(funcao,msg):
    return funcao(msg)

print(saudacao('Bom dia'))
saudacao_2 = saudacao
print(saudacao_2('bom dia'))
v = executa(saudacao_2,'Bom dia')
print(v)
