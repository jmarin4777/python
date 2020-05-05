from flask import Flask, render_template, request, session, redirect
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def root():
    if 'gold' not in session:
        session['gold'] = 0
        session['act'] = ""
    print(session['gold'])
    return render_template('ninja_gold.html', gold = session['gold'], act = session['act'])

@app.route('/process', methods = ['post'])
def process():
    if request.form['gold'] == 'farm':
        farm = random.randint(10,20)
        session['gold'] += farm
        session['act'] = f"<p class='green'>Earned {farm} gold from the farm! ({datetime.now()})</p>\n" + session['act']       
    if request.form['gold'] == 'cave':
        cave = random.randint(5,10)
        session['gold'] += cave
        session['act'] = f"<p class='green'>Earned {cave} gold from the cave! ({datetime.now()})</p>\n" + session['act']        
    if request.form['gold'] == 'house':
        house = random.randint(2,5)
        session['gold'] += house
        session['act'] = f"<p class='green'>Earned {house} gold from the house! ({datetime.now()})\n</p>" + session['act']        
    if request.form['gold'] == 'casino':
        if random.random() < 0.5:
            casino = random.randint(0,50)
            session['gold'] += casino
            session['act'] = f"<p class='green'>Earned {casino} gold from the casino! ({datetime.now()})\n</p>" + session['act']        
        else:
            if session['gold'] == 0:
                session['act'] = "<p>You don't have any money to gamble!</p>" + session['act']
                return redirect('/')
            elif session['gold'] < 51:
                casino = random.randint(0,session['gold'])
            else:
                casino = random.randint(0,50)
            session['gold'] -= casino
            session['act'] = f"<p class='red'>Lost {casino} gold from the casino. :( ({datetime.now()})</p>" + session['act']        
    if request.form['gold'] == 'reset':
        session.clear()
    print(request.form['gold'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)