import requests # pegar o link do site
import sys # sistema 
import json #Biblioteca para trabalhar com arquivos json

if len (sys.argv) != 2:
    sys.exit("Erro de pesquisa, poucos dados")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])

obj = response.json()

for result in obj["results"]:
    print(result["trackName"])