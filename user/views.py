from django.forms import model_to_dict
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User

def joinform(request):
    return render(request,'user/joinform.html')

def join(request):

    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    #models.insert((name,email,password,gender))
    user.save()


    return HttpResponseRedirect('/user/joinsuccess')


def joinsuccess(request):
    return render(request,'user/joinsuccess.html')

def loginform(request):
    return render(request, 'user/loginform.html')

def login(request):
    #user = models.get(email, password)
    results = User.objects.filter(email=request.POST['email']).filter(password=request.POST['password'])

    #로그인 실패
    if len(results) == 0:
        return HttpResponseRedirect('/user/loginform?result=fail')

    #로그인 성공
    authuser = results[0]
    request.session['authuser'] = model_to_dict(authuser)

    #main으로 리다이렉트
    return HttpResponseRedirect('/')

def modifyform(request):
    authuser = request.session['authuser']
    data = {'user':authuser}
    return render(request, 'user/modifyform.html',data)

def modify(request):
    authuser = request.session['authuser']

    auth_userid = User.objects.get(id=authuser.get('id'))
    auth_userid.password = request.POST['password']
    auth_userid.gender = request.POST['gender']
    #models.insert((name,email,password,gender))
    auth_userid.save()


    return HttpResponseRedirect('/user/modifysuccess')


def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')


def checkemail(request):
    results = User.objects.filter(email=request.GET['email'])
    result = {'result':len(results) == 0 } # true : not exist, false : exist
    return JsonResponse(result)

def modifysuccess(request):
    authuser = request.session['authuser']
    data = {'user':authuser}
    return HttpResponseRedirect('/user/modifyform', data)