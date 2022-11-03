from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos

from web.formularios.formularioPersonal import FormularioPersonal

# Create your views here.

#Las vistas en django son los CONTROLADORES
#Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def Platos(request):

    #Esta vista va a utilizar un formulario de django 
    #DEBO CREAR ENTONCES UN OBJETO DE LA CLASE FormularioPlatos()
    formulario=FormularioPlatos()

    #CREAMOS UN DICCIONARIO PARA ENVIAR EL FORMULARIO AL HTML(TEMPLATE)
    data={
        'formulario':formulario
    }

    #PREGUNTAMOS SI EXISTE ALGUNA PETICIÓN DE TIPO POST ASOCIADA A LA VISTA 
    if request.method=='POST':
        #se deberian capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosDelPlato=datosDelFormulario.cleaned_data
            print(datosDelFormulario)
            print(datosDelPlato)


    return render(request,'menuplatos.html', data)

def Empleados(request):

    formularioPersonal=FormularioPersonal()

    data={
        'formularioPersonal':formularioPersonal
    }

    #PREGUNTAMOS SI EXISTE ALGUNA PETICIÓN DE TIPO POST ASOCIADA A LA VISTA 
    if request.method=='POST':
        #se deberian capturar los datos del formulario
        datosFormulario=FormularioPersonal(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosFormulario.is_valid():
            #capturamos la data
            datosEmpleados=datosFormulario.cleaned_data
            print(datosFormulario)
            print(datosEmpleados)

    return render(request,'registroempleados.html', data)