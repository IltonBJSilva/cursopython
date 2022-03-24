#   Exercício Python 054 - Grupo da Maioridade
#   Crie um programa que leia o ano de nascimento de sete pessoas.
#   No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date, timedelta, datetime, time

#puxa a data atual
data_final = datetime.now()
data_final = int(data_final.strftime('%Y'))

todosanos = []
maioridade = []
menoridade = []

for x in range(1,8):
    data_inicial = int(input("Informe qual ano você nasceu: "))
    # converter data para int
    definitivo = data_final - data_inicial

    todosanos.append(data_inicial)
    if definitivo >= 21:
        print("Maior de idade")
        maioridade.append(definitivo)
    else:
        print("Menor de idade")
        menoridade.append(definitivo)
    x+=1

print(f"""
Os maiores de idade tem {maioridade} anos.
menor idade {menoridade} anos.
Os anos de nascimento são: {todosanos}
""")