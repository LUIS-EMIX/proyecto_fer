from database import Database
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

class Libro(Database):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    autor = Column(String(100))
    year = Column(String(4))
    portada = Column(String(100))
    