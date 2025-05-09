from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

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
    #cpf = db.Column(db.Integer(11))
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String())


'''
class UserTell(UserMixin, db.Model):
    Tell = db.Column(db.Integer(11), primary_Key=True)
    UserCPF = db.Column(db.Integer,db.ForeignKey('Admin.Cpf'), primary_key=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)



class Admin(UserMixin, db.Model):
    Mat = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    Name = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)
    Cpf = db.Column(db.Integer(11), nullable=False)
    Role = db.Column(db.String(10), nullable=False, default='admin')
    Password = db.Column(db.TEXT, nullable=False)


class AdminTell(UserMixin, db.Model):
    AdminMat = db.Column(db.String(36), db.ForeignKey('Admin.Mat'), primary_key=True, nullable=False)
    Tell = db.Column(db.Integer(11), prmary_key=True, nullable=False)
    Name = db.Column(db.String(50), nullable=False)


class Animal(UserMixin, db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Porte = db.Column(db.String(50), nullable=False)
    Race = db.Column(db.String(50), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    Cast = db.Column(db.Boolean, nullable=False, default=False)
    Image = db.Column(db.Blob, nullable=False, default=ANIMAL_HOLDER)


class Adoption(UserMixin, db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Data = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    Status = db.Column(db.String(10), nullable=False, default='Idle')
    AnimalId = db.Column(db.Integer,db.ForeignKey('Animal.Id'), nullable=False)
    AdminMat = db.Column(db.Integer,db.ForeignKey('Admin.Mat'), nullable=False)
    UserCpf = db.Column(db.Integer,db.ForeignKey('Admin.Cpf'), nullable=False)
'''