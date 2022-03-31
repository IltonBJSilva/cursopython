#   Exercício Python 058 - Jogo da Adivinhação v2.0
#   Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#   Só que agora o jogador vai tentar adivinhar até acertar, #   mostrando no final
#   quantos palpites foram necessários para vencer.

from time import sleep
import random

#cores
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}

while True:
    numeroescolhido = int(input(f"{cor['azul']}Tente descobrir o valor entre 0 e 5 que eu pensei aqui: "))


    print(f"{cor['azul']}Vou pensar em um número entre 0 e 5. Tente adivinhar...{cor['limpa']}")


    r1 = random.randint(0, 5)

    print(f"{cor['lilas']}Processando...{cor['limpa']}")
    sleep(3)
    if numeroescolhido == r1:
        print(f"{cor['verde']}Você Ganhou: {r1}")
        break

    else:
        print(f"{cor['vermelho']}Você perdeu: {r1}")




