#Abrir e fechar arquivo manualmente

#inves disso
arquivo  = open("vendas.txt",'r')
texto = arquivo.read()
print(texto)
arquivo.close()

#faça isso
with open("vendas.txt", "r") as arquivo:
    texto = arquivo.read()
    print(texto)


