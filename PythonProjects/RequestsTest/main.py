import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'df74386baf3e391ccce2097eccaa06a0'
HEADER = {'content-typy' : 'application/json', 'trainer_token':TOKEN}
BODY_POKEMONS = {
    "name": "ZZZ",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}
BODY_NAME = {
    "pokemon_id": "26694",
    "name": "zaza",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
BODY_pokeball = {
    "pokemon_id": "26694"
}


#response =  requests.post(url=f'{URL}/pokemons', headers= HEADER, json =BODY_POKEMONS )
#print(response.text) 

#response_name = requests.put(url=f'{URL}/pokemons',headers=HEADER, json=BODY_NAME)
#print(response_name.text)

#response_pokeball = requests.post (url=f'{URL}/trainers/add_pokeball',headers=HEADER, json=BODY_pokeball)
#print(response_pokeball.json())




            
