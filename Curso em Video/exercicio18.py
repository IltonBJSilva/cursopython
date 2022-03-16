#   Exercício Python 018 - Seno, Cosseno e Tangente
#   Faça um programa que leia um ângulo qualquer e mostre na tela
#   o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = int(input("\bDigite um ângulo para saber o Seno\nCosseno\n Tangente do ângulo.\n Digite:"))

#Em Radiando
seno = math.sin(angulo)
tangente = math.tan(angulo)
cosseno = math.cos(angulo)


print(f"\nSeno: {seno:.2f} \n Tangente: {tangente:.2f} \n Cosseno: {cosseno:.2f}\n")