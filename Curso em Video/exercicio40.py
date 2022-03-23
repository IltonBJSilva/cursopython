#   Exercício Python 040 - Aquele clássico da Média
#   Crie um programa que leia duas notas de um aluno e calcule sua média,
#   mostrando uma mensagem no final, de acordo com a média atingida:
#       - Média abaixo de 5.0: REPROVADO
#       - Média entre 5.0 e 6.9: RECUPERAÇÃO
#       - Média 7.0 ou superior: APROVADO


nota01 = float(input("Informe a primeira nota: "))
nota02 = float(input("Informe a primeira nota: "))

media = nota01+nota02/2

if media < 5:
    print("REPROVADO")

elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO")

elif media >= 7:
    print("APROVADO")





