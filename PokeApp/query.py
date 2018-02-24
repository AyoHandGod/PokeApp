import requests
import json
from jsonread import search

""" Our query function that performs the search and adds the item to our files"""
def query_pokeapi(resource_url, pkfile):
    """ Our base URL where we will be accessing data from"""
    base_url = 'http://pokeapi.co/api/v2/pokemon/'
    url = '{0}{1}'.format(base_url, resource_url)
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        json.dump(data, pkfile)
        return json.loads(response.text)
    return None


# create json to hold file
def fi_check():
    new_file = open('{0}.json'.format(poke), 'w')
    print("Couldn't create the file. :(")
    return new_file


""" The Pokemon our user is searching for"""
poke = input("Which Pokemon would you like to search?: ")
term = input("What data do you wish to checkout?: ")
poke = poke.lower()
term = term.lower()

while True:
    try:
        pokefile = open('{0}.json'.format(poke), 'r')
        search(poke, term)
        break

    except:
        print("Grabbing data from API... ")
        pokefile = open('{0}.json'.format(poke), 'w')
        pokemon = query_pokeapi(poke, pokefile)
        print("Bingo!\n")


