from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'barrapunto.views.mostrarContenido'),
    url(r'^(\d+)$', 'barrapunto.views.mostrarPagina'),
    url(r'^nuevocontenido/(.+)\/(.+)$', 'barrapunto.views.nuevoContenido'),
    url(r'^update$', 'barrapunto.views.update'),
    url(r'.*', 'barrapunto.views.notfound'),
]
