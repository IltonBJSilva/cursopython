#   Exercício Python 055 - Maior e menor da sequência
#   Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

bd = []
for x in range(1,6):
    peso = float(input(f"0{x} - Digite o peso: "))
    bd.append(peso)


print(f'''
Maior peso da lista: {max(bd)}
Maior peso da lista: {min(bd)}

''')
















