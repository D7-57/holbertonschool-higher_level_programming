#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format
        (username, password, db_name),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing 'a' in name
    states = session.query(State).filter
    (State.name.like('%a%')).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
