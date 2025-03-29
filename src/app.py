from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask import redirect, url_for, render_template, request, flash
from database import Database, Config
from cryptograph import Cryptograph
from functools import wraps
from flask import jsonify

import os


os.system('clear')
database = Database()
cryptograph = Cryptograph()
login_manager = LoginManager(Config.app)
login_manager.login_view = 'login'
app = Config.app


def require_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if current_user.role == 'admin':
            return f(*args, **kwargs)
        else:
            return jsonify({'error': 'Invalid Authorization'}), 401
    return wrapper


@login_manager.user_loader
def load_user(user_id):
    user = database.getUser(user_id)

    if user[0] != True:
        if user[0] == True:
            user = user[1]
            return user
        return None
    else:
        return user[1]


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internalServerError(error):
    return render_template('500.html', error=error), 501


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return render_template('index.html')
        else:
            return redirect(url_for('login'))
    else:
        ...


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        success, user = database.getUser(email)
        if success == True:
            if cryptograph.decrypt(user.Password, password) == True:
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Invalid Credentials')
                return redirect(url_for('login'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        success, user = database.getUser(email)
        if success == True:
            flash('User already exists')
            return redirect(url_for('login'))
        else:
            user = database.createUser(email, password)
            if user != None:
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Error creating user')
                return redirect(url_for('register'))
    else:
        return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)