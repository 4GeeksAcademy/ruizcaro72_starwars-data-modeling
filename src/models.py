import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    UsuarioID = Column(Integer, primary_key=True)
    Nombre = Column(String(100))
    Email = Column(String(100))
    Contraseña = Column(String(100))
    favoritos = relationship('Favorito', back_populates='usuario')

class Planeta(Base):
    __tablename__ = 'planeta'
    PlanetaID = Column(Integer, primary_key=True)
    Nombre = Column(String(100))
    Clima = Column(String(100))
    Terreno = Column(String(100))
    Poblacion = Column(Integer)
    favoritos = relationship('Favorito', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personaje'
    PersonajeID = Column(Integer, primary_key=True)
    Nombre = Column(String(100))
    AñoNacimiento = Column(String(20))
    Género = Column(String(20))
    favoritos = relationship('Favorito', back_populates='personaje')

class Favorito(Base):
    __tablename__ = 'favorito'
    FavoritoID = Column(Integer, primary_key=True)
    UsuarioID = Column(Integer, ForeignKey('usuario.UsuarioID'))
    PlanetaID = Column(Integer, ForeignKey('planeta.PlanetaID'))
    PersonajeID = Column(Integer, ForeignKey('personaje.PersonajeID'))

    usuario = relationship('Usuario', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
