from models import iniciar_ses
from flask import Flask, render_template, request
from flask import session
from flask import redirect, url_for
from models import create_client, iniciar_ses, add_prod_car, get_products

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass
    if 'username' in session:
        username = session['username']
        print(username)
    return render_template('index.html')

@app.route('/nosotros', methods=['GET', 'POST'])
def nosotros():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass
    return render_template('nosotros.html')

@app.route('/catalogo', methods=['GET', 'POST'])
def catalogo():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass
    return render_template('catalogo.html')

@app.route('/carrito', methods=['GET', 'POST'])
def carrito():
    if request.method == 'GET':
        pass
    posts = get_products()
    return render_template('carrito.html', posts_pro=posts)

@app.route('/acerca', methods=['GET', 'POST'])
def acercaa():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass
    return render_template('acerca.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['name']
        price = request.form['price']
        description = request.form['description']
        add_prod_car(1, nombre, description, price)
        return redirect(url_for('catalogo'))

@app.route('/register', methods=['GET', 'POST'])
def regis():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form['name']
        ape = request.form['ape']
        tel = request.form['tel']
        direc = request.form['direc']
        email = request.form['email']
        passwrd = request.form['password']
        if name == "":
            return "Error: Debe escribir el nombre"
        else:
            esc = create_client(name, ape, tel, direc, passwrd, email )
            session['username'] = name
            session['password'] = passwrd
            if esc == True:
                return redirect(url_for('main'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form['name']
        pos = request.form['password']
        if name == "":
            return "Error: Debe escribir el nombre"
        else:
            ver = iniciar_ses(name, pos)
            if ver == True:
                return redirect(url_for('catalogo'))
            else:
                return "Error: No esta registrado"
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logut():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)