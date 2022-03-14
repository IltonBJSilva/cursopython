#   Exercício Python 011 - Tinta
'''
Faça um programa que leia a largura e a altura de um parede
em metros, calcule a sua area e a quantidade de tinta necessaria
para pinta-la, sabendo que cada litro de tinta, pinta
uma area de 2m**2.
'''

largura = float(input("Lembre-se, sera em metros\nInsira a largura: "))
altura = float(input("Insira a altura: "))

area = largura*altura

tinta = area/2

print(f"Sua parde tem a dimensão de {largura}x{altura} e a sua área é de {area}m²")
print(f"Para pintar essa parede, você precisará de {tinta}L de tinta")