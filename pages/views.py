from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def vols(request):
    context = {"vols_page": "active"} # new info here
    return render(request, 'pages/vols.html', context)
def direct(request):
    context = {"direct_page": "active"} # new info here
    return render(request, 'pages/direct.html', context)
def meteo(request):
    context = {"meteo_page": "active"} # new info here
    return render(request, 'pages/meteo.html', context)

def contact(request):
    context = {"contact_page": "active"} # new info here
    return render(request, 'registration/login.html', context)

def sitac(request):
    context = {"sitac_page": "active"} # new info here
    return render(request, 'pages/sitac.html', context)

def index(request):
    context = {"index_page": "active"} # new info here
    return render(request, 'pages/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
            login(request, user)
            return redirect('vols')
    else :
        form = UserCreationForm()
    context = { "form" : form }
    return render(request, 'pages/registration.html', context)
