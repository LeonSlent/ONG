from flask_sqlalchemy import SQLAlchemy


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