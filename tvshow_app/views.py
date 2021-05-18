from django.shortcuts import redirect, render
from .models import Show

def index(request):
    context= {
        "shows": Show.objects.all(),
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'add_show.html')


def create(request):
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    desc = request.POST['desc']
    Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
    return redirect('/shows')


def show_info(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, 'show_info.html', context)

def edit(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)

def update(request, id):
    show_update = Show.objects.get(id=id)
    show_update.title = request.POST['title']
    show_update.network= request.POST['network']
    show_update.release_date = request.POST['release_date']
    show_update.desc= request.POST['desc']
    show_update.save()
    return redirect('/shows')



def delete(request, id):
    show_delete = Show.objects.get(id=id)
    show_delete.delete()
    return redirect('/shows')
