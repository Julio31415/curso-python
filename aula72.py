#EXERCICIOS -> SISTEMA DE PERGUNTAS E RESPOSTAS

perguntas = [
    {'pergunta': 'Quanto é 2 + 2?',
     'opcoes': ['3','4','5','8'],
     'resposta': "4"},
    {'pergunta': 'Quanto é 5*5?',
     'opcoes': ['25','40','65','48'],
     'resposta': "25"},
    {'pergunta': 'Quanto é 10/2?',
     'opcoes': ['15','5','25','19'],
     'resposta': "5"}
]
contador = 0
contador_opcoes = 0
contador_acertos = 0
print("SISTEMA DE PERGUNTAS E RESPOSTAS:")
while contador<len(perguntas):
    print(perguntas[contador].get('pergunta'))
    while contador_opcoes<len(perguntas[contador].get('opcoes')):
        resposta = perguntas[contador].get('opcoes')[contador_opcoes]
        indice = contador_opcoes + 1
        print(f'{indice} - {resposta}')
        print(" ")
        contador_opcoes = contador_opcoes + 1
    retorno = str(input("Qual o valor da opção correta?"))
    if retorno == perguntas[contador].get('resposta'):
        print("Parabéns, seu animal, você acertou")
        contador_acertos = contador_acertos + 1
    else:
        print("Errou!")
    contador = contador + 1
    contador_opcoes = 0
print(f'Você acertou {contador_acertos}/3. Parabens')

