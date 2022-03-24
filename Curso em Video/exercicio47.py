#   Exercício Python 047 - Contagem de pares

#   Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


for x in range(0,51):
    if x % 2 == 0:
        print(f"{x} - Par")
    else:
        print()

