comidas = ['Pizza','Pastel','Esfiha']
estacoes = ['Primavera', 'Verão', 'Outono','Inverno']


'''
#Você pode usar uma dessas opções abaixo
for posicao, comida in enumerate(comidas):
    print(f"#{posicao + 1} - {comida}")

for posicao, comida in enumerate(comidas, start=1):
    print(f"#{posicao} - {comida}")
'''

for posicao, estacao in enumerate(estacoes, start=1):
    print(f"#{posicao} - {estacao}")