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
    name = Column(String(40))
    base_xp = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    image = Column(String)

    def __repr__(self):
        return "<Pokemon(name='%s', base_experience='%s', weight='%s', " \
               "height='%s', sprite_url='%s'>" \
               % (self.name, self.base_xp, self.weight, self.height, self.image)
