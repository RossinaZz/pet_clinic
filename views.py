from cgitb import html
from multiprocessing.connection import Client
from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.models import Pets
from AppBlog.forms import ClientFormulario



def pets(request):

    return render(request,"AppBlog/pets.html")

def veterinary(request):

    return render(request,"AppBlog/veterinary.html")

def clienteFormulario(request):

    return render(request,"AppBlog/clientFormulario.html")
def client(request):

    return render(request,"AppBlog/client.html")

def inicio(request):

    return render(request,"AppBlog/inicio.html")

def cursoFormulario(request):

    if request.method == "POST" :

        miFormulario = ClientFormulario(request.POST)

        if miFormulario.is_valid():       #NO ME APARECE EN AMARILLO

            informacion= miFormulario.clean_data     #NO ME APARECE EN CELESTE

            client= client(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], numerocliente=informacion["numerocliente"])

            client.save()     #NO ME APARECE EN AMARILLO

            return render(request, "AppBlog/Inicio.html")

    else: miFormulario = ClientFormulario()
    
    return render(request, "AppBlog/ClientFormulario.html", {"miFormulario": miFormulario})

def busquedaNumeroCliente(request):

    return render(request,"AppBlog/busquedaNumeroCliente.html")

def buscar(request):

    respuesta=f"Buscando Numero del Cliente {request.GET ['NumeroCliente' ]}"

    if request.GET['NumeroCliente']:

        NumeroCliente=request.GET['NumeroCliente']
        clients= Client.objects.filter(client_icontains=client)   #NO ME APARACE CLIENT EN COLOR VERDE NI OBJECTS EN CELESTE NI FILTER EN AMARILLO
        return render(request, "AppBlog/resultadosBusqueda.html", {"clients": clients})
         #NO ME SALTA EN COLOR CELESTE

      
    return HttpResponse(respuesta)
    


