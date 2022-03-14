#   Exercício Python 009 - Tabuada
'''
Escreva um programa que receba um valor e mostre sua tabuada
'''


tabuada = input("Qual tabuada deseja saber?\n Digite: ")
tabuada = int(tabuada)

for n in range (1,11):
    resposta = n*tabuada
    print(f" {tabuada} x {n} = {resposta}")

