from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from model import User
from model import db


# Cria o Blueprint
controller_bp = Blueprint('controller_bp', __name__, template_folder='../view/templates')

# Rota principal
@controller_bp.route('/')
def home():
    return render_template('home.html')

# Função para usar no user_loader do login_manager no app.py
def user_loader_funcao(id):
    usuario = db.session.query(User).filter_by(id=id).first()
    return usuario

# Rota para registrar o Usuario
@controller_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        novo_usuario = User(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        login_user(novo_usuario)

        return redirect(url_for('controller_bp.home'))

    return render_template('register.html')

# Rota para logar o Usuario
@controller_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = db.session.query(User).filter_by(email=email, senha=senha).first()
        if not usuario:
            return render_template('login.html')

        login_user(usuario)
        return redirect(url_for('controller_bp.home'))
        
    return render_template('login.html')
        
# Possivel Rota para adotar o Animal
@controller_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('controller_bp.home'))

@controller_bp.route('/user')
@login_required
def user():
    return render_template('user.html', nome=current_user.nome)
    

