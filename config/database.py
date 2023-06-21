import os
from sqlalchemy import create_engine






from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_name = "../database.sqlite"

database_directory = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(database_directory, database_name)}"

database_engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=database_engine)

Base = declarative_base()
