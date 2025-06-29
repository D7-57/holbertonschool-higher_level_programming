#!/usr/bin/python3
"""Prints the id of a State object with a given name from the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format
        (username, password, db_name),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for state by name (safe from SQL injection)
    state = session.query(State).filter(State.name == state_name).first()

    # Output the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
