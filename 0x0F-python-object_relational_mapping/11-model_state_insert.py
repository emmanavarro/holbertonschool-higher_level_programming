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
                           format(username, password, db_name))
    Base.metadata.create_all(engine)
    # create a configured "Session" class
    Session = sessionmaker(engine)
    # create a Session
    session = Session()
    # create a new object
    new_state = State(name='Louisiana')
    # add a new object
    session.add(new_state)
    # confirm the current transaction
    session.commit()
    # print the new table after creation
    print(session.query(State).filter_by(name="Louisiana").first().id)
    # close the session
    session.close()
