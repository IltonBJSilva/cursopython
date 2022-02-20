#Exercicio 03
nome = input("Digite o seu primeiro nome:")
tamanho = len(nome)

if tamanho < 4:
    print("Seu nome e bem curto")
elif tamanho == 5 or tamanho == 6:
    print("Tamanho normal")
elif tamanho > 6:
    print("Big Name o teu em meu chapa")