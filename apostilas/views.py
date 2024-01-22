from django.contrib import messages
from django.contrib.messages import constants
from .models import Apostila, ViewApostila, Avaliacao
from django.shortcuts import render, redirect, get_object_or_404

def adicionar_apostilas(request):
    if request.method == 'GET':
        apostilas = Apostila.objects.filter(user=request.user)
        views_totais = ViewApostila.objects.filter(apostila__user=request.user).count()
        context = {
            'apostilas': apostilas,
            'views_totais': views_totais,
        }
        return render(request, 'adicionar_apostilas.html', context)
    
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        arquivo = request.FILES['arquivo']
        apostila = Apostila(
            user=request.user,
            titulo=titulo,
            arquivo=arquivo
        )
        apostila.save()

        messages.add_message(request, constants.SUCCESS, 'Apostila adicionada com sucesso.')
        return redirect('/apostilas/adicionar_apostilas/')

def apostila(request, id):
    apostila = Apostila.objects.get(id=id)
    
    view = ViewApostila(
        ip=request.META['REMOTE_ADDR'],
        apostila=apostila,
    )
    view.save()

    views_totais = ViewApostila.objects.filter(apostila=apostila).count()
    views_unicas = ViewApostila.objects.filter(apostila=apostila).values('ip').distinct().count()

    context = {
        'apostila': apostila,
        'views_totais': views_totais,
        'views_unicas': views_unicas,
        'avaliacoes': Avaliacao.objects.filter(apostila=apostila),
        'avaliacao': Avaliacao.objects.filter(apostila=apostila, user=request.user)
    }
    return render(request, 'apostila.html', context)

def avaliacao_apostila(request, id):
    apostila = get_object_or_404(Apostila, id=id)
    avaliacao = Avaliacao(
        user=request.user,
        apostila=apostila,
        avaliacao=request.POST.get('avaliacao')
    )
    avaliacao.save()
    return redirect(f'/apostilas/apostila/{apostila.id}')