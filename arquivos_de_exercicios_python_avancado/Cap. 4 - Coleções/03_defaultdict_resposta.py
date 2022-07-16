# Usando objetos defaultdict
from collections import defaultdict


def main():
    # Defina uma lista de itens você quer contar
    frutas = ['maçã', 'pêra', 'laranja', 'banana',
              'maçã', 'uva', 'banana', 'banana']

    # Use um dicionário para contar cada ele mento
    contador_frutas = defaultdict(int)
    #or
    contador_frutas = defaultdict(lambda: 100) #vai começar em 100


    # Conte os elementos da lista
    for fruta in frutas:
        contador_frutas[fruta] += 1

    # Faça o print do resultado
    for (c, v) in contador_frutas.items():
        print(c + ": " + str(v))


if __name__ == "__main__":
    main()
