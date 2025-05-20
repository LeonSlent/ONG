from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from model import User, Animal
from model import db, registrar_usuario, registrar_animal, login_usuario


# Cria o Blueprint
controller_bp = Blueprint('controller_bp', __name__, template_folder='../view/templates')

# Rota principal
@controller_bp.route('/')
def home():
    return render_template('home.html')

# Carrega o usuário a partir do ID salvo na sessão
def user_loader_funcao(id):
    usuario = db.session.query(User).filter_by(id=id).first()
    return usuario

# Rota para registrar o Usuario
@controller_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Chama a função do model para criar a instancia no banco de dados
        registrar_usuario()

        return redirect(url_for('controller_bp.home'))

    return render_template('register.html')

# Rota para logar o Usuario
@controller_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Chama a função do model para logar o usuario na sessão, se o login estiver incorreto, ele retorna para a rota de login novamente
        if login_usuario() is False:
            return render_template('login.html')
        
        return redirect(url_for('controller_bp.home'))
        
    return render_template('login.html')
        
# Rota para logout do usuario
@controller_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('controller_bp.home'))

# Rota para o perfil do usuario
@controller_bp.route('/user')
@login_required
def user():
    return render_template('user.html', nome=current_user.nome)

# Rota para cadastrar o animal
@controller_bp.route('/register_animal', methods=['GET', 'POST'])
@login_required
def register_animal():
    if request.method == 'POST':
        # Chama a função do model para criar a instancia no banco de dados
        registrar_animal()
        
        return redirect(url_for('controller_bp.home'))

    return render_template('register_animal.html')

