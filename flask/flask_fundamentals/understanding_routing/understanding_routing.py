from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<name>')
def say(name):
    return f"Hi {name}!"
@app.route('/repeat/<int:num>/<something>')
def repeat(num, something):
    return f"{something} "*num
@app.errorhandler(404)
def error_message(error):
    return "Sorry! No response. Try again."
if __name__ == "__main__":
    app.run(debug=True)