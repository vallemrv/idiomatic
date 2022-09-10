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
from django.urls import path, include
from . import views

urlpatterns = [
    path('token/', include('tokenapi.urls')),
    path("registrarse", views.registrarse, name="registrarse"),
    path("is_username_free", views.is_username_free, name="is_username_free"),
    path("crear_leccion", views.crear_leccion, name="crear_leccion")
]
