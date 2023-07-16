'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
Contagem de complexidade (ruim)
'''

velocidade = 61 # velocidade atual do carro
local_carro = 90 # local em que o carro esta na estrada

radar_1 = 60 # velocidade máxima do radar 1
local_1 = 100 # local onde o radar 1 está
radar_range = 1 # A distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > radar_1
carro_multado_radar_1 = local_carro >= (local_1 - radar_range)

if velocidade > radar_1:
    print('Velocidae carro passou do radar 1')

if local_carro >= (local_1-radar_range) and local_carro <= (local_1 + radar_range):
    print('Carro multado em radar1')