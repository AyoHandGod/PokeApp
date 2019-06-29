from sqlalchemy import MetaData
from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy.sql.expression import exists

from Models import Pokemon, BASE
import Models.Models


# decided to use DatabaseManager class to ease dependency on sqlalchemy.
class DatabaseManager:

    def __init__(self, database_system: str = 'sqlite', database_name: str = 'default') -> None:
        self._database_system = database_system
        self._database_name = database_name
        self._engine = self.connect_to_database()
        self._sessionmaker = sessionmaker(bind=self._engine)

    def connect_to_database(self) -> Engine:
        """
        Connects to database and returns engine
        :return: SqlAlchemy Engine
        """
        database_engine = create_engine(self._database_system + ':///' + self._database_name + '.db', echo=True)
        meta = MetaData(database_engine)
        if not database_engine.dialect.has_table(database_engine, Pokemon.__tablename__):
            BASE.metadata.create_all(database_engine)
        return database_engine

    def add_to_db(self, pokemon: Pokemon) -> None:
        """
        add item to database
        :return:
        """
        session = self._sessionmaker()

        session.add(pokemon)
        session.commit()
        session.close()

    def query_database(self, name: str) -> Query:
        """
        Checks if specified name in database
        :param name: string name
        :return: boolean result of query
        """
        session = self._sessionmaker()
        found_pokemon_bool = session.query(exists().where(Pokemon.name == name))
        pokemon = session.query(Pokemon).all()
        print(pokemon)
        session.close()
        return found_pokemon_bool
