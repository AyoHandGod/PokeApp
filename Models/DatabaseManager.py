"""
@Author: Dante Anthony
@Title: PokeApp.Models.DatabaseManager
@Version: 0.1.4
"""
import datetime
import logging

import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.engine import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy.sql.expression import exists

from Models import Pokemon
from Models import BASE
from Models import query


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("PokemonDB.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


# decided to use DatabaseManager class to ease dependency on sqlalchemy.
class DatabaseManager:

    def __init__(self, database_system: str = 'sqlite', database_name: str = 'default') -> None:
        self._database_system = database_system
        self._database_name = database_name
        self._engine = self._connect_to_database()
        self._sessionmaker = sessionmaker(bind=self._engine)
        logger.log(logging.INFO, str(datetime.datetime.now()) + " Creating Database Manager")

    def _connect_to_database(self) -> Engine:
        """
        Connects to database and returns engine
        :return: SqlAlchemy Engine
        """
        database_engine = create_engine(self._database_system + ':///' + self._database_name + '.db', echo=True)
        if not inspect(database_engine).has_table(Pokemon.__tablename__):
            BASE.metadata.create_all(database_engine)
        logger.log(logging.INFO, str(datetime.datetime.now()) + "Database connection established. "
                                                                "System: {}, DB_NAME: {}"
                   .format(self._database_system, self._database_name))
        return database_engine

    def add_to_db(self, pokemon: Pokemon) -> None:
        """
        add item to database
        :return:
        """
        session = self._sessionmaker()

        session.add(pokemon)
        session.commit()

        logger.log(logging.INFO, "Pokemon added to database. Name: {}".format(str(pokemon.name)))
        session.close()

    def check_if_database_has(self, name: str) -> Query:
        """
        Checks if specified name in database
        :param name: string name
        :return: boolean result of query
        """
        session = self._sessionmaker()
        found_pokemon_bool = session.query(session.query(Pokemon).filter(Pokemon.name == name).exists()).scalar()
        stmt = sqlalchemy.text('SELECT * FROM Pokemon where name = ' + '"' + name + '"')
        result = session.execute(stmt)
        print(result)
        print(found_pokemon_bool)
        print(type(found_pokemon_bool))
        session.close()
        return found_pokemon_bool

    def fill_database_with_pokemon(self):
        pokemon_results = query.grab_all_pokemon_from_api()
        for pokemon in pokemon_results:
            self.add_to_db(pokemon)


