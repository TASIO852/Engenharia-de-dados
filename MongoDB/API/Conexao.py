from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, redirect
import os
import pyodbc as odbc
import pandas as pd
from flask import Flask, jsonify, request

# inicio da api
Conexaodb = Flask(__name__)

mongoTestedadosjason = [
    {
        "id": 1,
        "sepalLength": 5.1,
        "sepalWidth": 3.5,
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "coluna": "etosa"
    },
    {
        "id": 2,
        "sepalLength": 4.9,
        "sepalWidth": 3.0,
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "coluna": "tosa"
    },
    {
        "id": 3,
        "sepalLength": 4.7,
        "sepalWidth": 3.2,
        "petalLength": 1.3,
        "petalWidth": 0.2,
        "coluna": "seto"
    },
    {
        "id": 4,
        "sepalLength": 4.6,
        "sepalWidth": 3.1,
        "petalLength": 1.5,
        "petalWidth": 0.2,
        "coluna": "set"
    },
]


@Conexaodb.route('/mongoTestedadosjason', methods=['GET'])
def obter_dados():
    return jsonify(mongoTestedadosjason)


@Conexaodb.route('/mongoTestedadosjason/<int:id>', methods=['GET'])
def consultar(coluna):
    for mongoTestedadosjason in mongoTestedadosjasondb:
        if mongoTestedadosjason.get('coluna') == coluna:
            return jsonify(mongoTestedadosjason)


Conexaodb.run(port=5000, host='localhost', debug=True)


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
