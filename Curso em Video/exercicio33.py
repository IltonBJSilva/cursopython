#   Exercício Python 033 - Maior e menor valores
#   Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))
numero3 = int(input("Digite o terceiro valor: "))

#verificar o maior numero
if numero1 > numero2 and numero2 > numero3:
    maior = numero1
    print(f'Maior numero: {maior}')

elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
    print(f'Maior numero: {maior}')

else:
    maior = numero3
    print(f'Maior numero: {maior}')



#Verificar o menor numero
if numero1 < numero2 and numero2 < numero3:
    menor = numero1
    print(f'Menor numero: {menor}')

elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
    print(f'Menor numero: {menor}')

else:
    menor = numero3
    print(f'Menor numero: {menor}')



