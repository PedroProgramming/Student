from django.urls import path
from .views import *

urlpatterns = [
    path('novo_flashcard/', novo_flashcard, name="novo_flashcard"),
    path('deletar_flashcard/<int:id>/', deletar_flashcard, name='deletar_flashcard'),
    path('iniciar_desafio/', iniciar_desafio, name='iniciar_desafio'),
    path('listar_desafio/', listar_desafio, name='listar_desafio'),
    path('desafio/<int:id>/', desafio, name='desafio'),
    path('responder_flashcard/<int:id>/', responder_flashcard, name='responder_flashcard'),
    path('relatorio/<int:id>/',relatorio, name='relatorio')

]
