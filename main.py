from flask import Flask,render_template

app=Flask(__name__)
#creation de notrefonction home de type route

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/login')
def connexion():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)

