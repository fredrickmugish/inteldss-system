from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Disruptor
from .models import Team
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('user_panel')
    else:
         
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Account created for ' +user)
               return redirect('login')
        context = {'form':form}
        return render(request, 'register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('user_panel')
    else:
         
        if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(request, username=username, password=password)
         
         if user is not None:
              login(request, user)
              return redirect('user_panel')
         else:
              messages.info(request, 'Username OR password is incorrect')
              
    context= {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def user_panel(request):
     return render(request, 'userpanel.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def data_coll(request):
    return render(request, 'data_coll.html')

def dash(request):
    return render(request, 'dashboard.html')

def disruption(request):
    disruptor = Disruptor.objects.all()
    context = {'disruptors': disruptor}
    return render(request, 'disruption.html', context)

def data_analysis(request):
    return render(request, 'data_analysis.html')

def team(request):
    member = Team.objects.all()
    context = {'members':member}
    return render(request, 'team.html', context)


