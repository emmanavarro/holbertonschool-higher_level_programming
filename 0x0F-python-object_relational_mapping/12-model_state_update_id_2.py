#!/usr/bin/python3
""" Script that adds the State object Louisiana to
    the database hbtn_0e_6_usa
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
    # query to change the name of the state
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    # confirm the current transaction
    session.commit()
    # close the session
    session.close()
