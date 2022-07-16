# Mostre o valor booleano de uma lista vazia
x = []
print(bool(x)) #false

# Mostre o valor booleano de um dicionario vazio
y = {}
print(bool(y)) #false

print("-"*30)
valor = int(input("Insira um valor: "))

x.append(valor)
print(bool(x)) #True
print(bool(y)) #false