from django.urls import path
from .views import *

urlpatterns = [
    path('adicionar_apostilas/', adicionar_apostilas, name='adicionar_apostilas'),
    path('apostila/<int:id>/', apostila, name='apostila'),
    path('avaliacao_apostila/<int:id>/', avaliacao_apostila, name='avaliacao_apostila'),
]
