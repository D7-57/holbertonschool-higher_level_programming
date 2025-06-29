#!/usr/bin/python3
"""Defines a State class linked to the states table in a MySQL database"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """State class mapped to the 'states' table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
