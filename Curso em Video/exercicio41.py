#   Exercício Python 041 - Classificando Atletas
#   A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#   e mostre sua categoria, de acordo com a idade:
#       - Até 9 anos: MIRIM
#       - Até 14 anos: INFANTIL
#       - Até 19 anos: JÚNIOR
#       - Até 25 anos: SÊNIOR
#       - Acima de 25 anos: MASTER


import calendar
from datetime import date, timedelta, datetime, time

#puxa a data atual
data_final = datetime.now()
data_inicial = int(input("Informe qual ano você nasceu: "))
#converter data para int
data_final = int(data_final.strftime('%Y'))
definitivo = data_final - data_inicial
idadealistar = 18

if definitivo <= 9:
    print("MIRIM")
elif definitivo <= 14:
    print("INFANTIL")

elif definitivo <= 19:
    print("JÚNIOR")

elif definitivo <= 25:
    print("SÊNIOR")

elif definitivo > 25:
    print("MASTER")








