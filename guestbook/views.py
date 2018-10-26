from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook.models import Guestbook



def index(request):
    results = Guestbook.objects.all().order_by('-id')
    data = {'guestbook_list': results}
    return render(request, 'guestbook/index.html', data)

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.data = request.POST['data']
    guestbook.save()

    return HttpResponseRedirect("/guestbook/")

def delete(request):
    guestbook = Guestbook()
    guestbook.id = request.POST['id']
    guestbook.password = request.POST['password']
    guestbook.delete()

    return HttpResponseRedirect("/guestbook/")

def deleteform(request):
    guestbook = Guestbook()
    guestbook.id = request.GET['id']
    guestbook.data = {"id": guestbook.id}

    return render(request, 'guestbook/deleteform.html', guestbook.data)