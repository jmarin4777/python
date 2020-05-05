from django.shortcuts import render, redirect
import random
from datetime import datetime
# Create your views here.
def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['act'] = ""
    myvars = {
        'gold': request.session['gold'],
        'act': request.session['act']
    }
    print(request.session['gold'])
    return render(request, "ninjaGold.html", myvars)

def process(request):
    if request.POST['gold'] == 'farm':
        farm = random.randint(10,20)
        request.session['gold'] += farm
        request.session['act'] = f"<p class='green'>Earned {farm} gold from the farm! ({datetime.now()})</p>\n" + request.session['act']       
    if request.POST['gold'] == 'cave':
        cave = random.randint(5,10)
        request.session['gold'] += cave
        request.session['act'] = f"<p class='green'>Earned {cave} gold from the cave! ({datetime.now()})</p>\n" + request.session['act']        
    if request.POST['gold'] == 'house':
        house = random.randint(2,5)
        request.session['gold'] += house
        request.session['act'] = f"<p class='green'>Earned {house} gold from the house! ({datetime.now()})\n</p>" + request.session['act']        
    if request.POST['gold'] == 'casino':
        if request.session['gold'] == 0:
                request.session['act'] = "<p>You don't have any money to gamble!</p>" + request.session['act']
                return redirect('/')
        if random.random() < 0.5:
            casino = random.randint(0,50)
            request.session['gold'] += casino
            request.session['act'] = f"<p class='green'>Earned {casino} gold from the casino! ({datetime.now()})\n</p>" + request.session['act']        
        else:
            if request.session['gold'] < 51:
                casino = random.randint(0,request.session['gold'])
            else:
                casino = random.randint(0,50)
            request.session['gold'] -= casino
            request.session['act'] = f"<p class='red'>Lost {casino} gold from the casino. :( ({datetime.now()})</p>" + request.session['act']        
    if request.POST['gold'] == 'reset':
        request.session.clear()
    print(request.POST['gold'])
    return redirect('/')