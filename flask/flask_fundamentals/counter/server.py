from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def root():
    if 'views' not in session:
        session['views'] = 0
    session['views'] += 1
    return render_template("counter.html")

@app.route('/increment_by_2', methods = ["POST"])
def increment_by_2():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 2
    return redirect('/')

@app.route('/increment', methods = ['POST'])
def increment():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += int(request.form['inc'])
    return redirect('/')

@app.route('/destroy_session', methods = ["POST"])
def destroy_session():
    session.pop('views')
    return redirect('/')

@app.route('/reset_counter', methods = ["POST"])
def reset_counter():
    session.pop('count')
    session['count'] = 0
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)