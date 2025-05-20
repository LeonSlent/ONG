from flask import Flask
from model import config_db, login_manager
from controller import controller_bp


# Instância o Flask
app = Flask(__name__, static_folder='view/static', template_folder='view/templates')

app.secret_key = 'secret_key'

# Inicia o Login Manager com o app
login_manager.init_app(app)

#Função para enviar o usuario para a rota de login se ele não estiver logado
login_manager.login_view = 'controller_bp.login'

# Chamada a função para configurar o Banco de Dados
config_db(app)

# Registra o Blueprint (rotas)
app.register_blueprint(controller_bp)

if __name__ == '__main__':
    app.run(debug=True)