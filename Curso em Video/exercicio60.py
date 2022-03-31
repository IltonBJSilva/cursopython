#   Exercício Python 060 - Cálculo do Fatorial
#   Faça um programa que leia um número qualquer e mostre o seu fatorial.
#   Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
import math
number1 = int(input("Insira um valor: "))
fat = math.factorial(number1)
while number1 > 1:
    if number1 == 1:
        print(f'{number1}', end=' ')
    else:
        print(number1, end=" X ")
        number1-=1
print(f'= {fat}')