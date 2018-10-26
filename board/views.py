from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board
from user.models import User


def index(request):
    if request.method == 'GET':
        results = Board.objects.all().order_by('-group_no')
        data = {'board_list': results}
    return render(request, 'board/index.html', data)




def view(request):
    if request.method == 'GET':
        id = request.GET['id']
        results = Board.objects.get(id=id)
        data = {'board_list': results}
        results.hit += 1
        results.save()
        return render(request, 'board/view.html', data)


def write(request):
    return render(request, 'board/write.html')

def add(request):
    board = Board()
    board.title =request.POST['title']
    board.content = request.POST['content']
    # 그룹넘버 구하기
    g_no= Board.objects.aggregate(Max('group_no'))
    if(g_no['group_no__max'] == None):
        board.group_no = 1
    else:
        board.group_no = g_no['group_no__max'] + 1
    board.order_no = 1
    board.depth = 0
    authuser = request.session['authuser']
    auth_username = authuser.get('name')
    auth_user_id = authuser.get('id')
    board.user_name = auth_username
    board.user_id = auth_user_id
    board.save()

    return HttpResponseRedirect("/board/")


def modify(request):
    if request.method == 'GET':
        id = request.GET['id']
        results = Board.objects.get(id=id)
        data = {'board_data': results}
        return render(request, 'board/modify.html',data)

def mod(request):
    if request.method == 'POST':
        id = request.GET['id']
        results = Board.objects.get(id=id)
        results.title = request.POST['title']
        results.content = request.POST['content']
        results.save()
    return HttpResponseRedirect("/board/")

def delete(request):
    board = Board()
    board.id = request.GET['id']
    board.delete()
    return HttpResponseRedirect("/board/")

def reply(request):
    if request.method == 'GET':
        id = request.GET['id']
        results = Board.objects.get(id=id)
        data = {'board_data': results}
        return render(request, 'board/reply.html',data)


def reple(request):
    new = Board()
    if request.method == 'POST':
        id = request.GET['id']
        board= Board.objects.get(id=id)

        new.group_no = board.group_no
        new.title = request.POST['title']
        new.content = request.POST['content']
        new.order_no = board.order_no + 1
        new.depth = board.depth + 1

        authuser = request.session['authuser']
        auth_username = authuser.get('name')
        auth_user_id = authuser.get('id')

        new.user_name = auth_username
        new.user_id = auth_user_id
        new.save()

    return HttpResponseRedirect("/board/")