from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def root(request):
    myvars = {
        "bk": Book.objects.all(),
    }
    return render(request, "index.html", myvars)

def addBook(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def displayBook(request, id):
    bk = Book.objects.get(id=int(id))
    myvars = {
        "title": bk.title,
        "id": int(id),
        "desc": bk.desc,
        "authors": bk.authors.all(),
        "ar": Author.objects.all(),
    }
    return render(request, "book.html", myvars)

def addAuthorToBook(request, id):
    bk = Book.objects.get(id=int(id))
    author = Author.objects.get(id=int(request.POST['author']))
    bk.authors.add(author)
    url = f"/books/{int(id)}"
    return redirect(url)

def authors(request):
    myvars = {
        "authors": Author.objects.all(),
    }
    return render(request, "authors.html", myvars)

def addAuthor(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('/authors')

def displayAuthor(request, id):
    author = Author.objects.get(id=int(id))
    myvars = {
        "first_name": author.first_name,
        "last_name": author.last_name,
        "id": author.id,
        "notes": author.notes,
        "books": author.books.all(),
        "bk": Book.objects.all(),
    }
    return render(request, "author.html", myvars)

def addBookToAuthor(request, id):
    author = Author.objects.get(id=int(id))
    bk = Book.objects.get(id=int(request.POST['book']))
    author.books.add(bk)
    url = f"/authors/{int(id)}"
    return redirect(url)