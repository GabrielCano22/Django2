from ast import For
from django.shortcuts import render

from web.formularios.formulariosPlatos import FormularioPlatos

from web.models import Platos
# Create your views here.

#Todas las vistas son funciones de python
def Home(request):
    return render(request,'home.html')
    
    # Esta vista va a utilizar un formulario de Django, debo crear entonces un objeto de la clase FormularioPlatos
def PlatosVista(request):
    formulario=FormularioPlatos()
    
    #Creamos un diccionario para enviar el formulario al html(template)
    data={
        'formulario':formulario
    }
    #Recibimos los datos del formulario
    if request.method=="POST":
        datosFormulario=FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios),
            #construir un diccionario de envio de datos haca la BD
            platoNuevo=Platos(
               nombre=datosLimpios["nombre"],
               descripcion=datosLimpios["descripcion"],
               fotografia=datosLimpios["fotografia"],
               precio=datosLimpios["precio"], 
               tipo =datosLimpios["tipo"]
            )
            #intentaré llevar mis datos a la db
            try:
                platoNuevo.save()
                print("Exito guardando")
            except Exception as error:
                print("upsss", error)
    
    return render(request,'menuPlatos.html',data)


def Empleados(request):
    return render(request,'registroEmpleados.html')