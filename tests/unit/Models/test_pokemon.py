import unittest
from unittest import TestCase

from Models import Pokemon
from Models.DatabaseManager import DatabaseManager
from Models import query


class TestPokemon(TestCase):

    def test_pokemon_instance_create(self):
        self.pokemon = Pokemon(id=2999, name="Test Mon", base_xp=3000, weight=4, height=6, image="No image")
        self.assertTrue(isinstance(self.pokemon, Pokemon), "Invalid pokemon object")


class TestDatabaseManager(unittest.TestCase):

    def setUp(self) -> None:
        self.db_manager = DatabaseManager(database_name="test2")

    def test_can_connect_to_database(self):
        self.db_manager = DatabaseManager(database_name="test2")
        self.assertTrue(self.db_manager.check_if_database_has("Test Mon"))

    def test_can_add_to_database(self):
        test_pokemon = Pokemon(id=3000, name="Test Mon2", base_xp=3000, weight=4, height=6)
        self.db_manager.add_to_db(test_pokemon)
        self.assertTrue(self.db_manager.check_if_database_has("Test Mon2"))

    def test_can_fill_database(self):
        self.db_manager.fill_database_with_pokemon()
        self.assertTrue(self.db_manager.check_if_database_has("Meowth"))


class TestApiFunctionality(unittest.TestCase):
    def test_can_find_pokemon_by_name(self):
        pokemon = query.pokeQuery("charmander")
        self.assertTrue(str(pokemon.name).lower() == "charmander")

    def test_can_grab_all_pokemon_from_api(self):
        self.db_manager = DatabaseManager(database_name="test2")
        pokemon_results = query.grab_all_pokemon_from_api()
        for pokemon in pokemon_results:
            print(self.db_manager.check_if_database_has(pokemon.name))