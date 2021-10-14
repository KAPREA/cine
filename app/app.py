from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html') 

""" REALIZADO """
@app.route('/login')
def login():
    return render_template('login.html') 

""" REALIZADO """
@app.route('/register')
def signup():
    return render_template('register.html')

""" REALIZADO """
@app.route('/cartelera')
def cartelera():
    return render_template('cartelera.html')

"""NO REALIZAR """
@app.route('/cartelera_pelicula')
def cartelera_pelicula():
    return render_template('cartelera_pelicula.html')

@app.route('/pelicula')
def pelicula():
    return render_template('pelicula.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

""" REALIZADO """
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 
                       

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
