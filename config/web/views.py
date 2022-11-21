from ast import For
from django.shortcuts import render

from web.formularios.formulariosPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos
from web.models import Empleados
# Create your views here.

#Todas las vistas son funciones de python
def Home(request):
    return render(request,'home.html')
    
    # Esta vista va a utilizar un formulario de Django, debo crear entonces un objeto de la clase FormularioPlatos
def PlatosVista(request):
    # Rutiina para la consulta d eplatos
    platosConsultados=Platos.objects.all()
    print(platosConsultados)

    formulario=FormularioPlatos()
    
    #Creamos un diccionario para enviar el formulario al html(template)
    data={
        'formulario':formulario,
        'bandera':False,
        'platos':platosConsultados
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
                data["bandera"]=True
                print("Exito guardando")
            except Exception as error:
                print("upsss", error)
                data["bandera"]=False
    
    return render(request,'menuPlatos.html',data)

    #Vamos a proceder a crear el fomrulario para los empleados
def EmpleadosVista(request):
    empleadosConsultados=Empleados.objects.all()
    print(empleadosConsultados)

    formulario=FormularioEmpleados()
    data={
        'formulario':formulario,
        'bandera':False,
        'empleados':empleadosConsultados
    }
    if request.method=="POST":
        datosFormulario=FormularioEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios),

            empleadoNuevo=Empleados(
                nombre=datosLimpios["nombre"],
                imagen=datosLimpios['imagen'],
                salario=datosLimpios["salario"],
                direccion=datosLimpios["direccion"],
                telefono=datosLimpios["telefono"],
                tipoEmpleado=datosLimpios["tipoEmpleado"]
            )
            #Llevando los datos a la db
            try:
                empleadoNuevo.save()
                data["bandera"]=True
                print("Empleado guardado con éxito")
            except Exception as error:
                print("se jodió esto", error)
                data["bandera"]=False
    return render(request,'registroEmpleados.html',data)