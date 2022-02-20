'''
1. Cálculo de média escolar
Faça um programa que solicite ao usuário o nome do aluno e quatro notas (em ponto
flutuante, float), calcule a média das notas e faça a validação da média conforme regra a
seguir: Se a média for menor que 5, o aluno está reprovado, se for maior ou igual a 5 ele
está de recuperação e se for maior ou igual a 7, ele está aprovado.
Ao final, imprima desta forma: “O aluno nome está resultado. Sua média foi media”, onde
nome é a variável que vai armazenar o nome digitado pelo usuário e resultado é a variável
que vai armazenar “aprovado”, “reprovado” ou “recuperação” e média é a variável que
vai armazenar a média calculada.
'''

nomeAluno = input("Insira o nome do Aluno: ")
nota1 = input("Insira a primeira nota do aluno: ")
nota2 = input("Insira a segunda nota do aluno: ")
nota3 = input("Insira a terceira nota do aluno: ")
nota4 = input("Insira a quarta nota do aluno: ")

nomeAluno = str(nomeAluno)

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
media = (nota1+nota2+nota3+nota4)/4
resultado = ""

if media < 5:
    resultado = "Reprovado"

elif media >= 5:
    resultado = "Recuperação"

elif media >= 7:
    resultado = "Passou"







print(f'Nome do Aluno: {nomeAluno} \nNota 1: {nota1} \n Nota 2: {nota2} \n Nota 3: {nota3} \n Nota 4: {nota4}\n '
      f'O aluno {nomeAluno} está {resultado}. Sua média foi {media}')


