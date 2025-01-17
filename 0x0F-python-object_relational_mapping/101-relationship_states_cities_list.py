#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects
from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]


    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')


    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id, City.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
