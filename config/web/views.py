from django.shortcuts import render
from django.shortcuts import redirect

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEdicionPlatos import FormularioEdicionPlatos

from web.formularios.formularioPersonal import FormularioPersonal

from web.models import Platos
from web.models import Empelado


# Create your views here.

#Las vistas en django son los CONTROLADORES
#Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def MenuPlatos(request):

    platosConsultados=Platos.objects.all()

    formulario=FormularioEdicionPlatos()

    diccionarioEnvio={
        'platos':platosConsultados,
        'formulario':formulario
    }

    return render(request, 'platos.html',diccionarioEnvio)

def EditarPlato(request,id):
    print(id)
    #Recibir los datos del formulario y editar mi plato
    if request.method=='POST':
        datosFormulario=FormularioEdicionPlatos(request.POST)
        if datosFormulario.is_valid():
            datosDelPlato=datosFormulario.cleaned_data
            try:
                Platos.objects.filter(pk=id).update(precio=datosDelPlato["precioPlato"])
                print("EXITO GUARDANDO LOS DATOS")

            except Exception as error:
                
                print("ERROR",error)

    return redirect('menu')


def Empleados(request):
    empleadosConsultados=Empelado.objects.all()

    diccionarioEnvio={
        'empleados':empleadosConsultados
    }

    return render(request, 'empleados.html',diccionarioEnvio)

def VistaPlatos(request):

    #Esta vista va a utilizar un formulario de django 
    #DEBO CREAR ENTONCES UN OBJETO DE LA CLASE FormularioPlatos()
    formulario=FormularioPlatos()

    #CREAMOS UN DICCIONARIO PARA ENVIAR EL FORMULARIO AL HTML(TEMPLATE)
    data={
        'formulario':formulario,
        'bandera':False
    }

    #PREGUNTAMOS SI EXISTE ALGUNA PETICIÓN DE TIPO POST ASOCIADA A LA VISTA 
    if request.method=='POST':
        #se deberian capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosDelPlato=datosDelFormulario.cleaned_data
            #Creamos un objeto de tipo MODELO PLATO
            platoNuevo=Platos(
                nombre=datosDelPlato["nombre"],
                fotografia=datosDelPlato["fotografiaPlato"],
                precio=datosDelPlato["precioPlato"],
                tipo=datosDelPlato["tipoPlato"],
                descripcion=datosDelPlato["descripcionPlato"]
            )
            #INTENTAMOS LLEVAR EL OBJETO PLATONUEVO A LA BD
            try:

                platoNuevo.save()
                data["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")

            except Exception as error:
                data["bandera"]=False
                print("ERROR",error)

    return render(request,'menuplatos.html', data)

def VistaEmpleados(request):

    formularioPersonal=FormularioPersonal()

    data={
        'formularioPersonal':formularioPersonal,
        'bandera':False
    }

    #PREGUNTAMOS SI EXISTE ALGUNA PETICIÓN DE TIPO POST ASOCIADA A LA VISTA 
    if request.method=='POST':
        #se deberian capturar los datos del formulario
        datosFormulario=FormularioPersonal(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosFormulario.is_valid():
            #capturamos la data
            datosEmpleados=datosFormulario.cleaned_data
            #Creamos un objeto de tipo MODELO EMPLEADO
            empleadoNuevo=Empleado(
                nombres_Empleado=datosEmpleados['nombres'],
                apellidos_Empleado=datosEmpleados['apellidos'],
                foto=datosEmpleados['foto'],
                cargo=datosEmpleados['cargo'],
                salario=datosEmpleados['salario'],
                contacto=datosEmpleados['contacto']
            )
            #INTENTAMOS LLEVAR EL OBJETO PLATONUEVO A LA BD
            try:

                empleadoNuevo.save()
                data["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")

            except Exception as error:
                data["bandera"]=False
                print("ERROR",error)

    return render(request,'registroempleados.html', data)