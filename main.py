from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)
#app = Flash(__name__, template_folder='../templates', static_folder='../static')
todos = ['Comprar café', 'Comprar donas', 'Comprar sushi']

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html', error= error)

@app.route('/hello')
def hello():
	#user_ip = request.remote_addr
	user_ip = request.cookies.get('user_ip')

	#return "Hello World Flask, tu IP es {}".format(user_ip)
	"""
	Para evitar pasar una a una las variables 
	
	return render_template('hello.html', user_ip=user_ip, todos=todos)
	
	se crea un contexto 
	"""
	context = {'user_ip' : user_ip, "todos" : todos}
	# **context -> expandir el diccionario
	return render_template('hello.html', **context)

@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	response.set_cookie('user_ip', user_ip)

	return response
