nome = "Ilton"
idade = 21
altura = 1.75
peso = 80.2
e_maior = idade > 18
data_1 = True #bool
data_atual = 2022
nascimento = data_atual-idade
imc = peso / altura**2


print("Nome:",nome,"\nIdade:",idade,"\nAltura:",altura,"\nPeso:",peso,"\nÉ maior:",e_maior,"\nSeu IMC é: %.4f"%imc)

print(f'\n{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa  {peso} e seu imc é  {imc:.2f}.')
print(f'{nome} nasceu  {nascimento}.')
