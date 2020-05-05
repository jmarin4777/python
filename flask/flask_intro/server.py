from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return "I've started my first web server!"
@app.route('/hello')
def hello():
    return "Hello"
@app.route('/hello/world')
def world():
    return "World!"
@app.route('/like/<int:num>')
def like(num):
    return f"I like the number {num}!"
    #return "I like the number " + num + "!" this doesn't work bc num gets cast as a string
@app.route('/template')
def template():
    return render_template("index.html", phrase="My name is Jeff!", characters=["Michael", "Dwight", "Jim"])
    #front_end_phrase = backend_value
if __name__ == "__main__":
    app.run(debug=True)