import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    people_id = Column(Integer, ForeignKey('peoples.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=True)
    
    user = relationship('Users', foreign_keys=[user_id] , backref='favorites')
    people = relationship('Peoples', foreign_keys=[people_id] , backref='favorites')
    planet = relationship('Planets',foreign_keys=[planet_id] , backref='favorites')
    species = relationship('Species',foreign_keys=[species_id], backref='favorites')


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column (String(250), unique=True, nullable=False)
    password = Column (String(250), nullable=False)


class Peoples(Base):
    __tablename__ = 'peoples'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(80), nullable=False)
    hair_color = Column(String(80), nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users, backref='peoples')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    terrain = Column(String(80), nullable=False)
    climate = Column(String(80), nullable=False)
    rotation_period  = Column(Integer, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users, backref='planets')

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    average_height = Column(Integer, nullable=False)
    hair_colors = Column(String(80), nullable=False)
    skin_colors= Column(String(80), nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users, backref='species')
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
