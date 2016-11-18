## this is going to call pokeapi to get information

import requests as r
import json

base_url = 'http://pokeapi.co/api/v2/'
def get_pokemon_data(pokenumber):
    request_url = base_url + 'pokemon/%s' % pokenumber
    pokedata = r.get(request_url)
    return pokedata.json()

## this creates a file 'bulbasaur.txt' and puts the
## results of get_pokemon_data(1) in that file

with open('bulbasaur.txt', 'w') as outfile:
    json.dump(get_pokemon_data(1), outfile)
