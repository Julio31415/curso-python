'''
DICIONÁRIOS EM PYTHON (tipo dict)
Dicionarios são estruturas de dados do tipo par de 'chave' e 'valor'
Chaves podem ser consideradas como o 'índice' que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple e etc
O valor pode ser qualquer tipo, incluindo outro dicionario
Usamos {} ou a classe sict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, List
'''
pessoa = {
    'nome':'Luiz Otávio',
    'sobrenome':'Miranda',
    'idade':18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal', 'numero':123},
        {'rua': 'tal','numero':321}
        ]
}
print(pessoa['nome'])
print(pessoa, type(pessoa))

for chave in pessoa:
    print(chave, pessoa[chave])