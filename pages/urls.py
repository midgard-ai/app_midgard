from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('meteo/', views.meteo, name='meteo'),
    path('about/', views.vols, name='vols'),
    path('accounts/contact', views.contact, name='contact'),
    path('direct/', views.direct, name='direct'),
    path('sitac/',views.sitac,name='sitac'),
    path('', auth_views.LoginView.as_view(template_name='pages/login.html')),
    path('register/', views.register, name='register')
]
