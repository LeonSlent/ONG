import os
from flask import Flask
from controller.controller import Controller
from model.database import db
from model import cliente, funcionario, adotante, adocao, animal, pessoa

# Instância o Flask
app = Flask(__name__, template_folder=os.path.join('view', 'templates'))

# Configura o Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicia o Banco de Dados
db.init_app(app)

#Instância o Controller
controller = Controller()

#Cria todas as tabelas no banco de Dados
with app.app_context():
    db.create_all()

app.add_url_rule('/', 'home', controller.home)

if __name__ == '__main__':
    app.run(debug=True)