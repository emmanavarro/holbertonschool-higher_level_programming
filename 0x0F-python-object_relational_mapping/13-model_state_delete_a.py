#!/usr/bin/python3
""" Script that deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    # an Engine, which the Session will use for connection resources
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    # create a configured "Session" class
    Session = sessionmaker(engine)
    # create a Session
    session = Session()
    # query to get and delete all abjects containing letter a
    states = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in states:
        session.delete(state)
    # confirm the current transaction
    session.commit()
    # close the session
    session.close()
