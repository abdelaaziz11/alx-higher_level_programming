#!/usr/bin/python3
"""
contains the class definition of a City
"""

from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]),
                           pool_pre_ping=True
                           )

    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    cities = session.query(State, City) \
                    .filter(State.id == City.state_id)

    for ci in cities:
        print("{}: ({}) {}".format(ci.State.name, ci.City.id, ci.City.name))

    session.close()
