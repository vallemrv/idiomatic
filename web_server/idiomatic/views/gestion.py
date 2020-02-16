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
        lec = Lecciones.objects.filter(id=request.session["leccion_gs"])
        lineas = request.POST["preguntas"].split("\n")
        lineas_local = []
        lienas_extranjero = []
        for l in lineas:
            sl = l.split(" # ")
            if len(sl) == 2:
                lineas_local.append(sl[0].strip())
                lienas_extranjero.append(sl[1].strip())
        if lec:
            lec = lec.first()
            lec.nombre = nombre=request.POST["nombre"]
            lec.objetivo = request.POST["des"]
            lec.save()
            lec.frases_set.all().delete()
        else:
            lec = Lecciones(curso_id=request.session["curso_gs"],
                            nombre=request.POST["nombre"],
                            objetivo=request.POST["des"])
            lec.save()

        for i in range(0, len(lineas_local)):
            lec.frases_set.create(propia=lineas_local[i],
                                  extranjera=lienas_extranjero[i])
        return redirect("lista_lecciones_gs", id=request.session["curso_gs"])

    lec = Lecciones.objects.filter(id=request.session["leccion_gs"])
    if lec:
        lec = lec.first()
        frases = []
        for f in lec.frases_set.all():
            frases.append("%s # %s" % (f.propia, f.extranjera))
        return render(request, "gestion/lecciones/editar.html",{
             "nombre":lec.nombre,
             "des":lec.objetivo,
             "frases": "\n".join(frases)
        })
    else:
        return render(request, "gestion/lecciones/crear.html")

@login_required(login_url="admin:login")
def lista_lecciones_gs(request, id):
    request.session["curso_gs"] = id
    result = Lecciones.objects.filter(curso_id=id)
    return render(request, "gestion/lecciones/elegir_leccion.html", {
        "result": result,
        "session": request.session
    })

@login_required(login_url="admin:login")
def set_leccion_gs(request, id):
    request.session["leccion_gs"] = id
    return crear_leccion(request)


@login_required(login_url="admin:login")
def set_idioma_gs(request, id):
    request.session["idioma_gs"] = id
    return redirect('elegir_curso_gs')


@login_required(login_url="admin:login")
def gestion_cursos_listado(request):
    return render(request, "gestion/cursos/listado.html")
