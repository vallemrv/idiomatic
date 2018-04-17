# @Author: Manuel Rodriguez <valle>
# @Date:   10-Apr-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 15-Apr-2018
# @License: Apache license vesion 2.0

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from idiomatic.models import Cursos, Idiomas, Frases, Lecciones

@login_required(login_url="admin:login")
def gestion(request):
    return render(request, "gestion/menu/home.html")

@login_required(login_url="admin:login")
def elegir_idioma_gs(request):
    result = Idiomas.objects.all()
    return render(request, "gestion/lecciones/elegir_idioma.html",{
        "result": result,
        "session": request.session
    })

@login_required(login_url="admin:login")
def elegir_curso_gs(request):
    result = Cursos.objects.filter(idioma_id=request.session["idioma_gs"])
    return render(request, "gestion/lecciones/elegir_curso.html", {
        "result": result,
        "session": request.session
    })

@login_required(login_url="admin:login")
def crear_leccion(request):
    if request.method == "POST":
        lineas_local = request.POST["principal"].split("\n")
        lienas_extranjero = request.POST["extranjero"].split("\n")
        lec = Lecciones(curso_id=request.session["curso_gs"],
                        nombre=request.POST["nombre"],
                        objetivo=request.POST["des"])
        lec.save()
        for i in range(0, len(lineas_local)-1):
            lec.frases_set.create(propia=lineas_local[i],
                                  extranjera=lienas_extranjero[i])


    return render(request, "gestion/lecciones/crear.html")

@login_required(login_url="admin:login")
def set_curso_gs(request, id):
    request.session["curso_gs"] = id
    return redirect('crear_leccion')


@login_required(login_url="admin:login")
def set_idioma_gs(request, id):
    request.session["idioma_gs"] = id
    return redirect('elegir_curso_gs')


@login_required(login_url="admin:login")
def gestion_cursos_listado(request):
    return render(request, "gestion/cursos/listado.html")
