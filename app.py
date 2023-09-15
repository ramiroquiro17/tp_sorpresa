from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
ma = Marshmallow(app)
@app.route("/")
def home():
    return "index"

@app.route("/contactos")
def contactos():
    return "contactos"

class UserSchema(ma.Schema):
    username = fields.String()
    email = fields.String()
    password = fields.String()
    saludo_function = fields.Method('probando_metodo')

class PostSchema(ma.Schema):
    titulo = fields.Integer()
    subtitulo = fields.String()
    cuerpo = fields.String()
    
    

    