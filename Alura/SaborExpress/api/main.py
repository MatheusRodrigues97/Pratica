from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')

def hello_world():
    '''
    Endpoint que exibe o world
    '''
    return {'Hello':'World'}

@app.get('/api/restaurantes/')

def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardapios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados_json = resposta.json()

        if restaurante is None:
            return{'Dados': dados_json}


        dados_restaurante = []

        for item in dados_json:
           nome_do_restaurante = item['Company']
           if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    'price':item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return{'Erro': f'{resposta.status_code} - {resposta.text}'}
