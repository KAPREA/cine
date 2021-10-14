from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('cartelera.html') 

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

@app.route('/pelicula-detalles')
def pelicula():
    return render_template('cartelera-pelicula.html')

""" REALIZADO """
@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

""" REALIZADO """
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 
                       

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
