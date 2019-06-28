import unittest
from unittest import TestCase

from sqlalchemy.engine import Engine

from Models import create_database
from Models import Pokemon
from Models import query


class TestPokemon(TestCase):

    def test_pokemon_instance_create(self):
        self.pokemon = Pokemon(id=2999, name="Test Mon", base_xp=3000, weight=4, height=6, image="No image")
        self.assertTrue(isinstance(self.pokemon, Pokemon), "Invalid pokemon object")

    def test_can_create_database(self):
        self.database_engine = create_database("test")
        self.assertTrue(isinstance(self.database_engine, Engine), "Database engine created")

    def test_can_store_pokemon_in_database(self):
        self.database_engine = create_database("test")
        self.pokemon = Pokemon(id=2999, name="Test Mon", base_xp=3000, weight=4, height=6, image="No image")
        try:
            query.add_to_db(self.database_engine, self.pokemon)
        except Exception as e:
            print("Database add failed due to: " + str(e))

    def test_can_query_database_for_pokemon_name(self):
        self.database_engine = create_database("test")
        self.assertTrue(query.query_database(self.database_engine, "Test Mon"))
