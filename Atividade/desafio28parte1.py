#Exercicio 01
num1 = input("Digite um numero:")

if num1.isdigit():
    num1 = int(num1)

    if (num1%2) == 0:
        print(f"{num1} é Par")
    else:
        print(f"{num1} é impar")

else:
    print("Não é um numero inteiro")