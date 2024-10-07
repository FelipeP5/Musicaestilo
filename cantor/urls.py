from django.urls import path
from .views import listar_cantor, cadastrar_cantor, editar_cantor, excluir_cantor

urlpatterns = [
    path('', listar_cantor, name='listar_cantor'),
    path('cadastrar/', cadastrar_cantor, name='cadastrar_cantor'),
    path('editar/<int:id>/', editar_cantor, name= 'editar_cantor'),
    path('excluir/<int:id>/', excluir_cantor, name= 'excluir_cantor')
]