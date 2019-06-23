from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import exists


# DB Table configuration
BASE = declarative_base()


class Pokemon(BASE):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    _base_xp = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    image = Column(String)

    def __init__(self, _id, name, baseXP, weight, height, sprite_url):
        self._id = id
        self._name = name
        self._base_xp = baseXP
        self._weight = weight
        self._height = height
        self._image = sprite_url

    def __repr__(self):
        return "<Pokemon(name='%s', base_experience='%s', weight='%s', " \
               "height='%s', sprite_url='%s'>" \
               % (self._name, self._base_xp, self.weight, self.height, self.image)
