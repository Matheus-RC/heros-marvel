import requests 
import hashlib
import time
from appHeros import models
import json

public_key = "ebf5378994f8cac3238450449ae0e8a8"
private_key = "d63ac3a97cffcb16563a4fbec66d3f2efc71a90a"
url_base= "http://gateway.marvel.com/v1/public/characters"


def generate_hash(ts, private_key, public_key):
    # Concatenando o timestamp, chave privada e chave pública
    data = f"{ts}{private_key}{public_key}"

    # Gerando o hash MD5
    hash_md5 = hashlib.md5(data.encode()).hexdigest()
    return hash_md5

def carregar_Charactere(id):
    timestamp = str(int(time.time()))
    hash_value = generate_hash(timestamp, private_key, public_key)
    limit = 100
    if(id == None):
        url = f"{url_base}?limit={limit}&ts={timestamp}&apikey={public_key}&hash={hash_value}"
    else:
        url = f"{url_base}/{id}?limit={limit}&ts={timestamp}&apikey={public_key}&hash={hash_value}"

    print(f"{url}")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['data']
            total = data['total']
            data_heros = data['results']
            print(total)
            for charactere_data in data_heros:
                print(charactere_data['name'])
                hero_save = models.Character(name=charactere_data['name'],id=charactere_data['id'],
                path = charactere_data['thumbnail']['path'], extension=charactere_data['thumbnail']['extension'])

    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
        return False

        


