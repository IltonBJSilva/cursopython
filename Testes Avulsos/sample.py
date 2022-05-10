# Python3 program
# the use of sample() function .

# import random
from random import sample

# Prints list of random items of given length
list1 = [1, 2, 3, 4, 5]

print(f'Antes: {sample(list1, len(list1))}')

while True:
    valoradicionar = int(input("Digite um valor que deseja adicionar: "))
    list1.append(valoradicionar)
    posicao = list1.index(3)
    print(f'''Valores total: {sample(list1, len(list1))}
Valor adicionado: {valoradicionar}
Valor em ordem: {sorted(list1)}
Primeiro valor 3 na posição {posicao}
    ''')

    opcao = str(input("Deseja parar? S OU N: ")).lower()
    if opcao == 's':
        break