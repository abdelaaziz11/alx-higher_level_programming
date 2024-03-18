#!/usr/bin/python3

"""
deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

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

    states = session.query(State).filter(State.name.ilike('%a%')).all()

    for state in states:
        session.delete(state)
    session.commit()
    session.close()
