from django.urls import path
from . import views
urlpatterns = [
    path('meteo/', views.meteo, name='meteo'),
    path('about/', views.vols, name='vols'),
    path('', views.contact, name='contact'),
    path('direct/', views.direct, name='direct'),
    path('sitac/',views.sitac,name='sitac'),
]
