#   Exercício Python 020 - Sorteando uma ordem na lista
#   O mesmo professor do desafio 019 quer sortear a ordem de
#   apresentação de trabalhos dos alunos. Faça um programa que
#   leia o nome dos quatro alunos e mostre a ordem sorteada.



import random

aluno = []


while len(aluno) < 4:
    nomes = str(input("Digite o nome dos alunos:"))
    aluno.append(nomes)


random.shuffle(aluno)

print(f'Ordem de Apresentação \n {aluno}')