from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, current_user
from datetime import datetime
from enum import Enum
from sqlalchemy import Enum as SqlEnum
from pytz import timezone
import os
from uuid import uuid4


# Configura o horario do brasil para utilizar no banco de dados
horario_brasil = timezone('America/Sao_Paulo')

UPLOAD_FOLDER = 'view/static/uploads'

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

class Tipo_User(Enum):
    CLIENTE = 'cliente'
    FUNCIONARIO = 'funcionario'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(50))
    data_nas = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(14), nullable=False, unique=True)
    tipo_usuario = db.Column(SqlEnum(Tipo_User), nullable=False)

    def is_funcionario(self):
        return self.tipo_usuario == Tipo_User.FUNCIONARIO

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(100), nullable=False)
    disponivel = db.Column(db.Boolean, default=True, nullable=False)
    nome_imagem = db.Column(db.String(250), nullable=False)

class Adocao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=lambda: datetime.now(horario_brasil), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pendente')
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    usuario = db.relationship('User', backref='adocoes')
    animal = db.relationship('Animal', backref='adocoes')

#class Admin(db.Model):

def registrar_usuario(nome, email, senha, data_nas, cpf):
    # Verifica se o email ja existe no banco de dados
    if db.session.query(User).filter_by(email=email).first() or db.session.query(User).filter_by(cpf=cpf).first() :
        return False

    novo_usuario = User(nome=nome, email=email, senha=senha, data_nas=data_nas, cpf=cpf, tipo_usuario=Tipo_User.CLIENTE)
    db.session.add(novo_usuario)
    db.session.commit()

    login_user(novo_usuario)

def registrar_animal(nome, idade, genero, especie, nome_imagem):
    novo_animal = Animal(nome=nome, idade=idade, genero=genero, especie=especie, nome_imagem=nome_imagem)
    db.session.add(novo_animal)
    db.session.commit()

def login_usuario(email, senha):
    usuario = db.session.query(User).filter_by(email=email, senha=senha).first()
    if not usuario:
        return False

    login_user(usuario)

def animal_existente(animal_id):
    animal = db.session.query(Animal).get(animal_id)
    if not animal:
        return False
    else:
        return animal

def processo_adocao(animal_id, sessao_usuario):
    nova_adocao = Adocao(animal_id=animal_id, usuario_id=sessao_usuario)
    db.session.add(nova_adocao)
    db.session.commit()


def listar_animais():
    return Animal.query.filter_by(disponivel=True).all()


def listar_adocoes():
    if current_user.tipo_usuario.value == 'cliente':
        return Adocao.query.filter_by(usuario_id=current_user.id).all()
    elif current_user.tipo_usuario.value == 'funcionario':
        return Adocao.query.all()

def animal_indisponivel(animal):
    animal.disponivel = False
    db.session.commit()

def animal_disponivel(animal):
    animal.disponivel = True
    db.session.commit()

def alterar_status_adocao(adocao_id, novo_status):
    adocao = db.session.query(Adocao).get(adocao_id)
    if adocao:
        adocao.status = novo_status
        db.session.commit()

def tratamento_imagem(imagem):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    extensao = imagem.filename.rsplit('.', 1)[1].lower()
    nome_imagem = f"{uuid4()}.{extensao}"
    imagem.save(os.path.join(UPLOAD_FOLDER, nome_imagem))

    return nome_imagem


"""
Criar um User como Funcionario
Abra o terminal dentro da pasta src
Digite os seguinte comandos:

flask shell

from model import User, Tipo_User, db

from datetime import date

novo_funcionario = User(
    nome='Admin',
    email='admin@gmail.com',
    senha='123',
    data_nas=date(9999, 9, 9),
    cpf='000.000.000-00',
    tipo_usuario=Tipo_User.FUNCIONARIO
)

db.session.add(novo_funcionario)
db.session.commit()

"""