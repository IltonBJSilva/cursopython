#   Exercício Python 036 - Aprovando Empréstimo
#   Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#   Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#   A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}

print("-=" * 12)
print(f"{cor['azul']}Aprovando Empréstimo")
print("-=" * 12)

casavalor = float(input("Qual o valor da casa? R$"))
salariocomprador = float(input("Qual e o seu salario? R$"))
anospagar = int(input("em quantos anos pretende pagar: "))

prestacao = casavalor / (anospagar * 12)

porcentagem = (salariocomprador*30/100)


if prestacao < porcentagem:
       #print(f"Imprestimo aceito e a prestação vai ser no valor de: R${prestacao:.2f}")
       print(f"Empréstimo aceito. A prestação será de R${prestacao:.2f}. Para pagamento em {anospagar*12} meses.")

else:
       print("Infelizmente, o empréstimo foi negado pois a prestação é superior a 30% de sua renda mensal.")



