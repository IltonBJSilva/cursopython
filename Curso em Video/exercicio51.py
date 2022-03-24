#   Exercício Python 051 - Progressão Aritmética
#   Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#   No final, mostre os 10 primeiros termos dessa progressão.

ptermo = int(input("Digite o primeiro termo da progressão PA: "))
razao = int(input("Digite a razão da progressão PA: "))

for x in range(1,11):
    an = ptermo+(x-1)*razao
    print(f' {an} ',end='->')
print("ACABOU!!")









