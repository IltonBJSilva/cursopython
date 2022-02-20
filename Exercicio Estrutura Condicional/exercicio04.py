usuario = input("Digite o seu usuario: ")
senha = input("Digite sua senha: ")


if usuario == "adm":
    if senha == "senha":
        print("Acesso Autorizado")
else:
    print("Senha ou Usuario incorreto")
