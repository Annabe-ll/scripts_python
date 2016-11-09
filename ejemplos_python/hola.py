from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

"""
@route('/')
def index():
    return template('<b>Hola world</b>!')

"""

run(host='localhost', port=9000)