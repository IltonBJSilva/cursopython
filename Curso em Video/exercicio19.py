#   Exercício Python 019 - Sorteando um item na lista
#   Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#   Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno = []
sorteado = ''
posicao = 0

while len(aluno) < 4:
    nomes = str(input("Digite o nome dos alunos:"))
    aluno.append(nomes)


for i in aluno:
    posicao += 1
    print(f'{posicao} - {i}')

print(f'Aluno sorteado {random.choice(aluno)} ')
