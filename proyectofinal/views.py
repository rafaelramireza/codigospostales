
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from .models import CodigoPostal

def index(request):
    """
    Vista para la página de inicio y búsqueda principal.
    
    Esta vista renderiza la plantilla 'index.html' y muestra la lista de estados y los resultados de la búsqueda.
    Si se realiza una solicitud POST, obtiene el estado, municipio y asentamiento y ejecuta el procedimiento almacenado
    'buscar_por_estado_municipio_asentamiento' para buscar por estado, municipio y asentamiento.
    """
    estados = CodigoPostal.objects.values_list('d_estado', flat=True).distinct()
    results = None
    if request.method == 'POST':
        estado = request.POST.get('nombre_estado')
        municipio = request.POST.get('nombre_municipio')
        asentamiento = request.POST.get('nombre_asentamiento')
        results = execute_stored_procedure('buscar_por_estado_municipio_asentamiento', estado, municipio, asentamiento)
    print(results)
    return render(request, 'index.html', {'estados': estados, 'results': results})

def execute_stored_procedure(procedure_name, *args):
    """
    Función para ejecutar procedimientos almacenados en la base de datos.
    
    Esta función recibe el nombre del procedimiento almacenado y los argumentos necesarios para ejecutarlo.
    Utiliza la conexión a la base de datos y el cursor para llamar al procedimiento almacenado y obtener los resultados.
    Devuelve los resultados obtenidos.
    """
    with connection.cursor() as cursor:
        cursor.callproc(procedure_name, args)
        results = cursor.fetchall()
    return results

def buscar_por_codigo_postal(request):
    """
    Vista para buscar por código postal.
    
    Esta vista renderiza la plantilla 'index.html' y muestra los resultados de la búsqueda por código postal.
    Si se realiza una solicitud POST, obtiene el código postal y ejecuta el procedimiento almacenado
    'buscar_por_codigo_postal' para buscar por código postal.
    """
    if request.method == 'POST':
        codigo_postal = request.POST.get('codigo_postal')
        results = execute_stored_procedure('buscar_por_codigo_postal', codigo_postal)
        return render(request, 'index.html', {'results': results})
    else:
        return render(request, 'index.html')

def buscar_por_asentamiento(request):
    """
    Vista para buscar por asentamiento.
    
    Esta vista renderiza la plantilla 'index.html' y muestra los resultados de la búsqueda por asentamiento.
    Si se realiza una solicitud POST, obtiene el nombre del asentamiento y ejecuta el procedimiento almacenado
    'buscar_por_asentamiento' para buscar por asentamiento.
    """
    if request.method == 'POST':
        nombre_asentamiento = request.POST.get('nombre_asentamiento')
        results = execute_stored_procedure('buscar_por_asentamiento', nombre_asentamiento)
        return render(request, 'index.html', {'results': results})
    else:
        return render(request, 'index.html')

def buscar_por_municipio(request):
    """
    Vista para buscar por municipio.
    
    Esta vista renderiza la plantilla 'index.html' y muestra los resultados de la búsqueda por municipio.
    Si se realiza una solicitud POST, obtiene el nombre del municipio y ejecuta el procedimiento almacenado
    'buscar_por_municipio' para buscar por municipio.
    """
    if request.method == 'POST':
        nombre_municipio = request.POST.get('nombre_municipio')
        results = execute_stored_procedure('buscar_por_municipio', nombre_municipio)
        return render(request, 'index.html', {'results': results})
    else:
        return render(request, 'index.html')

def buscar_por_estado(request):
    """
    Vista para buscar por estado.
    
    Esta vista renderiza la plantilla 'index.html' y muestra los resultados de la búsqueda por estado.
    Si se realiza una solicitud POST, obtiene el nombre del estado y ejecuta el procedimiento almacenado
    'buscar_por_estado' para buscar por estado.
    """
    if request.method == 'POST':
        nombre_estado = request.POST.get('nombre_estado')
        results = execute_stored_procedure('buscar_por_estado', nombre_estado)
        return render(request, 'index.html', {'results': results})
    else:
        return render(request, 'index.html')

def get_municipios_by_estado(request):
    """
    Vista para obtener municipios por estado.
    
    Esta vista recibe el estado como parámetro en la solicitud GET.
    Filtra los municipios por estado y devuelve la lista de municipios como una respuesta JSON.
    """
    estado = request.GET.get('estado')
    municipios = CodigoPostal.objects.filter(d_estado=estado).values_list('D_mnpio', flat=True).distinct()
    municipios_list = list(municipios)
    return JsonResponse(municipios_list, safe=False)

def get_asentamientos_by_municipio(request):
    """
    Vista para obtener asentamientos por municipio.
    
    Esta vista recibe el municipio como parámetro en la solicitud GET.
    Filtra los asentamientos por municipio y devuelve la lista de asentamientos como una respuesta JSON.
    """
    municipio = request.GET.get('municipio')
    asentamientos = CodigoPostal.objects.filter(D_mnpio=municipio).values_list('d_asenta', flat=True).distinct()
    asentamientos_list = list(asentamientos)
    return JsonResponse(asentamientos_list, safe=False)

def buscar_por_estado_municipio_asentamiento(request):
    """
    Vista para buscar por estado, municipio y asentamiento.
    
    Esta vista renderiza la plantilla 'index.html' y muestra los resultados de la búsqueda por estado, municipio y asentamiento.
    Si se realiza una solicitud POST, obtiene el estado y municipio, filtra los asentamientos por estado y municipio,
    y devuelve la lista de asentamientos como una respuesta JSON.
    """
    if request.method == 'POST':
        estado = request.POST.get('nombre_estado')
        municipio = request.POST.get('nombre_municipio')
        asentamientos = CodigoPostal.objects.filter(d_estado=estado, D_mnpio=municipio).values_list('d_asenta', flat=True).distinct()
        asentamientos_list = list(asentamientos)
        return JsonResponse(asentamientos_list, safe=False)
    else:
        return JsonResponse([], safe=False)
