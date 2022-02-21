while True:
    num = input("Digite um numero: ")
    sair = input("Deseja sair? \n Sim(S) ou Não(N)\n Digite: ")

    num = int(num)
    sair = str(sair)

    if sair == 'S' or sair =='s':
        print("Combinado")
        break
    elif sair == 'N' or sair =='n':
        if num % 2 == 0:
            print(f"{num} é um número par.")
        else:
            print(f"{num} é um número ímpar.")





