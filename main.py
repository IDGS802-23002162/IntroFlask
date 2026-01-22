from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route("/operasBas")
def operas1():
    return render_template("operasBas.html")

@app.route("/resultados", methods=["GET","POST"])
def resultado():
    opcion=request.form.get("opcion")
    n1=request.form.get("n1")
    n2=request.form.get("n2")

    if opcion == 1: 
        return f"La suma es: {float(n1)+float(n2)}"
    if else opcion == 2:
        return f"La resta es: {float(n1)-float(n2)}"
    else if opcion == 3:
        return f"La multiplicacion es: {float(n1)*float(n2)}"
    else if opcion == 4:
        return f"La division es: {float(n1)/float(n2)}"
    else:
        return f"Operacion no valida"
    

if __name__ == '__main__':
    app.run(debug=True)
