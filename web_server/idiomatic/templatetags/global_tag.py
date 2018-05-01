
# @Author: Manuel Rodriguez <valle>
# @Date:   09-Apr-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 24-Apr-2018
# @License: Apache license vesion 2.0

from django.db.models import Avg, Sum
from django import template
from django.conf import settings
from idiomatic.models import Frases, Progreso

register = template.Library()
max_repetir = 5

@register.filter
def brand(val):
    if val == "title":
        return settings.BRAND_TITLE
    elif val == "meta":
        return settings.BRAND_META
    else:
        return settings.BRAND

@register.filter
def sepuedemostrar(session, val):
    if val in session:
        return True
    return False


@register.filter
def progreso(session, id=None):
    estudiante = session["estudiante"]
    if id == None:
        id_leccion = session["leccion"]
    else:
        id_leccion = id
    frases = list(Frases.objects.filter(leccion_id=id_leccion).values_list('id', flat=True))
    total = len(frases) * max_repetir
    pg = Progreso.objects.filter(frase_id__in=frases, estudiante=estudiante).aggregate(Sum("puntos"))
    if pg["puntos__sum"] != None:
        minimos = Progreso.objects.filter(frase_id__in=frases, estudiante=estudiante, puntos__lt=max_repetir).count()
        progreso_int = ((pg["puntos__sum"] * 100) / total)
        progress = int(progreso_int) if int(progreso_int) < 100 else (100 - minimos)
        return progress
    else:
        return 0
