#
# Exemplo de processamento e parse de HTML
#
from html.parser import HTMLParser
import json
import urllib.request

def ManipulaJSON():
	#Acessar uma pagina
	endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
	webURL = urllib.request.urlopen(endereco)

	if webURL.getcode() == 200:
		dados = webURL.read()
		#Criar um dicionario json
		oJSON = json.loads(dados)
		#Navegar no obj dicionario
		contagem = oJSON["metadata"]["count"]
		print("Contagem: "+str(contagem))
		for local in oJSON["features"]:
			if local["properties"]["place"] == "18 km ESE of Naalehu, Hawaii":
				print("Encontrada registro especial*****")
			else:
				print(local["properties"]["place"])



ManipulaJSON()
