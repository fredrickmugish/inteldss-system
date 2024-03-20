from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               
    context = {'form':form}
    return render(request, 'register.html', context)
