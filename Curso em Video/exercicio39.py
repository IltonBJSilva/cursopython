#   Exercício Python 039 - Alistamento Militar
#   Faça um programa que leia o ano de nascimento de um jovem
#   e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#   se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#   Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import calendar
from datetime import date, timedelta, datetime, time

#puxa a data atual
data_final = datetime.now()
data_inicial = int(input("Informe qual ano você nasceu: "))
#converter data para int
data_final = int(data_final.strftime('%Y'))
definitivo = data_final - data_inicial
idadealistar = 18

if definitivo < 18:
    print(f"Ainda e menor de idade, você tem {definitivo} e precisa ter {idadealistar} anos de idade"
          f"faltam {idadealistar-definitivo} de anos para se alistar ")
elif definitivo > 18:
    print(f"Passou {definitivo-idadealistar} anos")