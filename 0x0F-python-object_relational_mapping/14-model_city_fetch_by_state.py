#!/usr/bin/python3
"""

"""
import sys
from model_state import Base, State
from model_city import City
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
    myresult = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()
    for city, state in myresult:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
