import sys, uuid, requests, os, json, datetime

from sqlalchemy.dialects.mysql import TEXT
from flask_sqlalchemy import SQLAlchemy
from cryptograph import Cryptograph
from flask_login import UserMixin
from dotenv import load_dotenv
from flask import jsonify
from flask import Flask

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')
    with open('/static/images/animal_holder.png', 'rb') as f:
        ANIMAL_HOLDER = f.read()
    crypograph = Cryptograph()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = SECRET_KEY
    db = SQLAlchemy(app)

class User(UserMixin, Config.db.Model):
    Cpf = Config.db.Column(Config.db.Integer(11), primary_key=True)
    Name = Config.db.Column(Config.db.String(50), nullable=False)
    Email = Config.db.Column(Config.db.String(50), nullable=False)
    Password = Config.db.Column(Config.db.String(50), nullable=False)
    Role = Config.db.Column(Config.db.String(10), nullable=False, default='user')
    Password = Config.db.Column(Config.db.TEXT, nullable=False)

    def toDict(self):
        return {
            'Cpf': self.Cpf,
            'Name': self.Name,
            'Email': self.Email,
            'Password': self.Password
        }
        
class UserTell(UserMixin, Config.db.Model):
    Tell = Config.db.Column(Config.db.Integer(11), primary_Key=True)
    UserCPF = Config.db.Column(Config.db.Integer,Config.db.ForeignKey('Admin.Cpf'), primary_key=True, nullable=False)
    Name = Config.db.Column(Config.db.String(50), nullable=False)

    def toDict(self):
        user = User.query.filter_by(Cpf=self.UserCPF).first().toDict()
        
        return{
        'Tell': self.Tell,
        'Name': self.Name,
        'user': user    
        }
    
class Admin(UserMixin, Config.db.Model):
    Mat = Config.db.Column(Config.db.String(36), primary_key=True, default=str(uuid.uuid4()))
    Name = Config.db.Column(Config.db.String(50), nullable=False)
    Email = Config.db.Column(Config.db.String(50), nullable=False)
    Password = Config.db.Column(Config.db.String(50), nullable=False)
    Cpf = Config.db.Column(Config.db.Integer(11), nullable=False)
    Role = Config.db.Column(Config.db.String(10), nullable=False, default='admin')
    Password = Config.db.Column(Config.db.TEXT, nullable=False)

    def toDict(self):
        return {
            'Cpf': self.Cpf,
            'Name': self.Name,
            'Email': self.Email,
            'Password': self.Password,
            'CPF': self.Cpf
        }
    
class AdminTell(UserMixin, Config.db.Model):
    AdminMat = Config.db.Column(Config.db.String(36), Config.db.ForeignKey('Admin.Mat'), primary_key=True, nullable=False)
    Tell = Config.db.Column(Config.db.Integer(11), prmary_key=True, nullable=False)
    Name = Config.db.Column(Config.db.String(50), nullable=False)
    
    def toDict(self):
        admin = Admin.query.filter_by(Mat=self.AdminMat).first().toDict()
        
        return{
            'Admin': admin,
            'Tell': self.Tell,
            'Name': self.Name
        }
    
class Animal(UserMixin, Config.db.Model):
    Id = Config.db.Column(Config.db.Integer, primary_key=True)
    Porte = Config.db.Column(Config.db.String(50), nullable=False)
    Race = Config.db.Column(Config.db.String(50), nullable=False)
    Name = Config.db.Column(Config.db.String(50), nullable=False)
    Type = Config.db.Column(Config.db.String(50), nullable=False)
    Cast = Config.db.Column(Config.db.Boolean, nullable=False, default=False)
    Image = Config.db.Column(Config.db.Blob, nullable=False, default=Config.ANIMAL_HOLDER)
    
    def toDict(self):
        return{
            'Id': self.Id,
            'Porte': self.Porte,
            'Race': self.Race,
            'Name': self.Name,
            'Type': self.Type,
            'Castra': self.Cast,
            'Image': self.Image
        }
    
class Adoption(UserMixin, Config.db.Model):
    Id = Config.db.Column(Config.db.Integer, primary_key=True)
    Data = Config.db.Column(Config.db.DateTime, nullable=False, default=datetime.datetime.now())
    Status = Config.db.Column(Config.db.String(10), nullable=False, default='Idle')
    AnimalId = Config.db.Column(Config.db.Integer,Config.db.ForeignKey('Animal.Id'), nullable=False)
    AdminMat = Config.db.Column(Config.db.Integer,Config.db.ForeignKey('Admin.Mat'), nullable=False)
    UserCpf = Config.db.Column(Config.db.Integer,Config.db.ForeignKey('Admin.Cpf'), nullable=False)

    def toDict(self):
        user = User.query.filter_by(Cpf=self.UserCpf).first().toDict()
        admin = Admin.query.filter_by(Mat=self.AdminMat).first().toDict()
        animal = Animal.query.filter_by(Id=self.AnimalId).first().toDict()

        return{
            'Id': self.Id,
            'Data': self.Data,
            'Status': self.Status,
            'Animal': animal,
            'Admin': admin,
            'User': user
        }
        
class Database:
    def __init__(self) -> None:
        ...