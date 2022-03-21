#   Exercício Python 030 - Par ou Ímpar?
#   Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

valor = int(input("Insira um valor: "))

if valor % 2 == 0:
    print(f"O Valor: {valor} e um numero Par")
else:
    print(f"O Valor: {valor} e um numero impar")
