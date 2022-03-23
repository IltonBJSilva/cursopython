#   Exercício Python 042 - Analisando Triângulos v2.0
#   Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#       - EQUILÁTERO: todos os lados iguais
#       - ISÓSCELES: dois lados iguais, um diferente
#       - ESCALENO: todos os lados diferentes
import math
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}

lado1 = int(input("Digite o lado 01: "))
lado2 = int(input("Digite o lado 02: "))
lado3 = int(input("Digite o lado 03: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print(f"{cor['verde']}Os segmentos acima podem formar triângulo")
    if lado1 == lado2 and lado1 == lado3:
        print("EQUILÁTERO")

    elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado1 != lado2 or lado3 == lado1 and lado3 != lado2:
        print("ISÓSCELES")

    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print("ESCALENO")

    else:
        print("Error")

else:
    print(f"{cor['vermelho']}Os segmentos acima não podem formar triângulo")



