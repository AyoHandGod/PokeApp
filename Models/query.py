"""
@Author: Dante Anthony
@Title: PokeApp
@Version: 0.1.1
"""
import requests


# create database function
def baseStart(name):
    name = create_engine('sqlite:///' + name + '.db', echo=True)
    if not name.dialect.has_table(name, 'pokemon'):
        Base.metadata.create_all(name)
    return name


# data capture from pokeApi
def pokeQuery(engine, pokemon):
    BASE_URL = 'http://pokeapi.co/api/v2/pokemon/'
    searchPokemon = pokemon.lower().strip()
    response = requests.get(BASE_URL + searchPokemon)
    jsonResponse = response.json()
    # create pokemon object
    pokemon = Pokemon(id=api_response_json['id'], _name=api_response_json['name'],
                      _base_xp=api_response_json['base_experience'],
                      _weight=api_response_json['weight'], _height=api_response_json['height'],
                      _iamge=api_response_json['sprites']['front_default'])
    return pokemon


def checkDB(engine, name):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(exists().where(Pokemon.name == name)).scalar()
    session.close()
    return result

def checkDB2(db, search):
    c = db.cursor()
    c.execute('SELECT * FROM Pokemon WHERE name=?', (search,))
    data = c.fetchone()
    if data is None:
        print("Failed to find data")
        return False
    else:
        print(data[1])
        return data

# Create session and add Pokemon to DB
# session = Session()
# session.add(pokE)
# session.commit()
# session.close()

# UP NEXT #######
# Finish adding keys to our database table as columns for the items we want to retain
# once we have that, we are pretty much set for this part of the backend until we config
# GUI.
####################################

if __name__ == '__main__':
    checkDB2('Pokemon.db', 'char')
    # db = baseStart('Pokemon')
    # pokeList = open("pokemon.txt", "r")
    # pokeRead = pokeList.readlines()
    # for x in pokeRead:
    #     x = x.strip().lower()
    #     testDB = checkDB(db, x)
    #     if not testDB:
    #         pokeQuery(db, x)
    # Session = sessionmaker(bind=db)
    # session = Session()
    # for instance in session.query(Pokemon).order_by(Pokemon.id):
    #     print(instance.name, instance.id)
    # session.close()

