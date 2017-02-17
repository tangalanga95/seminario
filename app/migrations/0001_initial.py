# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AltasCese',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('tipo', models.TextField()),
                ('fechaDesde', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaHasta', models.DateTimeField(default=django.utils.timezone.now)),
                ('dni_reemplazado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('horas', models.IntegerField()),
                ('modulos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('anio', models.IntegerField()),
                ('seccion', models.CharField(max_length=20)),
                ('turno', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('apellido', models.TextField()),
                ('nombre', models.TextField()),
                ('cuil', models.TextField()),
                ('fecha_nacimiento', models.DateTimeField(default=django.utils.timezone.now)),
                ('cupof', models.IntegerField()),
                ('altasCeses', models.ForeignKey(to='app.AltasCese')),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('direccion', models.TextField()),
                ('numero', models.TextField()),
                ('cue', models.TextField()),
                ('docentes', models.ForeignKey(to='app.Docente')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('dias', models.TextField()),
                ('hora', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HorasCatedra',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('revista', models.TextField()),
                ('modalidad', models.TextField()),
                ('asignatura', models.TextField()),
                ('cargos', models.ForeignKey(to='app.Cargo')),
                ('cursos', models.ForeignKey(to='app.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Inasistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('fechaDesde', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaHasta', models.DateTimeField(default=django.utils.timezone.now)),
                ('cursos', models.ForeignKey(to='app.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('articulo', models.CharField(max_length=20)),
                ('inciso', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('horarios', models.ForeignKey(to='app.Horario')),
            ],
        ),
        migrations.AddField(
            model_name='inasistencia',
            name='licencias',
            field=models.ForeignKey(to='app.Licencia'),
        ),
        migrations.AddField(
            model_name='docente',
            name='horas',
            field=models.ForeignKey(to='app.HorasCatedra'),
        ),
        migrations.AddField(
            model_name='docente',
            name='inasistencias',
            field=models.ForeignKey(to='app.Inasistencia'),
        ),
        migrations.AddField(
            model_name='curso',
            name='materias',
            field=models.ForeignKey(to='app.Materia'),
        ),
    ]
