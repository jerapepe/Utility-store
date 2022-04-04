import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_client(name, apel, tele, dire, passwor, email):
    con = sql.connect(path.join(ROOT, 'Tienda_huhuetlahtolli.db'))
    cur = con.cursor()
    cur.execute('insert into Cliente (Nombre, Apellidos, Telefono, Direccion, Password, Email) values (?,?,?,?,?,?)', (name, apel, tele, dire, passwor, email))
    con.commit()
    con.close()
    return True

def add_prod_car(id_cli, name, desc, precio):
    con = sql.connect(path.join(ROOT, 'Tienda_huhuetlahtolli.db'))
    cur = con.cursor()
    cur.execute('insert into Productos_carrito (ID_Cliente, Nombre_producto, descripcion, Precio_producto) values (?,?,?,?)', (id_cli, name, desc, precio))
    con.commit()
    con.close()

def get_products():
    con = sql.connect(path.join(ROOT, 'Tienda_huhuetlahtolli.db'))
    cur = con.cursor()
    cur.execute('select * from Productos_carrito')
    posts = cur.fetchall()
    return posts

def iniciar_ses(name, password):
    con = sql.connect(path.join(ROOT, 'Tienda_huhuetlahtolli.db'))
    cur = con.cursor()
    cur.execute('select * from Cliente where Nombre = ? and Password = ?', (name, password))
    posts = cur.fetchone()
    if posts:
        return True
    else:
        return False
