palavra = input("Escreva uma palavra: ")

palavra = str(palavra)

a = 0
e = 0
i = 0
o = 0
u = 0

vogais = ["a", "e", "i", "o", "u"]
#conta as vogais respectivas
contar_vogais = [0, 0, 0, 0, 0]

#vai percorrer cada letra da palavra do usuario
for letra in palavra:
    #transforma Maisculo em minisculo
    if letra.lower() in vogais:
        contador = 0
        #contador para percorrer a palavra digitada sendo menor que a quantidade de vogais por que começa no 0 ate 4
        while contador < 5:
            #ignora Maiusculo e transforma em minusculo
            if letra.lower() == vogais[contador]:
                #Variavel que sera armazenada o valor a cada passada do laço
                contar_vogais[contador]+=1
            #contador que ira aumentar a cada passada
            contador+=1




print(f"Qtd. de 'a': {contar_vogais[0]}\n"
      f"Qtd. de 'e': {contar_vogais[1]}\n"
      f"Qtd. de 'i': {contar_vogais[2]}\n"
      f"Qtd. de 'o': {contar_vogais[3]}\n"
      f"Qtd. de 'u': {contar_vogais[4]}\n")


