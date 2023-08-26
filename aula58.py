'''
CPF 746.824.890 - 70
COLETE A SOMA DOS 9 PRIMEIROS DIGITOS DO CPF
MULTIPLICANDO CADA UM DOS VALORES POR UMA CONTAGEM REGRSSIVA COMEÇANDO DE 10

EX.: 74682489070
10 9 8 7 6 5 4 3 2
7  4 6 8 2 4 8 9 0
70 36 48 56 12 20 32 27 0

SOMAR TODOS OS RESULTADOS
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
MULTIPLICAR O RESULTADO ANTERIOR POR 10
301 * 10 = 3010
OBTER O RESTO DA DIVISÃO DA CONTA ANTERIOR POR 11
SE > 9 = RESULTADO = 0
SE <= 9 = MESMO RESULTADO

'''
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10
resultado = 0
for digito in nove_digitos:
    resultado += int(digito)*contador_regressivo
    contador_regressivo -= 1
digito = (resultado*10)%11
digito = digito if digito <= 9 else 0
print(digito)
