#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    delete_states = session.query(State).filter(State.name.like('%a%')).all()
    for state in delete_states:
        session.delete(state)

    session.commit()
    session.close()
