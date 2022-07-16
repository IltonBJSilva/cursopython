# Usando set comprehensions



def main():
    # Definindo uma lista de temperaturas
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # Crie um set com as temperaturas em Fahrenheit
    # Dica: Fórmula pra converter para Fahrenheit -> (t * 9/5) + 32
    ftemps_lista = [(t * 9/5) + 32 for t in ctemps] #lista
    ftemps_set = {(t * 9/5) + 32 for t in ctemps} #sets
    print(f"Lista: {ftemps_lista}")#repete numeros
    print(f"Sets: {ftemps_set}")#Não repete numeros

    # Crie um set a partir de uma string
    frase = "O primeiro podcast Brasileiro sobre ciência de dados"
    letras = {c.upper() for c in frase if not c.isspace()} #Retorna todas as letras e muda a ordem
    print(letras)


if __name__ == "__main__":
    main()
