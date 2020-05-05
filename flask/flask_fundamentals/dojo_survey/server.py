from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def template():
    return render_template("dojo_survey.html")

@app.route('/result', methods = ["POST"])
def form():
    print("*"*80)
    print(request.form)
    print(request.form.getlist('checkbox'))
    return render_template("result.html", name = request.form['name'],
    location = request.form['location'], language = request.form['language'],
    comment = request.form['comment'], radio = request.form['radio'], checkbox = request.form.getlist('checkbox'))

if __name__ == '__main__':
    app.run(debug=True)
