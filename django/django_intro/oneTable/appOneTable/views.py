from django.shortcuts import render, redirect
from .models import Dungeon, Prisoner

# Create your views here.
def root(request):
    # ids=[]
    # names=[]
    # prisoners=[]
    # locations=[]
    # for i in Dungeon.objects.all():
    #     ids.append(i.id)
    #     names.append(i.name)
    #     prisoners.append(i.prisoners)
    #     locations.append(i.location)

    myvars = {
        # "ids": ids,
        # "names": names,
        # "prisoners": prisoners,
        # "locations": locations,
        "db": Dungeon.objects.all(),
        "pr": Prisoner.objects.all(),
    }
    # print(ids,'\n',names,'\n',prisoners,'\n',locations)
    return render(request, 'index.html', myvars)

def addDungeon(request):
    Dungeon.objects.create(name=request.POST['name'], num_people_inside=
    int(request.POST['num_people_inside']), location=request.POST['location'])
    return redirect('/')

def addPrisoner(request):
    Prisoner.objects.create(first_name=request.POST['first_name'], last_name=
    request.POST['last_name'], dungeon=Dungeon.objects.get(id=request.POST['dungeon']))
    x = Dungeon.objects.get(id=request.POST['dungeon'])
    x.num_people_inside += 1
    x.save()
    return redirect('/')

def delete(request, i):
    Dungeon.objects.get(id=i).delete()
    return redirect('/')

def dislike(request, j):
    x = Prisoner.objects.get(id=j)
    y = Dungeon.objects.get(id=request.POST['dislikes'])
    if x not in y.prisoner_dislikes.all():
        x.dislikes.add(y)
    else: print(f"{x.first_name} {x.last_name} already disliked {y.name}!")
    return redirect('/')