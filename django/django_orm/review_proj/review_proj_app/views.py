from django.shortcuts import render, redirect
from .models import User, Cat
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request, "index.html")

def homepage(request):
    myvars = {
        "user": User.objects.get(id=request.session['user_id']),
        "cats": Cat.objects.annotate(votes=Count('users_who_voted_for')).order_by('-votes')
        # "cats": Cat.objects.all(),
    }
    return render(request, "main_page.html", myvars) #<--- And inside of here!

def userProfile(request):
    myvars = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "one_user.html", myvars)

def catProfile(request, id):
    cat = Cat.objects.filter(id=id)
    if cat:
        cat = cat[0]
        myvars = {
        "cat": cat
        }
        return render(request, "one_cat.html", myvars)
    return redirect('/homepage')
# ************************************************************************************************************

def createUser(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            print("User's password entered was " + request.POST['password'])
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(name=request.POST['name'], password=hashed_pw)
            print("User's password has been changed to " + user.password)
    return redirect('/')

def login(request):
    if request.method == "POST":
        users_with_name = User.objects.filter(name=request.POST['name'])
        if users_with_name:
            user = users_with_name[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id #IMPORTANT!!!
                return redirect('/homepage')
            else:
                print("Password didn't match")
                messages.error(request, "Incorrect name or password")
        else:
            print("Name not found")
            messages.error(request, "Incorrect name or password")
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def createCat(request):
    #Logic to create a Cat, you should validate!
    if request.method == "POST":
        errors = Cat.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
        else:
            owner = User.objects.get(id=request.session['user_id'])
            Cat.objects.create(name=request.POST['name'], owner=owner)
    return redirect('/homepage')

def deleteCat(request, id):
    if request.method == "POST":
        cat = Cat.objects.filter(id=id)
        if cat:
            cat = cat[0]
            user = User.objects.get(id=request.session['user_id'])
            if cat.owner == user:
                cat.delete()
    return redirect('/homepage')

def voteCat(request, id):
    if request.method == "POST":
        cat = Cat.objects.filter(id=id)
        if cat:
            cat = cat[0]
            user = User.objects.get(id=request.session['user_id'])
            if cat.users_who_voted_for.all().filter(id=user.id):
                cat.users_who_voted_for.remove(user)
            else:
                cat.users_who_voted_for.add(user)
    return redirect('/homepage')