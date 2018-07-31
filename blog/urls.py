from django.conf.urls import include, url
from . import views

urlpatterns = [
      url(r'^$', views.lista_casas),
      url(r'^casas/(?P<pk>[0-9]+)/$', views.detalles_casas, name='detalles_casas'),
      #url(r'^casa/nueva/$', views.nueva_casa, name='nueva_casa'),
    ]
