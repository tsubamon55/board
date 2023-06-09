from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required

from .models import BoardModel

# Create your views here.


def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html',  {'error': 'このユーザーは登録されています'})
        except Exception:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some': 100})
    if request.method == 'GET':
        return render(request, 'signup.html', {'some': 100})


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')


@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')
