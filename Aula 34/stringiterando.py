frase = 'o rato roeu a roupa do rei de roma e o rei' #Iterável

tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_do_usuario = input("Qual letra deseja coloca maiuscula: ")

input_do_usuario = str(input_do_usuario)


#Iteração <- Iterar
while contador < tamanho_frase:
    # print(f'{frase[contador]}|{contador}')
    letra = frase[contador]
    #pega a letra que o usuario digitou e a transforma em maisuculo
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()

    else:
        nova_string += letra
    contador +=1

print(f"{nova_string}")
