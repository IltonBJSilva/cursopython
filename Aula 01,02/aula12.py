import requests

def retorna_dados_cep(cep):
    #Fazer a requisição do site
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    dados_cep = response.json()

    #pegar o texto do site
    print(response.text)

    #Mostrar o code de erro ou acerto do site
    print(response.status_code)

    #String
    print(type(response.text))

    #Transforma em um dicionario
    print(response.json())

    #Dicionario
    print(type(response.json()))

    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])

    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://www.google.com/?&bih=772&biw=1511&hl=pt-BR')
    print(response)

    #API de buscar CEP
    # cep = int(input('Digite um CEP: '))
    # retorna_dados_cep(cep)

    #API do Pokemon
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])

