from flask import Flask
#creation d'une instance de la classe Flask
app = Flask(__name__)
#creation decorator qui permet de lancer la fonction helloword
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"