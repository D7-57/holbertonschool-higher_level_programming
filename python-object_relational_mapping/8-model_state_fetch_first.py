#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get database credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format
        (username, password, db_name),
        pool_pre_ping=True
    )

    # Create a configured session class and instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Print result or "Nothing"
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()
