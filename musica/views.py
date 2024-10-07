from django.shortcuts import render, redirect, get_object_or_404
from musica.form import MusicaForm
from musica.models import Musica

def listar_musica(request):
    musicas = Musica.objects.all()
    return render(request, 'listar_musica.html', {'musicas': musicas})

def cadastrar_musica(request):
    if request.method == "POST":
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_musica')
    else:
        form = MusicaForm()
    return render(request, 'form_musica.html', {'form': form})

def editar_musica(request, id):
    musica = get_object_or_404(Musica, id=id)
    if request.method == "POST":
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('listar_musica')
    else:
        form = MusicaForm(instance=musica)
    return render(request, 'form_musica.html', {'form': form})

def excluir_musica(request, id):
    musica = get_object_or_404(Musica, id=id)
    if request.method == "POST":
        musica.delete()
        return redirect('listar_musica')
    return render(request, 'confirmar_ex_musica.html', {'musica': musica})

