#!/usr/bin/python3
"""Create the states table in a given database using SQLAlchemy"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create engine using provided MySQL credentials
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    
    # Create all tables defined via Base metadata (in this case, State)
    Base.metadata.create_all(engine)
