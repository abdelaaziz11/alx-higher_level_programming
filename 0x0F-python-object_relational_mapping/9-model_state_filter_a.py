#!/usr/bin/python3

"""
lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
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

    # Ensure consistent indentation for the continuation line
    session = Session()

    """states = session.query(State)\
            .filter(State.name.ilike('%a%')).order_by(State.id).all()"""
    states = session.query(State).filter(State.name.ilike('%a%')) \
                    .order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
