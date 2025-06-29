from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, logout_user
from model import registrar_usuario, registrar_animal, login_usuario, listar_animais, animal_existente, processo_adocao, listar_adocoes, animal_indisponivel, animal_disponivel, alterar_status_adocao, tratamento_imagem
from datetime import datetime

# Cria o Blueprint
controller_bp = Blueprint('controller_bp', __name__, template_folder='../view/templates')

# Rota principal
@controller_bp.route('/')
def home():
    lista = listar_animais()
    return render_template('home.html', animais=lista)

# Rota para registrar o Usuario
@controller_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        data_nas_str = request.form.get('data_nas')
        cpf = request.form.get('cpf')
        # Converte string para datetime.date
        data_nas = datetime.strptime(data_nas_str, '%Y-%m-%d').date()
        # Chama a função do model para criar a instancia no banco de dados
        if registrar_usuario(nome, email, senha, data_nas, cpf) is False:
            return render_template('register.html')

        return redirect(url_for('controller_bp.home'))

    return render_template('register.html')

# Rota para logar o Usuario
@controller_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        # Chama a função do model para logar o usuario na sessão, se o login estiver incorreto, ele retorna para a rota de login novamente
        if login_usuario(email, senha) is False:
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
    lista = listar_adocoes()

    return render_template('user.html', current_user=current_user, adocoes=lista)

@controller_bp.route('/alterar_status/<adocao_id>', methods=['GET', 'POST'])
@login_required
def alterar_status(adocao_id):
    status = request.form.get('status')
    alterar_status_adocao(adocao_id, status)
    if status == 'cancelado':
        animal = animal_existente(adocao_id)
        animal_disponivel(animal)
        
    return redirect(url_for('controller_bp.user'))


# Rota para cadastrar o animal
@controller_bp.route('/register_animal', methods=['GET', 'POST'])
@login_required
def register_animal():
    if not current_user.is_funcionario():
        return redirect(url_for('controller_bp.home'))
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        genero = request.form['genero']
        especie = request.form['especie']
        descricao = request.form['descricao']
        imagem = request.files['imagem']

        nome_imagem = tratamento_imagem(imagem)
        # Chama a função do model para criar a instancia no banco de dados
        registrar_animal(nome, idade, genero, especie, descricao, nome_imagem)
        
        return redirect(url_for('controller_bp.user'))

# Rota do animal
@controller_bp.route('/animal/<animal_id>', methods=['GET', 'POST'])
@login_required
def animal_perfil(animal_id):
    # Verifica se o id do animal procurado existe, se não existir, o usuario é direcionado para a pagina home
    animal = animal_existente(animal_id)
    if not animal:
        return render_template('home.html')
    

    if request.method == 'POST':
        animal_indisponivel(animal)
        return redirect(url_for('controller_bp.adotar', animal_id=animal.id))
    
    lista = listar_animais()
    return render_template('animal.html', animal=animal, lista=lista)

@controller_bp.route('/adotar/<animal_id>')
@login_required
def adotar(animal_id):
    processo_adocao(animal_id, current_user.id)

    return redirect(url_for('controller_bp.user'))



