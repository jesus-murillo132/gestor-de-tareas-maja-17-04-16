from flask import Flask, render_template, redirect, url_for, request

flask_app = Flask(__name__, template_folder='.')

@flask_app.route('/')
def home():
    return render_template('inicio.html')

@flask_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('tasks_page'))
    return render_template('formulario.html')

@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('tasks_page'))
    return render_template('inicio_de_sesion.html')

@flask_app.route('/recover', methods=['GET', 'POST'])
def recover():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('recuperar_contraseña.html')

@flask_app.route('/tasks')
def tasks_page():
    return render_template('gestor_de_tareas.html')

if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port=8000)
