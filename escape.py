from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route("/")
def Bienvenue():
    return f"Hello,bienvenue!"

@app.route("/<name>")
def hello(name):
     return f"Hello, <script>alert('bad')</script>!"
@app.route("/i")
def hello_i():
     i = 2
     return f"Hello, {i}"
app.run()