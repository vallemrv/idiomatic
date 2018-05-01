# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idiomatic', '0005_auto_20180417_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recursos',
            options={'verbose_name': 'Recurso', 'verbose_name_plural': 'Recursos'},
        ),
        migrations.AddField(
            model_name='recursos',
            name='res_external',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lecciones',
            name=b'recursos',
            field=models.ManyToManyField(blank=True, to='idiomatic.Recursos'),
        ),
        migrations.AlterField(
            model_name='recursos',
            name=b'fichero',
            field=models.FileField(blank=True, null=True, upload_to='final_leccion'),
        ),
        migrations.AlterField(
            model_name='recursos',
            name=b'nota',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recursos',
            name=b'tipo',
            field=models.CharField(choices=[('VD', 'Video'), ('SN', 'Sonido'), ('EX', 'Youtube')], default='SN', max_length=2),
        ),
    ]