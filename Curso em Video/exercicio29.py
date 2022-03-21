#   Exercício Python 029 - Radar eletrônico
#   Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#   mostre uma mensagem dizendo que ele foi multado.
#   A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("(obs: em km)Velocidade do carro: "))
multa = (velocidade-80) * 7

if velocidade > 80:
    print(f"Você foi multado valor da multa: R${multa:.2f}")
else:
    print("Vá com Deus")
