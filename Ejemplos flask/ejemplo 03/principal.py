from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/verificacion/<nombre>')
def verificacion(nombre):
    if nombre == 'admin':
        usuario = 'Administrador del sistema'
    else:
        usuario = "Invitado"
    return render_template('index.html', usuario = usuario)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        nombre = request.form['nombre']
        return redirect(url_for('verificacion', nombre = nombre))    

if __name__ == '__main__':
    app.run(debug = True)
