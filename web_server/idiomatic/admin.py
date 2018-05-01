# @Author: Manuel Rodriguez <valle>
# @Date:   13-Jan-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 17-Apr-2018
# @License: Apache license vesion 2.0


from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from idiomatic.models import *

class IdiomasAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        url = reverse("view_logo", args=(obj.id, ))
        return format_html('<img height=50 src="{}" />'.format(url))

    image_tag.short_description = 'Logo'

    list_display = ["idioma", 'image_tag',]



class CursosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]


class FrasesInline(admin.TabularInline):
    model = Frases

class LeccionAdmin(admin.ModelAdmin):
    list_display = ["nombre", "objetivo"]
    inlines = [
        FrasesInline
    ]


class FrasesAdmin(admin.ModelAdmin):
    exclude = ["positivos"]
    list_display = ["propia", "extranjera"]

class RecursosAdmin(admin.ModelAdmin):

    def nombre(self, obj):
        return obj.leccion.nombre

    nombre.short_description = 'Nombre'

    list_display = ["nombre", 'fichero',]


admin.site.register(Recursos, RecursosAdmin)
admin.site.register(Frases, FrasesAdmin)
admin.site.register(Lecciones, LeccionAdmin)
admin.site.register(Idiomas, IdiomasAdmin)
admin.site.register(Cursos, CursosAdmin)
