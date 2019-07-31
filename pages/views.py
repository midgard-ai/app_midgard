from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
    if request.method == 'GET':
        form = AuthentificationForm()
        context = {"contact_page": "active"} # new info here
        return render(request, 'pages/contact.html', context)
    else:
        form = AuthentificationForm(data=request.POST)
        return render(request, "pages/login.html")

def sitac(request):
    context = {"sitac_page": "active"} # new info here
    return render(request, 'pages/sitac.html', context)
