from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html') 

@app.route('/login')
def login():
    return render_template('login.html') 

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/cartelera')
def cartelera():
    return render_template('cartelera.html')

@app.route('/cartelera_pelicula')
def cartelera_pelicula():
    return render_template('cartelera.pelicula.html')

@app.route('/pelicula')
def pelicula():
    return render_template('pelicula.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 
                       

 

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
