from functools import reduce
from importlib.metadata import unique_everseen
from operator import mul

import duplicates as duplicates

lista = set()

while True:
    palavras = str(input("Informe os números (número zero para sair): "))


    if palavras == '0':
        break

    lista.add(palavras)



print(lista)