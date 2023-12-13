from models import Libro
from database import db_session
from flask import render_template
import models


def get_libro(id):
    libro = db_session.query(models.Libro).all()
    return render_template("vista.html", libro=libro)

def delete_libro(id):
    libro = get_libro(id)
    db_session.delete(libro)
    db_session.commit()

    