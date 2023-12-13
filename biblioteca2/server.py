from datetime import datetime
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from database import Database
from database import engine
from database import db_session

import models
from services import delete_libro
app = Flask(__name__)

Database.metadata.create_all(engine)

@app.get('/')
def home():
    libro = db_session.query(models.Libro).all()
    return render_template("vista.html", libro=libro)

@app.get('/crear')
def crear():
    return render_template("registro.html")

@app.get('/act/<id>/update')
def act(id):
    libro = db_session.query(models.Libro).get(id)
    return render_template("actualizar.html", libro=libro)

@app.post('/registro')
def registro():
    nombre = request.form['nombre']
    autor = request.form['autor']
    year = request.form['year']
    portada = request.form['portada']
    

    nuevo_libro = models.Libro(
        nombre = nombre,
        autor = autor,
        year = year,
        portada = portada
    )
    db_session.add(nuevo_libro)
    db_session.commit()
    return redirect(url_for('home'))


@app.get('/eliminar/<id>/delete')
def eliminar(id):
    libro = db_session.query(models.Libro).get(id)

    db_session.delete(libro)
    db_session.commit()

    return redirect(url_for('home'))

@app.post('/actualizar/<id>/update')
def actualizar(id):
    libro = db_session.query(models.Libro).get(id)

    nuevo_id = request.form['id_a'] 
    nuevo_nombre = request.form['nombre_a']
    nuevo_autor = request.form['autor_a']
    nuevo_year = request.form['year_a']
    nuevo_portada = request.form['portada_a']
    

    libro.id = nuevo_id
    libro.nombre = nuevo_nombre
    libro.autor = nuevo_autor
    libro.year = nuevo_year
    libro.portada = nuevo_portada
    
    db_session.add(libro)
    db_session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run('0.0.0.0', 7070, debug=True)