from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine(db_uri, echo=False)
db_session = scoped_session(sessionmaker())

Base = declarative_base()
Base.query = db_session.query_property()


def initialize_sql():
    db_session.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)
