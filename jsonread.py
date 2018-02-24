import json
from pprint import pprint

#<<<<<<< HEAD
def search(pokefile, term):
    pokef = open("{0}.json".format(pokefile), 'r')
    pkjs = json.load(pokef)
    return pprint(pkjs[term])
