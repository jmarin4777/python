from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages
import bcrypt
from django.db.models import Count

# Create your views here.
def root(request):
    
    return render(request, "index.html")

def quotes(request):
    if 'user_id' not in request.session:
        return redirect('/')
    myvars = {
        "quotes": Quote.objects.annotate(likes=Count('users_who_liked')).order_by('-likes'),
        "user": User.objects.get(id=request.session['user_id']),
    }
    return render(request, "quotes.html", myvars)

def displayUser(request, id):
    if "user_id" not in request.session:
        return redirect('/')
    user = User.objects.filter(id=id)
    if user:
        user = user[0]
        myvars = {
            "user": user
        }
        return render(request, "user.html", myvars)
    return redirect('/quotes')

def edit(request):
    if "user_id" not in request.session:
        return redirect('/')
    myvars = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "myAccount.html", myvars)
    
# ********************************************************************************************
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
        request.POST['email'], password=hash_pw, salt=salt.decode())
        request.session['user_id'] = user.id
        return redirect('/quotes')
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
                return redirect('/quotes')
        messages.error(request, "Email or password is incorrect", extra_tags="Login")
        return redirect('/')
    return redirect('/')

def logout(request):
    # GET and POST methods are allowed
    request.session.clear()
    messages.info(request, "Successfully logged out", extra_tags="Login")
    return redirect('/')

def addQuote(request):
    if request.method == "POST":
        errors = Quote.objects.validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/quotes')
        Quote.objects.create(author=request.POST['author'], quote=request.POST['quote'], user=User.objects.get(id=
        request.session['user_id']))
        messages.info(request, "Quote successfully added")
        return redirect('/quotes')
    return redirect('/')

def like(request, id):
    if request.method == "POST":
        quote = Quote.objects.filter(id=id)
        if quote:
            quote = quote[0]
            quote.users_who_liked.add(User.objects.get(id=request.session['user_id']))
        return redirect('/quotes')
    return redirect('/')

def editAccount(request):
    if request.method == "POST":
        errors = User.objects.editValidator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/edit')
        user = User.objects.get(id=request.session['user_id'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        messages.info(request, "Account information successfully updated")
        return redirect('/edit')
    return redirect('/')

def delete(request, id):
    if request.method == "POST":
        quote = Quote.objects.filter(id=id)
        if quote:
            quote = quote[0]
            user = User.objects.get(id=request.session['user_id'])
            if user == quote.user:
                quote.delete()
                messages.info(request, "Quote successfully deleted")
                return redirect('/quotes')
            return redirect('/quotes')
    return redirect('/')
