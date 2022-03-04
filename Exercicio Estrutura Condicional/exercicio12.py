tabuadaTreinar = input("Qual tabuada deseja Treinar?\n Digite: ")
tabuadaTreinar = int(tabuadaTreinar)
acertos = 0
erros = 0

while True:
    #vai gerar um valor de 1 a 10 em uma tabuada
    for n in range (1,11):
        #vai multiplicar o valor digitado antes na sequencia de 1 a 10
        respostaUser = int(input(f"{tabuadaTreinar} x {n} = "))
        #vai inserir a pontuação nos acerto
        if respostaUser == (n*tabuadaTreinar):
            print("Acertou")
            acertos +=1
        #vai inserir a pontuação nas derrotas
        else:
            print(f'Que pena você errou, o correto deveria ser: {n*tabuadaTreinar}')
            erros+=1

    print(f'Numero de acertos: {acertos} \n Numero de erros: {erros}')
        #print(tabuada, 'x', n, '=', resposta)
