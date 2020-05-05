from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def template():
    return render_template("pokemon.html")

@app.route('/pikachu', methods = ["POST"])
def pikachu():
    return render_template("pikachu.html")

@app.route('/charzard', methods = ["POST"])
def charzard():
    return render_template("charzard.html")

@app.route('/charzard/flamethrower', methods = ["POST"])
def flamethrower():
    return render_template("flamethrower.html")

@app.route('/charzard/fly', methods = ["POST"])
def fly():
    return render_template("fly.html")

if __name__ == '__main__':
    app.run(debug=True)