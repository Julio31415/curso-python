'''
METODOS ÚTEIS COM DICIONARIOS EM PYTHON

LEN -> QUANTAS CHAVES
KEYS -> ITERÁVEL COM AS CHAVES (pode ser convertido em lista/tupla)
VALUES -> ITERÁVEL COM OS VALORES
ITEMS -> RETORNA CHAVE E O VALOR 
SETDEFAULT -> ADICIONA VALOR A UMA CHAVE QUE NÃO EXISTE
COPY -> RETORNA UMA COPIA RASA (SHALLOW COPY)
GET -> OBTÉM UMA CHAVE 
POP -> APAGA UM ITEM COM A CHAVE ESPECIFICADA (DEL)
POPITEM -> APAGA O ULTIMO ITEM ADICIONADO
UPDATE -> ATUALIZA UM DICIONARIO COM OUTRO
'''

pessoa = {
    'nome':'Luiz Otávio',
    'sobrenome':'Miranda',
    #'idade':18,
    'altura': 1.8,
}

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa.setdefault('idade',0)
print(pessoa['idade'])

print(pessoa.get('nome'))
print(pessoa.pop('nome'))
print(pessoa.popitem())

pessoa.update({
    'nome': 'julio',
    'saude':'boa',

})

print(pessoa)