from flask import render_template

class Controller:
    def home(self):
        return render_template('teste.html')