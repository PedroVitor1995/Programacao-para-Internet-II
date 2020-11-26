import requests
import json

def get(url):
    response = requests.get(url)
    return response

def post(url):
    response = requests.post(url)
    return response

###########################################################################################################

#           IP-API - https://ip-api.com/

#   É uma API de consulta a localização de um IP

#   O caminho base da API é
#   http://ip-api.com/json/{query}
#       {query}pode ser um único endereço IPv4 / IPv6 ou um nome de domínio. Se você não fornecer uma
#       consulta, o endereço IP atual será usado.
#   Parâmetros de consulta (como campos personalizados e retorno de chamada JSONP) são anexados como 
#   parâmetros de solicitação GET, por exemplo:
#       http://ip-api.com/json/?fields=61439

def IP():
    url = "http://ip-api.com/json/19.48.0.1"
    response = post(url)
    print(response.status_code)

    location = json.loads(response.content)
    
    print("----------------------------------")
    for l in location:
        print("{} - {}" .format(l,location[l]))

    print("----------------------------------")
    print("Cidade - {}" .format(location["city"]))
    print("Região - {}".format(location["regionName"]))
    print("País - {}".format(location["country"]))

###########################################################################################################

#          Makeup API - https://makeup-api.herokuapp.com/

#   É uma API de consulta produtos e filtre-os por marca, preço, categoria de produto, etiquetas e muito
#   mais.

#   O endpoint da versão atual da API é:
#       http://makeup-api.herokuapp.com/api/v1/products.json
#   Para pesquisar a marca maybelline, anexe brand = maybelline. Por exemplo:
#       http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline

def Makeup():
    url = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline"
    response = get(url)
    print(response.status_code)

    products = json.loads(response.content)

    for p in products:
        print("Marca - {} | Produto - {}" .format(p["brand"], p["name"]))

###########################################################################################################

#           Data API - https://developer.dailymotion.com/api/

#   É uma API que permite acessar dados sobre vídeos, usuários, comentários, etc

#   Cada objeto na API de dados do Dailymotion possui um identificador exclusivo (dentro de sua
#   classe de objeto). Você pode acessar os campos de cada objeto, solicitando /<OBJECT_CLASS>/<OBJECT_ID>,
#   onde <OBJECT_CLASS>pode ser video, user, playlist, etc.

def Data():
    url = "https://api.dailymotion.com/user/x1fz4ii/videos"
    response = get(url)
    print(response.status_code)

    pages = json.loads(response.content)

    for video in pages["list"]:
        print("Título - {} | Canal - {}" .format(video["title"], video["channel"]))        

def main():
    #   IP-API
    IP()

    #   Makeup API
    #Makeup()

    #   Data API
    #Data()

if __name__ == '__main__':
	main()