import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__="usuarios"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(24), nullable=False)
    favourites = relationship("Favoritos", backref= "usuarios", lazy=True)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

class Naves(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))


class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_planeta = Column(Integer, ForeignKey('planetas.id'))
    id_personaje = Column(Integer, ForeignKey('personajes.id'))
    id_nave = Column(Integer, ForeignKey('naves.id'))  


 
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagrama.png')