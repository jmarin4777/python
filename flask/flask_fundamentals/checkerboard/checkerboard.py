from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def template1():
    return render_template("checkerboard.html", x=8, y=8)
@app.route('/<int:y>')
def template2(y):
    return render_template("checkerboard.html", x=8, y=y)
@app.route('/<int:x>/<int:y>')
def template3(x, y):
    return render_template("checkerboard.html", x=x, y=y)
if __name__ == '__main__':
    app.run(debug=True)