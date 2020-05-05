from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    def suffix(day):
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        return suffix 

    x = datetime.now()
    month = x.strftime("%B")
    day = int(x.strftime("%d"))
    suffix = suffix(day)
    day = f"{day}{suffix}"
    year = x.strftime("%Y")
    hour = int(x.strftime("%I"))
    minute = x.strftime("%M")
    sec = x.strftime("%S")
    am_pm = x.strftime("%p")
    y = f"{month} {day}, {year} at {hour}:{minute}:{sec} {am_pm}"
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    id = request.form['student_id']
    sum = strawberry + raspberry + apple
    print(f"Charging {first_name} {last_name} for {sum} fruits")
    return render_template("checkout.html", strawberry = strawberry, 
    raspberry = raspberry, apple = apple, first_name = first_name, 
    last_name = last_name, id = id, sum = sum, y = y)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    