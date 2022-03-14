#   Exercício Python 012 - Calculando Descontos
#   Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

desconto = 5
preco = float(input("Digite o preço do produto para saber o desconto: "))


precoFinal = preco-(preco*(desconto/100))


print(f"Preço final foi de: {precoFinal:.2f}")