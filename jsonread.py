import json

<<<<<<< HEAD
def search(pokefile, term):
    pokef = open("{0}.json".format(pokefile))
    pkjs = json.load(pokef)
    print(pkjs[term])

# search('jigglypuff', 'name')
=======
with open('meowth.json') as opj:
    jload = json.load(opj)
>>>>>>> c994bc5b5ce0f8c4d05e4a208e448be486f9a33a
