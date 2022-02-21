import re

while True:
    quantidadeNumero = input("Escolha a quantidade de numero de 1 a 9: ")
    numeroFinal = 0

    sair = str(input("\n Deseja sair?\n Sim (S) ou Não (N)\n Qual: "))

    if sair == 'S' or sair == 's':
        print("Combinado")
        break
    elif sair == 'N' or sair == 'n':

        if not quantidadeNumero.isnumeric():
            print('Você precisa digitar um numero.')
            continue

        #Validação para saber se digitou um numero
        else:
            quantidadeNumero = int(quantidadeNumero)
            #validação de valor digitado
            if quantidadeNumero > 9 or quantidadeNumero < 1:
                print("Quntidade de numero invalida")

            else:
                contador = 1
                while contador <= quantidadeNumero:
                    if contador == 1:
                        posicao = 'Primeiro'
                    elif contador == 2:
                        posicao = 'Segundo'
                    elif contador == 3:
                        posicao = 'Terceiro'
                    elif contador == 4:
                        posicao = 'Quarto'
                    elif contador == 5:
                        posicao = 'Quinto'
                    elif contador == 6:
                        posicao = 'Sexto'
                    elif contador == 7:
                        posicao = 'Setimo'
                    elif contador == 8:
                        posicao = 'Oitavo'
                    else:
                        posicao = 'Nono'
                    #Solicitar valores que serão multiplicados
                    numero = int(input(f"Informe o {posicao} número: "))
                    print(f"Você informou {numero}, o resultado sera {numero * contador}")
                    numeroFinal += numero*contador
                    contador+=1
                    print(f"O resultado final é: {numeroFinal}")

                print("Quantidade valida")