from django.urls import path
from .views import listar_estilo, cadastrar_estilo, editar_estilo, excluir_estilo

urlpatterns = [
    path('', listar_estilo, name='listar_estilo'),
    path('cadastrar/', cadastrar_estilo, name='cadastrar_estilo'),
    path('editar/<int:id>/', editar_estilo, name= 'editar_estilo'),
    path('excluir/<int:id>/', excluir_estilo, name= 'excluir_estilo')
]