import json

def search(pokefile, term):
    pokef = open("{0}.json".format(pokefile))
    pkjs = json.load(pokef)
    print(pkjs[term])

# search('jigglypuff', 'name')
