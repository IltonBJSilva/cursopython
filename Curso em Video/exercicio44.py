#   Exercício Python 044 - Gerenciador de Pagamentos
#   Elabore um programa que calcule o valor a ser pago por um produto,
#   considerando o seu preço normal e condição de pagamento:
#       - à vista dinheiro/cheque: 10% de desconto
#       - à vista no cartão: 5% de desconto
#       - em até 2x no cartão: preço formal
#       - 3x ou mais no cartão: 20% de juros

produto = float(input("Insira o valor do produto: R$"))
print('''
1 - à vista dinheiro/cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço formal
4 - 3x ou mais no cartão: 20% de juros
''')
opcao = int(input("Insira o meio de pagamento: "))

if opcao == 1:
    print("Você escolheu a opcao à vista dinheiro/cheque: 10% de desconto")
    newvalue = produto-((produto*(10/100)))
    print(f"Novo valor sera de: R${newvalue:.2f}")

elif opcao == 2:
    print("Você escolheu a opcao à vista no cartão: 5% de desconto")
    newvalue = produto-((produto*(5/100)))
    print(f"Novo valor sera de: R${newvalue:.2f}")

elif opcao == 3:
    print("Você escolheu a opcao em até 2x no cartão: preço formal sem juros")
    newvalue = produto/2
    quantidade = int(input("Quantas parcelas? obs(max = 2) \n Escolha: "))

    if quantidade == 2:
        parcela = produto/ 2
        print(f"Novo valor sera de: 2X de R${newvalue:.2f} sem juros ou seja sera de R${produto}")
    elif quantidade == 1:
        print(f"Novo valor sera de R${produto}")
    else:
        print("Opção invalida para esse pagamento, caso deseje parcelar mais escolha a opção 4")


elif opcao == 4:
    print("Você escolheu a opcao 3x ou mais no cartão: 20% de juros")
    quantidade = int(input("Quantas parcelas? "))
    acrescimo = produto+((produto*(20/100)))
    parcela = (produto + (produto * 20) / 100) / quantidade
    print(parcela)
    print(f"Novo valor sera de: {acrescimo:.2f}"
          f"\ndividido em {quantidade}x vezes de {parcela:.2f}")

else:
    print("Opção invalida")





