#   Exercício Python 035 - Analisando Triângulo v1.0
#   Desenvolva um programa que leia o comprimento de três retas
#   e diga ao usuário se elas podem ou não formar um triângulo.
#cores
from math import sqrt

cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}

print(f"{cor['lilas']}-=" * 12)
print("Analisador de Triângulos")
print(f"{cor['lilas']}-=" * 12)

r1 = float(input(f"{cor['azul']}Primeiro segmento: "))
r2 = float(input(f"{cor['amarelo']}Segundo segmento: "))
r3 = float(input(f"{cor['limpa']}Teceiro segmento: "))

#triangulo equilatero, nenhum de seus lados e maior, todos são o mesmo tamanho
'''
Cada comprimento precisa ser menor que a soma dos outros dois
'''
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"{cor['verde']}Os segmentos acima podem formar triângulo")
else:
    print(f"{cor['vermelho']}Os segmentos acima não podem formar triângulo")








