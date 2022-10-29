from ast import For
from django.shortcuts import render

from web.formularios.formulariosPlatos import FormularioPlatos

# Create your views here.

#Todas las vistas son funciones de python
def Home(request):
    return render(request,'home.html')
    
    # Esta vista va a utilizar un formulario de Django, debo crear entonces un objeto de la clase FormularioPlatos
def Platos(request):
    formulario=FormularioPlatos()
    
    #Creamos un diccionario para enviar el formulario al html(template)
    data={
        'formulario':formulario
    }
    return render(request,'menuPlatos.html',data)


def Empleados(request):
    return render(request,'registroEmpleados.html')