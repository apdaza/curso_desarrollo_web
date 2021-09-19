from flask import Flask, render_template, redirect, url_for, request
from models.modelo import *

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/listar')
def listar():
    data = consultar()
    return render_template('listar.html', data = data)

@app.route('/agregar', methods = ['POST', 'GET'])
def agregar():
    if request.method == 'GET':
        return render_template('agregar.html')
    else:
        info = request.form
        data = {
            'nombre': info['nombre'],
            'apellido': info['apellido'],
            'ciudad': info['ciudad']
        }
        insertar(data)
        return redirect(url_for('listar'))

@app.route('/eliminar/<id>')
def eliminar(id):
    eliminar_porid(id)
    return redirect(url_for('listar'))

@app.route('/editar/<id>', methods = ['POST', 'GET'])
def editar(id):
    if request.method == 'GET':
        data = consultar_porid(id)
        return render_template('editar.html', data = data)
    else:
        info = request.form
        data = {
            'nombre': info['nombre'],
            'apellido': info['apellido'],
            'ciudad': info['ciudad']
        }
        actualizar(id, data)
        return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(debug=True)