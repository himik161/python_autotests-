import requests 
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'df74386baf3e391ccce2097eccaa06a0'
HEADER = {'content-typy' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2224'

def test_status_code():
    response= requests.get(url=f'{URL}/trainers', params= {'trainer_id':TRAINER_ID})
    assert response.status_code ==200