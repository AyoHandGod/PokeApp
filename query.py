import requests
import json
from jsonread import search

""" Our base URL where we will be accessing data from"""
BASE_URL = 'http://pokeapi.co/api/v2/pokemon/'


""" The Pokemon our user is searching for"""
poke = input("Which Pokemon would you like to search?: ")
term = input("What data do you wish to checkout?: ")

poke = poke.lower()
term = term.lower()

""" Our query function that performs the search and adds the item to our files"""
def query_pokeapi(resource_url, pkfile):
    url = '{0}{1}'.format(BASE_URL, resource_url)
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        json.dump(data, pkfile)
        return json.loads(response.text)
    return None

try:
    search(poke, term)
except:    
    """ Creates a json file to hold the pokemons information """
    print("Grabbing data from API... ")
    pokefile = open('{0}.json'.format(poke), 'w')
    pokemon = query_pokeapi(poke, pokefile)
    print("Bingo!\n")
    print(pokemon[term])

