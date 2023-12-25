from urllib import response
import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysql_connector import MySQL
from flask import Flask, session, redirect, g
from flask import request,flash
from flask import jsonify
from flask import render_template,url_for
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones
from flaskext.mysql import MySQL
from backends.blueprints.evento_blueprint import evento_blueprint
from backends.blueprints.ponente_blueprint import ponente_blueprint

from backends.models.evento import EventoModel
from backends.models.ponente import PonenteModel

app = Flask(__name__,template_folder='frontend/templates',static_folder='frontend/static')

app.secret_key= "averysecretkey"

mysql = MySQL()
app.register_blueprint(evento_blueprint)
app.register_blueprint(ponente_blueprint)

cors = CORS(app)
mysql = MySQL(app)
mysql.init_app(app)

@app.route('/', methods=['GET'])
def Index():
    response = requests.post("http://127.0.0.1:5000/api/evento/get_all").json()
    return render_template('home.html', eventos=response)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validate_login', methods = ['POST'])
def validate_login():
    if request.method == 'POST':
        correo = request.form['typeEmailX']
        password = request.form['typePasswordX']
        users=requests.post("http://127.0.0.1:5000/api/ponente/get_all").json()
        user={}
        for x in users:
            if x['correo']==correo:
                user=x
                break
        if not user:
            return "Not found"
        elif password == user['nombre']:
            session['correo'] = user['correo']
            return  redirect(url_for('Index'))

    return redirect(url_for('error'))

@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')

@app.route('/logout')
def logout():
    if 'correo' in session:
        session.pop('correo', None)
        return render_template('index.html')

@app.route('/registro', methods=['GET'])
def Registro():
    return render_template('registrar.html')

@app.route('/evento/<int:id>', methods=['GET'])
def Evento(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/evento/get", json=query).json()
    #evento = EventoModel(resp['id'], resp['ponente'], resp['id_lista'], resp['nombre'], resp['detalles'], resp['link'])
    return render_template('evento.html', evento=resp)

@app.route('/profile/<int:id>', methods=['GET'])
def Profile(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/ponente/get", json=query).json()
    return render_template('profile.html', ponente=resp)

if __name__ == "__main__":
    app.run(debug=True)

#branch: gabriel