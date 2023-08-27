'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o codigo é alcançavel.
O escopo loca é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a noems de escopos internos nos escopos externos
A palavra global daz uma variavel do escopo externo ser a mesma no escopo interno.
'''
x= 1

def escopo():
    global x
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x,y)
    print(x)
print(x)

print(x)
escopo()
print(x)
