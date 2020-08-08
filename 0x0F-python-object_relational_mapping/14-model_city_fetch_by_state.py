#!/usr/bin/python3
""" script that prints all City objects
    from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
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
    # query to get all City objects and print them
    query = session.query(State, City).filter(
            State.id == City.state_id).all()
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
