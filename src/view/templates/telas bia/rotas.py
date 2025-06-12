from flask import render_template

# home
#@app.route()
def home():
    return render_template(
        'homepage.html',
        title="Home",
        banner_title="UMA CAMPANHA ESPECIAL",
        banner_description="Uma seleção especial de peludinhos que buscam um lar para chamar de seu"
    )

# login
#@app.route()
def login():
    return render_template(
        'login_page.html',
        title="Login",
        banner_title="SEJA BEM VINDO!",
        banner_description=""
    )

# cadastro
#@app.route()
def cadastro():
    return render_template(
        'register_page.html',
        title="Cadastro",
        banner_title="SEJA BEM VINDO!",
        banner_description=""
    )

# perfil admin
#@app.route()
def admin():
    return render_template(
        'admin_profile.html',
        title="Perfil",
        banner_title="SEJA BEM VINDO!",
        banner_description=""
    )

# perfil usuário
#@app.route()
def user():
    return render_template(
        'user_profile.html',
        title="Perfil",
        banner_title="SEJA BEM VINDO!",
        banner_description=""
    )

# adotar animal
#@app.route()
def adocao():
    return render_template(
        'adopt_animal.html',
        title="Adoção",
        banner_title="UMA CAMPANHA ESPECIAL",
        banner_description="Uma seleção especial de peludinhos que buscam um lar para chamar de seu"
    )