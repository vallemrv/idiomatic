# @Author: Manuel Rodriguez <valle>
# @Date:   13-Jan-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 16-Apr-2018
# @License: Apache license vesion 2.0

"""web_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path as url
from django.contrib import admin
from idiomatic import views

urlpatterns = [
    url(r'^view_logo/(?P<id>\d*)/$', views.view_logo, name="view_logo"),
    url(r'^sel_idioma/(?P<id>\d*)/$', views.sel_idioma, name="sel_idioma"),
    url(r'^sel_curso/(?P<id>\d*)/$', views.sel_curso, name="sel_curso"),
    url(r'^sel_leccion/(?P<id>\d*)/$', views.sel_leccion, name="sel_leccion"),
    url(r'^get_sound/(?P<id>\d*)/$', views.get_sound, name="get_sound"),
    url(r'^calificar/(?P<id>-?\d*)/(?P<punto>-?\d*)/$', views.calificar, name="calificar"),
    url(r'^lista_cursos/$', views.lista_cursos, name="lista_cursos"),
    url(r'^lista_lecciones_gs/(?P<id>-?\d*)/$', views.lista_lecciones_gs, name="lista_lecciones_gs"),
    url(r'^lista_lecciones/$', views.lista_lecciones, name="lista_lecciones"),
    url(r'^elegir_idioma/$', views.elegir_idioma, name="elegir_idioma"),
    url(r'^leccion/$', views.leccion, name="leccion"),
    url(r'^get_next_frase/$', views.get_next_frase, name="get_next_frase"),
    url(r'^gestion_cursos_listado/$', views.gestion_cursos_listado, name="gestion_cursos_listado"),
    url(r'^gestion/$', views.gestion, name="gestion"),
    url(r'^elegir_curso_gs/$', views.elegir_curso_gs, name="elegir_curso_gs"),
    url(r'^elegir_idioma_gs/$', views.elegir_idioma_gs, name="elegir_idioma_gs"),
    url(r'^set_leccion_gs/(?P<id>-?\d*)/$', views.set_leccion_gs, name="set_leccion_gs"),
    url(r'^set_idioma_gs/(?P<id>-?\d*)/$', views.set_idioma_gs, name="set_idioma_gs"),
    url(r'^crear_leccion/$', views.crear_leccion, name="crear_leccion"),
    url(r'^create_student/$', views.create_student, name="create_student"),
    url(r'^get_final/$', views.get_final, name="get_final"),
    url(r'^$', views.home, name="home"),
]
