from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hola')
def hola():
    return 'Hola Pesados y Pesadas!'

# si no especifiquem res al decorator, és el mètode GET
@app.route('/formulario')
def formulario_get():
    # mostramos el formulario
    return """
<form method='post'>
    Introduce tu nombre:
    <input name='nombre' type='text' />
    <br>
    <input type='submit'>
</form>
"""
 
# importante importar la request para acceder a los datos adjuntos
from flask import request
 
@app.route('/formulario', methods=['POST'])
def formulario_post():
    # procesamos los datos del formulario
    nombre = request.form["nombre"]
    return "Salud, {}".format(nombre)
