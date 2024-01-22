from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro/', cadastro, name="cadastro"),
    path('login/', logar, name='login'),
    path('logout/', logout, name='logout'),
]
