# @Author: Manuel Rodriguez <valle>
# @Date:   13-Jan-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 22-Apr-2018
# @License: Apache license vesion 2.0


from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.conf import settings
import os
import uuid

# Create your models here.
IDIOMAS = [
     ('en' , 'English'),
     ('en-au', 'English (Australia)'),
     ('en-uk', 'English (United Kingdom)'),
     ('en-us', 'English (United States)'),
     ('fr', 'French'),
     ('de', 'German'),
     ('es' , 'Spanish'),
     ('es-es', 'Spanish (Spain)'),
     ('es-us', 'Spanish (United States)'),
]

class Idiomas(models.Model):
    fichero = models.FileField("Logo", upload_to="logos", null=True)
    idioma = models.CharField(max_length=6, choices=IDIOMAS, default="en")

    def __str__(self):
        return self.idioma

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    idioma = models.ForeignKey("Idiomas", on_delete=models.CASCADE)
    descripcion = models.TextField(default="")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = 'Cursos'


class Lecciones(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey("Cursos", on_delete=models.CASCADE)
    objetivo = models.TextField(default="")
    recursos = models.ManyToManyField("Recursos", blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Leccion"
        verbose_name_plural = 'Lecciones'



class Frases(models.Model):
    propia = models.CharField(max_length=300)
    extranjera = models.CharField(max_length=300)
    leccion = models.ForeignKey("Lecciones", on_delete=models.CASCADE)

    def __str__(self):
        return self.propia + " " + self.extranjera

    def save(self, *args, **kwargs):
        super(Frases, self).save(*args, **kwargs)
        self.pronunciacion_set.all().delete()

    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = 'Frases'


class Pronunciacion(models.Model):
    frase = models.ForeignKey("Frases", on_delete=models.CASCADE)
    fichero = models.FileField(null=True, upload_to='pronuciacion')
    tipo = models.CharField(max_length=2, choices=[("VD", "Video"), ("SN", "Sonido")], default="SN")

    class Meta:
        verbose_name = "Pronuciacion"
        verbose_name_plural = 'Pronuciaciones'

class Recursos(models.Model):
    nombre = models.CharField(max_length=100)
    res_external = models.CharField("Url youtube", max_length=100, blank=True, null=True)
    nota = models.TextField(blank=True)
    fichero = models.FileField(null=True, blank=True, upload_to='final_leccion')
    tipo = models.CharField(max_length=2, choices=[("VD", "Video"), ("SN", "Sonido"), ("EX", "Youtube")], default="EX")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = 'Recursos'

class Helpers(models.Model):
    frase = models.ForeignKey("Frases", on_delete=models.CASCADE)
    helper_file = models.ImageField(null=True, upload_to='helpers')
    helper_str = models.TextField(null=True)

    class Meta:
        verbose_name = "Helper"
        verbose_name_plural = 'Helpers'


class Progreso(models.Model):
    estudiante = models.CharField(max_length=100, default=uuid.uuid4)
    frase = models.ForeignKey("Frases", on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)


def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """

    if instance.fichero:
        path = os.path.join(settings.MEDIA_ROOT, instance.fichero.name)
        if os.path.isfile(path):
            os.remove(path)


pre_delete.connect(auto_delete_file_on_delete, sender=Idiomas)
pre_delete.connect(auto_delete_file_on_delete, sender=Pronunciacion)
pre_delete.connect(auto_delete_file_on_delete, sender=Recursos)


def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).fichero
    except MediaFile.DoesNotExist:
        return False

    new_file = instance.fichero
    if not old_file == new_file:
        path = os.path.join(settings.MEDIA_ROOT, instance.fichero.name)
        if os.path.isfile(path):
            os.remove(path)



pre_save.connect(auto_delete_file_on_change, sender=Idiomas)
pre_save.connect(auto_delete_file_on_change, sender=Pronunciacion)
pre_save.connect(auto_delete_file_on_change, sender=Recursos)
