from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")
@app.route('/tell_secret', methods = ["POST"]) #POST route, sending info
def secret():
    print(request.form['secret'])
    return render_template("secret.html", secret=request.form['secret']) #there is another way to do this

if __name__ == '__main__':
    app.run(debug=True)