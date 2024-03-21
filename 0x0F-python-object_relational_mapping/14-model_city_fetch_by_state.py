#!/usr/bin/python3
"""
prints all City objects from the database
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    cities = session.query(City, State).\
        filter(City.state_id == State.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
