# chat/views.py
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType,ContentTypeManager
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")


@login_required(login_url='userlogin')
def room(request, room_name):
    return render(request, 'cartoon.html',{'room_name': room_name})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('userlogin')
