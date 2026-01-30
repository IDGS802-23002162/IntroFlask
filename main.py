from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)

import math
import forms


app.secret_key='Clave secreta'
csrf=CSRFProtect()


@app.route('/')
def index():
    titulo = "IDGS-802 Flask"
    lista = ['Juan', 'Karla', 'Miguel', 'Ana']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/formularios')
def formularios():
    return render_template("formularios.html")

@app.route('/reportes')
def reportes():
    return render_template("reportes.html")

@app.route('/hola')
def hola():
    return "¡Hola, Hola!"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return f"Número: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"ID: {id} nombre: {username}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    resultado = n1 + n2
    return f"<h1>Calculadora</h1><p>La suma de {n1} + {n2} es: <strong>{resultado}</strong></p>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func2(param="Juan"):
    return f"<h1>Hola, {param}</h1>"

@app.route("/operas")
def operas():
    return '''
    <form>
        <label>Name:</label>
        <input type="text"><br>
        <label>Apellido Paterno:</label>
        <input type="text"><br>
        <input type="submit">
    </form>
    '''

@app.route("/operasBas", methods=["GET","POST"])
def operas1():
    n1=0
    n2=0
    res=0

    if request.method == "POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        res=float(n1)/float(n2)

    return render_template("operasBas.html", n1=n1,n2=n2,res=res)

@app.route("/resultados", methods=["GET","POST"])
def resultado():
    opcion=0
    n1=0
    n2=0

    if request.method == "POST":
        opcion=request.form.get("opcion")
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        if opcion == 1:
            resultado=("la suma es:" + n1+n2)
        elif opcion == 2:
            resultado=("la resta es:" + n1-n2)
        elif opcion == 3:
            resultado=("la multiplicacion es:" + n1*n2)
        elif opcion == 4:
            resultado=("la division es:" + n1/n2)
        else: 
            resultado=("Operacion no valida")
    return render_template("operasBas.html")
    
    

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    resultado = None

    if request.method == "POST":
        X1 = float(request.form["X1"])
        X2 = float(request.form["X2"])
        Y1 = float(request.form["Y1"])
        Y2 = float(request.form["Y2"])

        resultado = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

    return render_template("distancia.html", resultado=resultado)

@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
    mat = 0
    nom = ''
    apa = ''
    ama = ''
    email = ''

    usuarios_class = forms.UserForm(request.form)

    if request.method == "POST" and usuarios_class.validate():
        mat = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.apaterno.data
        ama = usuarios_class.amaterno.data
        email = usuarios_class.correo.data

        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)

    return render_template(
        "usuarios.html",
        form=usuarios_class,
        mat=mat,
        nom=nom,
        apa=apa,
        ama=ama,
        email=email
    )

@app.route('/compra', methods=["GET","POST"])
def compra():
    boleto=12
    total=0

    compra_class = forms.CineForm(request.form)

    if request.method == "POST" and compra_class.validate():

        nombre=compra_class.nombre.data
        compradores=compra_class.compradores.data
        cantidad=compra_class.cantidad.data
        cantidadMaxima=compradores*7
        tarjeta=int(request.form.get("tarjeta"))

       

        if cantidad > cantidadMaxima:
            mensaje = 'Solo se permiten 7 boletos por coprador ({} en total)'.format(cantidadMaxima)
            flash(mensaje)
        else:
            temporal=boleto*cantidad
            mensaje='Bienvenido {}'.format(nombre)
            flash(mensaje)

            if cantidad > 5: 
                total=(temporal)-(temporal*0.15)
                if tarjeta == 1:
                    total=total-(total*0.1)
            elif cantidad in(3,4,5):
                total=(temporal)-(temporal*0.10)
                if tarjeta == 1:
                    total=total-(total*0.1)
            else:
                total=(boleto*cantidad)
                if tarjeta == 1:
                    total=total-(total*0.1)

    return render_template("compra.html", form=compra_class,
    total=total)



if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
