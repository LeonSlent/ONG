#rotas que vão renderizar os templates aqui

import os
from flask import Flask
from flask_login import LoginManager
from controller import controller_bp, user_loader_funcao
import model

# Instância o Flask
app = Flask(__name__, template_folder=os.path.join('view', 'templates'))

app.secret_key = 'chave_secreta'

login_manager = LoginManager(app)
login_manager.user_loader(user_loader_funcao)
login_manager.login_view = 'controller_bp.logar'

# Chamada a função para configurar o Banco de Dados
config_db(app)

# Registra o Blueprint (rotas)
app.register_blueprint(controller_bp)

if __name__ == '__main__':
    app.run(debug=True)