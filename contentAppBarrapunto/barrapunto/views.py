from django.shortcuts import render
from django.http import HttpResponse
from bp import obtenerFich
from models import Pages, Barrapunto
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

bp = {}

def update(request):
    bp = obtenerFich()
    for elem in bp:
        noticia = Barrapunto(title=elem, link=bp[elem])
        noticia.save()
    respuesta = "Fichero RSS cargado"
    return HttpResponse(respuesta)


def mostrarContenido(request):
    try:
        paginas = Pages.objects.all()
        respuesta = "<ul>"
        for pagina in paginas:
            respuesta += '<li><a href="/'+ str(pagina.id) + '">' + str(pagina.id) + ") " + pagina.name + ': ' + pagina.page + '</a></li>'
            #respuesta += '<li>' + pagina.name + ": " + pagina.page
        respuesta += "</ul>"
        return HttpResponse(respuesta)
    except ObjectDoesNotExist:
        respuesta = "Does not exist"
        return HttpResponse(respuesta)

def mostrarPagina(request, identificador):
    try:
        pagina = Pages.objects.get(id=int(identificador))
        respuesta = "<ul>"
        respuesta += '<li><a href:"' + pagina.name + '">' + pagina.page + '</a>'
        respuesta += "</ul>"
        try:
            barrapunto = Barrapunto.objects.all()
            for elem in barrapunto:
                respuesta += '<li><a href="'+ elem.link + '">' + elem.title + '</a></li>' + '\n'
            return HttpResponse(respuesta)
        except ObjectDoesNotExist:
            respuesta = "Does not exist"
            return HttpResponse(respuesta)
    except ObjectDoesNotExist:
        respuesta = "Does not exist"
        return HttpResponse(respuesta)


@csrf_exempt
def nuevoContenido(request, name, page):
    try:
        pagina = Pages(name=name, page=page)
        pagina.save()
        respuesta = "Nuevo contenido guardado con exito"
        return HttpResponse(respuesta)
    except ObjectDoesNotExist:
        respuesta = "Does not exist"
        return HttpResponse(respuesta)

def notfound(request):
    respuesta = "<ul>Usos de la aplicacion:"
    respuesta += "<li>La pagina principal te muestra todos los contenidos diponibles"
    respuesta += "<li>/(identificador): devuelve el contenido correspondiente"
    respuesta += "<li>/nuevocontenido/(name)/(page): crea un nuevo contenido</li>"
    respuesta += '<br><a href="http://localhost:8000">Vuelve a la pagina principal</a></ul>'
    return HttpResponse(respuesta)
