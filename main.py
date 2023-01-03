from flask import Flask,render_template

app=Flask(__name__)
#creation de notrefonction home de type route

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

