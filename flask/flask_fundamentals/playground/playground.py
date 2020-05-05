from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/play')
def template():
    return render_template("playground.html", x=0)
@app.route('/play/<int:x>')
def boxes(x):    
    return render_template("playground.html", x=x, color="deepskyblue")
@app.route('/play/<int:x>/<color>')
def color(x, color):
    return render_template("playground.html", x=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)