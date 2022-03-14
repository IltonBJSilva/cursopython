#   Exercício Python 010 - Conversor d emoeda
'''
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos dolares ela pode comprar

Considere US$1,00 = R$3,27
'''

dolar = 3.27

dinheiro = float(input("Digite quanto valor você tem na carteira: "))

dolarComprado = dinheiro/dolar

print(f"Você pode comprar US${dolarComprado:.2f}")

