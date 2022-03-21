#   Exercício Python 031 - Custo da Viagem
#   Desenvolva um programa que pergunte a distância de uma viagem em Km.
#   Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
#   200Km e R$0,45 parta viagens mais longas.
#cores
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}

distancia = int(input(f"{cor['lilas']}Digite a distancia em KM: "))



if distancia <= 200:
    passagem = distancia*0.50
    print(f"{cor['azul']}Preço da passagem R$:{passagem:.2f}")

elif distancia > 200:
    passagem = distancia*0.45
    print(f"{cor['vermelho']}Preço da passagem {passagem:.2f}")


