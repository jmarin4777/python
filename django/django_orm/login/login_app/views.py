from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def root(request):
    return render(request, "index.html")

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    myvars = {
        "user": user
    }
    return render(request, "success.html", myvars)

# *****************************************************************
def register(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
        salt = bcrypt.gensalt()
        hash_pw = bcrypt.hashpw(request.POST['pw'].encode(), salt).decode()
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=
        request.POST['email'], password=hash_pw, salt=salt.decode(), birthday=request.POST['birthday'])
        request.session['user_id'] = user.id
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user:
            user = user[0]
            salt = user.salt.encode()
            # print(salt.decode())
            hash_pw = bcrypt.hashpw(request.POST['pw'].encode(), salt).decode()
            # print(hash_pw)
            # print(user.password)
            # print(hash_pw == user.password)
            # print(bcrypt.checkpw(hash_pw.encode(), user.password.encode()))
            if bcrypt.checkpw(request.POST['pw'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/success')
        messages.error(request, "Email or password is incorrect", extra_tags="Login")
        return redirect('/')
    return redirect('/')

def logout(request):
    request.session.clear()
    messages.error(request, "Successfully logged out", extra_tags="Login")
    return redirect('/')