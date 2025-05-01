from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required
from model.usuario import Usuario
from model.database import db


# Cria o Blueprint
controller_bp = Blueprint('controller_bp', __name__, template_folder='../view/templates')

# Rota principal
@controller_bp.route('/')
def home():
    return render_template('home.html')

# Função normal para usar no user_loader do login_manager no app.py
def user_loader_funcao(id):
    usuario = db.session.query(Usuario).filter_by(id=id).first()
    return usuario

# Rota para registrar o Usuario
@controller_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        login_user(novo_usuario)

        return redirect(url_for('controller_bp.home'))

    return render_template('registrar.html')

# Rota para logar o Usuario
@controller_bp.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = db.session.query(Usuario).filter_by(email=email, senha=senha).first()
        if not usuario:
            return render_template('logar.html')

        login_user(usuario)
        return redirect(url_for('controller_bp.home'))
        
    return render_template('logar.html')
        
# Possivel Rota para adotar o Animal
@controller_bp.route('/adotar')
@login_required
def adotar():
    return 'me adota ai'
    

