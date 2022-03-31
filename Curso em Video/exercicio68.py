#   Exercício Python 068 - Jogo do Par ou Ímpar
#   Faça um programa que jogue par ou ímpar com o computador.
#   O jogo só será interrompido quando o jogador perder,
#   mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

while True:
    parimpar = str(input("Digite Escolha Par ou Impar: ")).lower()
    computador = random.randint(1, 9)

    if parimpar == 'par':
        valor = int(input("Digite o valor Par: "))
        soma = valor+computador
        if soma % 2 == 0:
            print(f"Você ganhou, Total = {soma}, computador = {computador}, você = {valor}")
        else:
            print(f"Você perdeu, Total = {soma}, computador = {computador}, você = {valor}")


    elif parimpar == 'impar':
        valor = int(input("Digite o valor Impar: "))
        soma = valor+computador
        if soma % 2 == 0:
            print(f"Você perdeu, Total = {soma}, computador = {computador}, você = {valor}")
        else:
            print(f"Você ganhou, Total = {soma}, computador = {computador}, você = {valor}")



