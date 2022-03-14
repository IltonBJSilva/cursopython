#   Exercício Python 006 - Dobro, Triplo, Raiz
'''
Crie um algoritmo que leia um numero e mostre   o seu dobro, triplo e raiz quadrada
'''
import math

entrada = int(input("Digite um valor: "))

dobro = entrada*2
tripo = entrada*3
raiz = math.sqrt(entrada)

print(f"Dobro: {dobro} \n Tripo: {tripo} \n Raiz Quadrada: {raiz:.2f}")
