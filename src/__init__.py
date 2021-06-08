# importamos los módulos
# flask
from flask import Flask, request, jsonify
# orm
from flask_sqlalchemy import SQLAlchemy
# parseos
from flask_marshmallow import Marshmallow


app = Flask(__name__)
# base de datos: tipo+driver://usuario:clave@ip/bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://fcojfuwzntvrdk:a454fca9d0e8fdf3b4d088d10bc858dca0491016c6874694e429a986279a24e9@ec2-54-216-185-51.eu-west-1.compute.amazonaws.com:5432/d3lpo29it4ck3g'
# postgresql+psycopg2://fcojfuwzntvrdk:a454fca9d0e8fdf3b4d088d10bc858dca0491016c6874694e429a986279a24e9@ec2-54-216-185-51.eu-west-1.compute.amazonaws.com/d3lpo29it4ck3g
# mysql+pymysql://root:Lunnis-2310@localhost/proyecto

# para evitar warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instancia de la base de datos a través del orm
bd = SQLAlchemy(app)

# instancia de marshmallow para generar esquemas y facilitar parseo
ma = Marshmallow(app)

