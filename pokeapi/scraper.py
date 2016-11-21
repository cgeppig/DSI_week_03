## this is going to call pokeapi to get information

import requests as r
import json
import parser.return_pokemon_information
import time
import parser

base_url = 'http://pokeapi.co/api/v2/'
def get_pokemon_data(pokenumber):
    request_url = base_url + 'pokemon/%s' % pokenumber
    pokedata = r.get(request_url)
    return pokedata.json()

def get_gender_data(pokenumber):
    request_url = base_url + 'gender/%s' % pokenumber
    pokedata = r.get(request_url)
    return pokedata.json()

gender_data = get_gender_data(1)

for x in range(1,5):
    pokemon_data = get_pokemon_data(x)
    time.sleep(1)
    print parser.return_pokemon_information(pokemon_data, gender_data)
