#!/usr/bin/python3
""" Script that prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # an Engine, which the Session will use for connection
    # resources
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    st_name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name))
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(engine)

    # create a Session
    session = Session()

    states = session.query(State).filter(State.name == st_name).first()
    print(states.id if states else 'Not found')

    # close the session
    session.close()
