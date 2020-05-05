from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def random_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    myvars = {
        "count": request.session['count'],
        "rand": get_random_string(length=14),
    }
    return render(request, "random_word.html", myvars)

def reset(request):
    request.session['count'] = 0
    return redirect('/random_word')