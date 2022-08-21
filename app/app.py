from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    #return "Hola mundo :v"
    cursos = ['Python', 'Sql', 'Vue.js']
    data = {
        'titulo':'Index333',
        'bienvenida':'Saludos!',
        'cursos':cursos,
        'numero_cursos':len(cursos)
    }
    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
