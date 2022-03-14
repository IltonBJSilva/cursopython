#   Exercício Python 015 - Aluguel de Carros
#   Escreva um programa que pergunte a quantidade de Km percorridos
#   por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#   Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


km = float(input("Quantos KM percorreu?"))
dia = int(input("Por quanto dia usou?"))

valorFinal = (60*dia) + (km*0.15)

print(f"Valor total a pagar e de: {valorFinal:.2f}")





