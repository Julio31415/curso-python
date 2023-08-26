'''
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
'''
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3,3))

numero_4 = decimal.Decimal(0.5)
numero_5 = decimal.Decimal(0.8)
numero_6 = numero_5 + numero_4
print(numero_6)