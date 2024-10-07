from django.shortcuts import render, redirect, get_object_or_404
from cantor.forms import CantorForm
from cantor.models import Cantor

def listar_cantor(request):
    cantores = Cantor.objects.all()
    return render(request, 'listar_cantor.html', {'cantores': cantores})

def cadastrar_cantor(request):
    if request.method == "POST":
        form = CantorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cantor')
    else:
        form = CantorForm()
    return render(request, 'form_cantor.html', {'form': form})

def editar_cantor(request, id):
    cantor = get_object_or_404(Cantor, id=id)
    if request.method == "POST":
        form = CantorForm(request.POST, instance=cantor)
        if form.is_valid():
            form.save()
            return redirect('listar_cantor')
    else:
        form = CantorForm(instance=cantor)
    return render(request, 'form_cantor.html', {'form': form})

def excluir_cantor(request, id):
    cantor = get_object_or_404(Cantor, id=id)
    if request.method == "POST":
        cantor.delete()
        return redirect('listar_cantor')
    return render(request, 'confirmar_ex_cantor.html', {'cantor': cantor})
