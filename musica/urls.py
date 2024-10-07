from django.urls import path
from .views import listar_musica, cadastrar_musica, editar_musica, excluir_musica

urlpatterns = [
    path('', listar_musica, name='listar_musica'),
    path('cadastrar/', cadastrar_musica, name='cadastrar_musica'),
    path('editar/<int:id>/', editar_musica, name= 'editar_musica'),
    path('excluir/<int:id>/', excluir_musica, name= 'excluir_musica')
]
