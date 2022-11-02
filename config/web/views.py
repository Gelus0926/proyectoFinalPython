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

    return render(request,'menuplatos.html', data)

def Empleados(request):

    formularioPersonal=FormularioPersonal()

    data={
        'formularioPersonal':formularioPersonal
    }

    return render(request,'registroempleados.html', data)