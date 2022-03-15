#   Exercício Python 017 - Catetos e Hipotenusa
#   Faça um programa que leia o comprimento do cateto oposto
#   e do cateto adjacente de um triângulo retângulo.
#   Calcule e mostre o comprimento da hipotenusa.
import math

catetoadj = int(input("Informe o valor do cateto adjacente: "))
catetopos= int(input("Informe o valor do cateto oposto: "))

hipotenusa = math.hypot(catetoadj, catetopos)

print(f'{hipotenusa:.2f}')


