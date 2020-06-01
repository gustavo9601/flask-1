"""
#Instalar flask
pip install flask

#Subir servicio de Flask
flask run

#Si el nombre del archivo es diferente a app en la consola para setear
set FLASK_APP=nameFile.py

#Cambiar el ambiente de trabajo ya que por default esta en production
set FLASK_ENV=development

"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def inicio():
    app.logger.debug('Mensaje de debugger')
    app.logger.info('Mensaje de info')
    app.logger.warn('Mensaje de Warnign')
    app.logger.error('Mensaje de error')
    # usamos el request de flask que trae informacion de la peticion
    print(f'Entramos al path: {request.path}')
    return 'Hola Mundo desde Flask- Cool'

@app.route('/saludar/<mensaje>')
def saludar(mensaje):
    return f'<h1>Saludos a {mensaje.upper()}</h1>'

@app.route('/edad/<int:edad>')
def saber_Edad(edad):
    return f'<h1>La edad es: {edad}</h1>'