from django.shortcuts import render, redirect
from .models import Show
from .forms import addShow
from django.contrib import messages

# Create your views here.
def root(request):
    return redirect('/shows')

def shows(request):
    myvars = {
        "shows": Show.objects.all(),
    }
    return render(request, "shows.html", myvars)

def new(request):
    myvars = {
        "form": addShow(),
    }
    return render(request, "new.html", myvars)

def add(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        errors = Show.objects.validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/shows/new')
        title, network, release_date, desc = request.POST['title'], request.POST['network'], request.POST['release_date'], request.POST['desc']
        newShow = Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
        id = newShow.id
        url = f"/shows/{id}"
    else:
        # print(request.POST)
        url = "/shows"
    return redirect(url)

def displayShow(request, id):
    show = Show.objects.get(id=id)
    myvars = {
        "show": show,
    }
    return render(request, "show.html", myvars)

def edit(request, id):
    myvars = {
        "show": Show.objects.get(id=id),
    }
    print(myvars['show'].updated_at)
    return render(request, "edit.html", myvars)

def editShow(request):
    show_id = int(request.POST['id'])
    if request.method == "POST":
        errors = Show.objects.edit_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            url = f"/shows/{show_id}/edit"
        else:
            show = Show.objects.get(id=show_id)
            for k, v in request.POST.items():
                if k != 'id' and k != 'csrfmiddlewaretoken' and v != '':
                    setattr(show, k, v)
            show.save()
            url = f"shows/{show_id}"
    return redirect(url)

def delete(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')
