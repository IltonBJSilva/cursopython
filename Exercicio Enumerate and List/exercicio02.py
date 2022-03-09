from functools import reduce
from operator import mul
lista_palavra = []
while True:
    quantidade = str(input("Informe palavras (número zero para sair): "))
    if quantidade != '0':
        lista_palavra.append(quantidade)
    elif quantidade == '0':
        Qtd_palavra = str(input("Informe palavras que deseja contar(número zero para sair): "))
        break
    else:
        print("Nenhuma palavra digitada")
print(f"Qunatidade de vezes que --> {Qtd_palavra} <-- apareceu: ",lista_palavra.count(Qtd_palavra))
