from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import declarative_base
import psycopg2
import os

usuario = os.getenv("db_usuario", "postgres")
pwd = os.getenv("db_pwd", "1234")
host = os.getenv("db_host", "localhost")
port = os.getenv("db_port", "5432")
db = os.getenv("database", "postgres")

engine = create_engine(f'postgresql://{usuario}:{pwd}@{host}:{port}/{db}')
#engine = create_engine(f'postgresql://fer:12345678@localhost:8282/biblioteca')
db_session = scoped_session(sessionmaker(engine))

Database = declarative_base()
