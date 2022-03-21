#   Exercício Python 028 - Jogo da Adivinhação v.1.0
#   Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#   e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#   O programa deverá escrever na tela se o usuário venceu ou perdeu.
from time import sleep
import random

#cores
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}

numeroescolhido = int(input(f"{cor['azul']}Tente descobrir o valor entre 0 e 5 que eu pensei aqui: "))


print(f"{cor['azul']}Vou pensar em um número entre 0 e 5. Tente adivinhar...{cor['limpa']}")


r1 = random.randint(0, 5)

print(f"{cor['lilas']}Processando...{cor['limpa']}")
sleep(3)
if numeroescolhido == r1:
    print(f"{cor['verde']}Você Ganhou: {r1}")

else:
    print(f"{cor['vermelho']}Você perdeu: {r1}")


