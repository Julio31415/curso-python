'''
CPF 746.824.890 - 70
COLETE A SOMA DOS 10 PRIMEIROS DIGITOS DO CPF
MULTIPLICANDO CADA UM DOS VALORES POR UMA CONTAGEM REGRSSIVA COMEÇANDO DE 11

EX.: 74682489070
11 10 9  8  7  6  5  4  3 2
7  4  6  8  2  4  8  9  0 7
77 40 54 64 14 24 40 36 0 14

SOMAR TODOS OS RESULTADOS
77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363
MULTIPLICAR O RESULTADO ANTERIOR POR 10
363 * 10 = 3630
OBTER O RESTO DA DIVISÃO DA CONTA ANTERIOR POR 11
SE > 9 = RESULTADO = 0
SE <= 9 = MESMO RESULTADO

'''
cpf = '74682489070'
nove_digitos = cpf[:10]
contador_regressivo = 11
resultado = 0
for digito in nove_digitos:
    resultado += int(digito)*contador_regressivo
    contador_regressivo -= 1
digito = (resultado*10)%11
digito = digito if digito <= 9 else 0
print(digito)
