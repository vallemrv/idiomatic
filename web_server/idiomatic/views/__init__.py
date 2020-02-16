# @Author: Manuel Rodriguez <valle>
# @Date:   13-Jan-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 21-Apr-2018
# @License: Apache license vesion 2.0
from .gestion import *

from django.db.models import Q, Avg
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from idiomatic.models import (Idiomas, Cursos, Lecciones, Frases,
                              Progreso, Estudiante)
from idiomatic.decorators import is_student_registered
import os
import random
import uuid

def show_home_page(request):
    if "idioma" in request.session:
        if "curso" in request.session:
            if "leccion" in request.session:
                redirect("leccion")
            else:
                redirect("lista_lecciones")
        else:
            redirect("lista_cursos")
    result = Idiomas.objects.all()
    return render(request, "idiomatic/home.html", {
        "result": result,
        "session": request.session
    })

def create_student(request):
    print(request.POST)
    if "nick" in request.POST and request.POST["nick"] != "":
        nick = request.POST["nick"]
        uid = ""
        s = Estudiante.objects.filter(nick=nick)
        if s:
            uid = s.first().id
        else:
            s = Estudiante(nick = request.POST["nick"])
            s.save()
            uid = s.id

        request.session["estudiante"] = str(uid)
        return show_home_page(request)
    else:
        return render(request, "idiomatic/keep_nick.html", {
        })

@is_student_registered
def home(request):
    return show_home_page()


@is_student_registered
def lista_cursos(request):
    if "idioma" not in request.session:
        redirect("home")
    result = Idiomas.objects.get(pk=request.session["idioma"])
    return render(request, "idiomatic/lista_cursos.html", {
        "result": result.cursos_set.all(),
        "session": request.session
    })


@is_student_registered
def lista_lecciones(request):
    if "curso" not in request.session:
        redirect("home")
    result = Cursos.objects.get(pk=request.session["curso"])
    return render(request, "idiomatic/lista_lecciones.html", {
        "result": result.lecciones_set.all(),
        "session": request.session
    })

@is_student_registered
def leccion(request):
    if "leccion" not in request.session:
        return redirect("home")
    leccion = Lecciones.objects.get(pk=request.session["leccion"])
    return render(request, "idiomatic/leccion.html", {
        "session": request.session,
        "title": leccion.nombre,
    })

@is_student_registered
def get_next_frase(request):
    if "leccion" not in request.session:
        redirect("home")
    estado = request.session["estado"]
    if estado["punt"] < len(estado["prg"]):
        id = estado["prg"][estado["punt"]]
        frase = Frases.objects.get(id=id)
        estado["punt"] = estado["punt"] + 1
    else:
        estado["punt"] = 0
        frases = get_lista_frases(request)
        if len(frases) > 0:
            s = list(frases.values_list("id", flat=True))
            random.shuffle(s)
            estado["prg"] = s
            id = s[estado["punt"]]
            frase = Frases.objects.get(id=id)
            estado["punt"] = estado["punt"] + 1
        else:
            request.session["contador"] = get_contador(request)
            frases = get_lista_frases(request)
            s = list(frases.values_list("id", flat=True))
            random.shuffle(s)
            estado["prg"] = s
            id = s[estado["punt"]]
            frase = Frases.objects.get(id=id)
            estado["punt"] = estado["punt"] + 1

    request.session["estado"] = estado
    return render(request, "idiomatic/leccion_ajax.html", {
        "frase": frase,
        "session": request.session
    })

def calificar(request, id, punto):
    estudiante = request.session["estudiante"]
    ps = Progreso.objects.filter(Q(frase_id=id) & Q(estudiante_id=estudiante))
    if len(ps) == 0:
        progreso = Progreso(estudiante_id=estudiante, frase_id=id)
        progreso.save()
    else:
        progreso = ps[0]

    progreso.puntos = progreso.puntos + int(punto)
    progreso.save()
    return redirect('get_next_frase')

def get_final(request):
    leccion = Lecciones.objects.get(pk=request.session["leccion"])
    gift = leccion.recursos.all()
    if len(gift) > 0:
        return render(request, "idiomatic/gift.html", {
            "session": request.session,
            "obj": gift[0]
        })
    else:
        return render(request, "idiomatic/no_gift.html", {
            "session": request.session
        })


def view_logo(request, id):
    try:
        obj = Idiomas.objects.get(pk=id)
    except Exception as e:
        print("[ Error en view_logo ] %s" % e)

    file_rml = os.path.join(settings.MEDIA_ROOT, obj.fichero.name )
    f = open(file_rml, "rb")
    response = HttpResponse(content_type='image/*')
    response['Content-Disposition'] = 'inline; filename="%s"' % os.path.basename(obj.fichero.name)
    response.write(f.read())
    return response

def get_sound(request, id):
    def crear_sonido():
        from gtts import gTTS
        idioma = Idiomas.objects.get(pk=request.session["idioma"])
        tts = gTTS(text=obj.extranjera, lang=idioma.idioma)
        name = "pronunciacion/" +str(uuid.uuid4())+".mp3"
        file_rml = os.path.join(settings.MEDIA_ROOT,  name)
        tts.save(file_rml)
        sonido = obj.pronunciacion_set.create(fichero=name, tipo='SN')
        return file_rml

    try:
        obj = Frases.objects.get(pk=id)
    except Exception as e:
        print("[ Error en get_sound ] %s" % e)

    sounds = obj.pronunciacion_set.all()
    num_sounds = len(sounds)
    if num_sounds > 0:
        sonido = sounds[random.randint(0, num_sounds-1)]
        file_rml = os.path.join(settings.MEDIA_ROOT, sonido.fichero.name )
        if not os.path.isfile(file_rml):
            file_rml = crear_sonido()
    else:
        file_rml = crear_sonido()

    f = open(file_rml, "rb")
    response = HttpResponse(content_type='audio/*')
    response['Content-Disposition'] = 'inline; filename="%s"' % os.path.basename(file_rml)
    response.write(f.read())
    return response


def sel_leccion(request, id):
    request.session["leccion"] = id
    request.session["contador"] = get_contador(request)
    request.session["estado"] = {"prg":[], "punt": 0}
    return redirect("leccion")


def sel_curso(request, id):
    request.session["curso"] = id
    return redirect("lista_lecciones")


def sel_idioma(request, id):
    request.session["idioma"] = id
    return redirect("lista_cursos")

def elegir_idioma(request):
    if "idioma" in request.session:
        del request.session["idioma"]
    if "curso" in request.session:
        del request.session["curso"]
    if "leccion" in request.session:
        del request.session["leccion"]
    return redirect("home", permanent=False)


def get_contador(request):
    estudiante = request.session["estudiante"]
    leccion = Lecciones.objects.get(pk=request.session["leccion"])
    frases = leccion.frases_set.all()
    ids_frases = list(frases.values_list("id", flat=True))
    max = Progreso.objects.filter(frase_id__in=ids_frases,
                                  estudiante=estudiante).aggregate(Avg("puntos"))

    if max["puntos__avg"] == None:
        return 1
    else:
        return int(max["puntos__avg"])


def get_lista_frases(request):
    estudiante = request.session["estudiante"]
    leccion = Lecciones.objects.get(pk=request.session["leccion"])
    all_frases = leccion.frases_set.all()
    ids_frases = list(all_frases.values_list("id", flat=True))
    ids_progres = list(Progreso.objects.filter(frase_id__in=ids_frases,
                                               estudiante=estudiante,
                                               puntos__gt=request.session["contador"]).values_list('frase_id', flat=True))

    return all_frases.exclude(id__in=ids_progres)
