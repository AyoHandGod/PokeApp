"""
@Author: Dante Anthony
@Title: PokeApp
@Version: 1.1.0
"""
import requests
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import exists

# DB Table configuration
Base = declarative_base()
class Pokemon(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    base_experience = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    image = Column(String)

    def __repr__(self):
        return "<Pokemon(name='%s', base_experience='%s', weight='%s', height='%s', sprite_url='%s'>" %(self.name, self.base_experience, self.weight, self.height, self.image)

    def __init__(self, idNumber, name, baseXP, weight, height, sprite_url):
        self.id = idNumber
        self.name = name
        self.base_experience = baseXP
        self.weight = weight
        self.height = height
        self.image = sprite_url


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
    pokE = Pokemon(jsonResponse['id'], jsonResponse['name'], jsonResponse['base_experience'], jsonResponse['weight'],
               jsonResponse['height'], jsonResponse['sprites']['front_default'])
    addToDB(engine, pokE)


def addToDB(engine, pokemon):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(pokemon)
    session.commit()
    session.close()


def checkDB(engine, name):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(exists().where(Pokemon.name == name)).scalar()
    session.close()
    return result

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

    db = baseStart('Pokemon')
    pokeList = open("pokemon.txt", "r")
    pokeRead = pokeList.readlines()
    for x in pokeRead:
        x = x.strip().lower()
        testDB = checkDB(db, x)
        if not testDB:
            pokeQuery(db, x)
    Session = sessionmaker(bind=db)
    session = Session()
    for instance in session.query(Pokemon).order_by(Pokemon.id):
        print(instance.name, instance.id)
    session.close()

