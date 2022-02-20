#Exercicio 02
horario = input("Digite o horario 0-23:")

if horario.isdigit():
    #cash
    horario = int(horario)

    if horario < 0 or horario >23:
        print("Por favor digite um horario valido entre 0 e 23")

    else:
        if horario<=11:
            print("Bom Dia")
        elif horario<=17:
            print("Boa Tarde")
        elif horario<=23:
            print("Boa Noite")

else:
    print("Por favor digite um horario entre 0 e 23")
