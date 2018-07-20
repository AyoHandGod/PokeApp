"""
@Author: Dante Anthony
@Title: PokeApp
@Version: 1.1.0
"""
import requests
import sqlite3
import json


# # Create database, table and columns
# pokeDB = sqlite3.connect('Pokemon.db')
# pkCursor = pokeDB.cursor()
#
# pkCursor.execute('''CREATE TABLE pokemon
#                     (number integer primary key, name text)''')

# Retrieval process
# pkname = 'Charmander'
# pkCursor.execute('SELECT * FROM pokemon WHERE name=?', (pkname,))
# print(pkCursor.fetchone())

# process for adding a row to table
# pkCursor.execute('''INSERT INTO pokemon VALUES ('1','Charmander')''')

# pokeDB.commit()
# pokeDB.close()


# data capture from pokeApi
BASE_URL = 'http://pokeapi.co/api/v2/pokemon/'
searchPokemon = input("Pokemon name?: ").lower().strip()

response = requests.get(BASE_URL + searchPokemon)
jsonResponse = response.json()


# for k, v in jsonResponse.items():
#     print("keys: " + str(k) + " ------ " + " values: " + str(v))

for k, v in jsonResponse.items():
    if k != 'abilities':
        print(k, v)

# UP NEXT #######
# Finish adding keys to our database table as columns for the items we want to retain
# once we have that, we are pretty much set for this part of the backend until we config
# GUI.
####################################




