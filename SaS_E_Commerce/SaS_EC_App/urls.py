from django.urls import path
from SaS_EC_App import views




urlpatterns = [
    path('', views.index , name='index'),
    path('registration', views.Registration, name ='registration'),
    path('login', views.Login, name ='login'),
]
