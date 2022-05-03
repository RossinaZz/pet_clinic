from django.urls import path
from AppBlog import views

urlpatterns = [
    path('pets/',views.pets, name='Pets'),
    path('veterinary/',views.veterinary, name='Veterinary'),
    path('client/',views.client, name='Clients'),
    path('',views.inicio, name='Inicio'),
    path('clientFormulario/', views.clienteFormulario, name='clientFormulario'),
    path('busquedaNumeroCliente/', views.busquedaNumeroCliente, name='busquedaNumeroCliente'),
    path('buscar/', views.buscar)
]