#   Exercício Python 038 - Comparando números
#   Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#       - O primeiro valor é maior
#       - O segundo valor é maior
#       - Não existe valor maior, os dois são iguais


num1 = int(input("Insira um valor: "))
num2 = int(input("Insira outro valor: "))

if num1 > num2:
    print("O primeiro valor é maior")
elif num1 < num2:
    print("O segundo valor é maior")
elif num1 == num2:
    print("Não existe valor maior, os dois são iguais")

