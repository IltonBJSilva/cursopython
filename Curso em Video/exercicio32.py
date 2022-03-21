#   Exercício Python 032 - Ano Bissexto
#   Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
#cores
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}


ano = int(input(f"{cor['lilas']}Digite o ano: "))

if calendar.isleap(ano):
    print(f"{cor['verde']}É bisexto")
else:
    print(f"{cor['vermelho']}Não e bisexto")
