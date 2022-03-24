#   Exercício Python 052 - Números primos
#   Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# primo = divisivel por 1 ou por ele mesmo

n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(2,n):
    #Contar quais numeros são multiplos do input
    #Resto de um numero primo e diferente de 0
    if (n % count == 0):
        print("Múltiplo de",count)
        #Contar a quantidade de multiplos
        mult += 1
#Calculo acima foi realizado para saber os numeros multiplos, oque e diferente disso e um primo
if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)




















