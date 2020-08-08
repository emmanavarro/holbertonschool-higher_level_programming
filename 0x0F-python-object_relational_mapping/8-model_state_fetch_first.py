#!/usr/bin/python3
""" script that prints the first State object
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

    first_state = session.query(State).first()
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # close the session
    session.close()
