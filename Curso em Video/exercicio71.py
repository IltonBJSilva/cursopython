#   Exercício Python 071 - Simulador de Caixa Eletrônico
#   Crie um programa que simule o funcionamento de um caixa eletrônico.
#   No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#   e o programa vai informar quantas cédulas de cada valor serão entregues.
#       OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from time import sleep

print('='*30)
print("{:^30}".format("CAIXA ELETRÔNICO"))
print('='*30)

dinheiro = int(input("qual será o valor a ser sacado (número inteiro): R$"))
total = dinheiro

print('\n\nAnalisando a transação....')
print('-[ Verificando disponiblidade de cédulas ]-')
sleep(1)

#cedula do momento, cada iteração vai diminuir de acordo com meu dinheiro
cedula = 200
#total de cedulas a serem enviadas
total_de_cedulas = 0


while True:

    #gerador de notas pois compara as notas que faltam e se a cedula da maquina foi maior que meu dinheiro
    #o codigo continua para o else para transforma 100 em 50 ou 50 em 20
    if dinheiro >= cedula:
        dinheiro -= cedula
        total_de_cedulas += 1
    #caso não de mais
    else:
        #vai passar aqui uma vez
        if total_de_cedulas > 0:
            print(f"Total de {total_de_cedulas} cédulas de R${cedula}...[OK]")
        if cedula == 200:
            cedula = 100

        elif cedula == 100:
            cedula = 50


        elif cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 5

        elif cedula == 5:
            cedula = 2

        elif cedula == 2:
            cedula = 1

        #Quando chega aqui, reseta o total de cedulas para proxima iteração
        total_de_cedulas = 0
        if dinheiro == 0:
            print('=' * 40)
            print(f"Transação realizada com sucesso!\nSaque no valor total de => : R${total}")
            exit()
        elif dinheiro == 1:
            print("\nOPERAÇÃO CANCELADA!"
                  "\nAs cédulas disponíveis neste caixa não permitem concluir esta transação.\n"
                  "Por favor, refaça sua operação com outro valor!")
            exit()
