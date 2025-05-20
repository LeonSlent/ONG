from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user

db = SQLAlchemy()

def config_db(app):
    # Configura o Banco de Dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicia o Banco de Dados
    db.init_app(app)

    #Cria todas as tabelas no banco de Dados
    with app.app_context():
        db.create_all()



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String())

class Animal(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(100), nullable=False)
    #imagem = db.Column(db.String, nullable=False)


def registrar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    novo_usuario = User(nome=nome, email=email, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()

    login_user(novo_usuario)

def registrar_animal():
    nome = request.form['nome']
    idade = request.form['idade']
    genero = request.form['genero']
    especie = request.form['especie']


    novo_animal = Animal(nome=nome, idade=idade, genero=genero, especie=especie)
    db.session.add(novo_animal)
    db.session.commit()

def login_usuario():
    email = request.form['email']
    senha = request.form['senha']

    usuario = db.session.query(User).filter_by(email=email, senha=senha).first()
    if not usuario:
        return False

    login_user(usuario)
