from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola mundo en flask"

@app.route('/hola/<nombre>')
def hola_saludo(nombre):
    return "Hola %s" % nombre

@app.route('/saludar/<int:cantidad>')
def saludar(cantidad):
    return "Hola " * cantidad

if __name__ == '__main__':
    app.run(debug = True)