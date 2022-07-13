# 
# Arquivo com exemplos para manipulação de dados na Internet
#

import urllib.request

def ConectaInternet():
	#Vai armazenar o conteudo que vai retornar
	objUrl = urllib.request.urlopen('https://www.google.com/')

	if objUrl.getcode() == 200:
		dados = objUrl.read
		print(dados)


ConectaInternet()
		

