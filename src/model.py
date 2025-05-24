from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager
from datetime import datetime

# Banco de Dados
db = SQLAlchemy()

def config_db(app):
    # Configura o Banco de Dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicia o Banco de Dados com o app
    db.init_app(app)

    #Cria todas as tabelas no banco de Dados
    with app.app_context():
        db.create_all()

# Instância o Login Manager
login_manager = LoginManager()

# Função responsável por carregar o usuário a partir do ID salvo na sessão.
@login_manager.user_loader
def user_loader(id):
    return db.session.query(User).filter_by(id=id).first()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(50))
    data_nas = db.Column(db.String(15), nullable=False)
    cpf = db.Column(db.String(14), nullable=False, unique=True)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(100), nullable=False)

#class Adocao(UserMixin, db.Model):
#class Admin(UserMixin, db.Model):

def registrar_usuario(nome, email, senha):
    # Verifica se o email ja existe no banco de dados
    if db.session.query(User).filter_by(email=email).first():
        return False

    novo_usuario = User(nome=nome, email=email, senha=senha, data_nas=data_nas, cpf=cpf)
    db.session.add(novo_usuario)
    db.session.commit()

    login_user(novo_usuario)

def registrar_animal(nome, idade, genero, especie):
    novo_animal = Animal(nome=nome, idade=idade, genero=genero, especie=especie)
    db.session.add(novo_animal)
    db.session.commit()

def login_usuario(email, senha):
    usuario = db.session.query(User).filter_by(email=email, senha=senha).first()
    if not usuario:
        return False

    login_user(usuario)

def listar_animais():
    return Animal.query.all()

def animal_existente(animal_id):
    animal = db.session.query(Animal).get(animal_id)
    if not animal:
        return False
    else:
        return animal
