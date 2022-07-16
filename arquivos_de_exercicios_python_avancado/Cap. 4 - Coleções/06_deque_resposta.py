# Deques são filas duplamente terminadas
import collections
import string


def main():
    # Inicialize um deque com letras minúsculas
    letrinhas = collections.deque(string.ascii_lowercase) #passando todas letras em minusculo

    # Deques suportam o método len(), mostre o tamanho da deque
    print(f"Item count: {str(len(letrinhas))}")
    print('-'*30)
    # Itere sobre a deque criada
    for letra in letrinhas:
        print(letra.upper(), end=",")

    print('')

    # Manipule os itens em qualquer um dos terminais
    letrinhas.pop()
    letrinhas.popleft()
    letrinhas.append(2)
    letrinhas.appendleft(1)
    print(letrinhas)
    print("-"*300)
    # Rotacione a deque
    print(letrinhas)
    letrinhas.rotate(10)
    print(letrinhas) #letra vai andando para frente


if __name__ == "__main__":
    main()
