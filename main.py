from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash

from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm

from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired 

app = Flask(__name__)
bootstrap = Bootstrap(app)

#app = Flash(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'SUPER SECRETO'
todos = ['Comprar café', 'Comprar donas', 'Comprar sushi']

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.errorhandler(404)
def not_found(error):
	flash('Error', category='danger')
	return render_template('404.html', error= error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
	#user_ip = request.remote_addr
	#user_ip = request.cookies.get('user_ip')
	user_ip = session.get('user_ip')
	login_form = LoginForm()
	username = session.get('username')

	#return "Hello World Flask, tu IP es {}".format(user_ip)
	"""
	Para evitar pasar una a una las variables 
	
	return render_template('hello.html', user_ip=user_ip, todos=todos)
	
	se crea un contexto 
	"""
	#context = {'user_ip' : user_ip, "todos" : todos}
	context = {
		'user_ip' : user_ip, 
		"todos" : todos,
		'login_form' : login_form,
		'username': username
	}

	if login_form.validate_on_submit():
		username = login_form.username.data
		session['username'] = username

		flash('Nombre de usuario registrado corerctamente', category='success')
		return redirect(url_for('index'))
	# **context -> expandir el diccionario
	return render_template('hello.html', **context)

@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	session['user_ip'] = user_ip
	#response.set_cookie('user_ip', user_ip)

	return response
