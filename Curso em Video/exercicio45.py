#   Exercício Python 045 - GAME: Pedra Papel e Tesoura
#   Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
import random

computador = ['Tesoura','Papel','Pedra'][random.randint(0,2)]

desejo = 1

while desejo == 1:
    opcao = str(input("Faça sua escolha \n01-Pedra\n02-Papel\n03-Tesoura \nQual deseja: "))
    desejo = int(input("Deseja encerrar? \n Digite 0 para sim ou 1 para não \nEscolha: "))

    if computador == 'Tesoura' and opcao == 'Pedra':
        print(f"\nVocê ganhou, parabens\n")

    elif computador == 'Papel' and opcao == 'Pedra':
        print(f"\nVocê perdeu\n")

    elif computador == 'Papel' and opcao == 'Tesoura':
        print(f"\nVocê ganhou, parabens\n")

    elif computador == 'Pedra' and opcao == 'Tesoura':
        print(f"\nVocê perdeu\n")

    elif computador == 'Pedra' and opcao == 'Papel':
        print(f"\nVocê ganhou, parabens\n")

    elif computador == 'Tesoura' and opcao == 'Papel':
        print(f"\nVocê perdeu\n")

    elif computador == opcao:
        print(f"\nEmpate\n")

    else:
        print("Opção invalida, digite na mesma forma que aparece escrito, respeitando minusculo e maiusculo.")


