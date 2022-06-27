locadora = []

#Função para criar novo filme
def create():
    while True:
        titulo = str(input("Digite o nome do filme: "))
        ano = str(input("Digite o ano do filme: "))
        diretor = str(input("Digite o diretor do filme: "))
        sair = int(input("Digite 0 para sair: "))
        listafilmes = {"titulo": titulo, "ano": ano, "diretor": diretor}
        locadora.append(listafilmes)
        if sair == 0:
            break

#Função para retornar todos
def read():
    print(f"Todos: {locadora}")

#Função para editar
def update():
    print("")
    editar = int(input("Qual filme deseja alterar as informações?"))
    my_dict = {**locadora, 'Pooja': 12}
    print(my_dict)



#Função para apagar
def delete():
    print("Qual Filme deseja apagar?")
    apagar = int(input("Digite: "))
    del(locadora[apagar])
    print(f'Nova lista{locadora}')



create()
read()
delete()












