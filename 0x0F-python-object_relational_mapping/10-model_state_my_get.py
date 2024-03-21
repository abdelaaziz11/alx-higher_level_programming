#!/usr/bin/python3

"""
lists all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    Session = sessionmaker(bind=engine)

    states = session.query(State).filter(State.name == argv[4]).first()
    if states:
        print("{}".format(states.id))
    else:
        print("Not found")
    session.close()
