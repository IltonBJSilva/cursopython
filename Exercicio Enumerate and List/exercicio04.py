from functools import reduce
from importlib.metadata import unique_everseen
from operator import mul

import duplicates as duplicates

lista = []
par_lista = []
impar_lista = []

while True:
    numeros = int(input("Informe os números (número zero para sair): "))
    if numeros == 0:
        break
    lista.append(numeros)
for posicao in lista:

    if posicao % 2 == 0:
        par_lista.append(posicao)

    else:
        impar_lista.append(posicao)

print("Numeros Pares: ",par_lista,"\n Numero impares: ", impar_lista)
