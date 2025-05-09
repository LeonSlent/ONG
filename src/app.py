import os
from flask import Flask
from flask_login import LoginManager
from model import config_db
from controller import controller_bp, user_loader_funcao


# Instância o Flask
app = Flask(__name__, static_folder='view/static', template_folder='view/templates')

app.secret_key = 'secret_key'


login_manager = LoginManager(app)
login_manager.user_loader(user_loader_funcao)
login_manager.login_view = 'controller_bp.login'

# Chamada a função para configurar o Banco de Dados
config_db(app)

# Registra o Blueprint (rotas)
app.register_blueprint(controller_bp)

if __name__ == '__main__':
    app.run(debug=True)