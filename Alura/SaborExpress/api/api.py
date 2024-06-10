import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

resposta = requests.get(url)

if resposta.status_code == 200:
    dados_json = resposta.json()
    print(dados_json)
else:
    print(f'O erro foi {resposta.status_code}')