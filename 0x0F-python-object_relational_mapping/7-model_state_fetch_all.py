#!/usr/bin/python3
""" script that lists all State objects
    from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # an Engine, which the Session will use for connection
    # resources
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(engine)

    # create a Session
    session = Session()

    states_q = session.query(State).order_by(State.id)
    for state in states_q.all():
        print("{}: {}".format(state.id, state.name))
