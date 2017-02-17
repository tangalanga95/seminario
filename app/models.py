from django.db import models
from django.utils import timezone


class AltasCese(models.Model):
    tipo = models.TextField()
    fechaDesde = models.DateTimeField(default=timezone.now)
    fechaHasta = models.DateTimeField(default=timezone.now)
    dni_reemplazado = models.IntegerField()


class Licencia(models.Model):
    articulo = models.CharField(max_length=20)
    inciso = models.CharField(max_length=20)


class Inasistencia(models.Model):
    fechaDesde = models.DateTimeField(default=timezone.now)
    fechaHasta = models.DateTimeField(default=timezone.now)
    licencias = models.ForeignKey('Licencia')
    cursos = models.ForeignKey('Curso')


class Horario(models.Model):
    dias = models.TextField()
    hora = models.TextField()


class Materia(models.Model):
    nombre = models.TextField()
    horarios = models.ForeignKey('Horario')


class Curso(models.Model):
    anio = models.IntegerField()
    seccion = models.CharField(max_length=20)
    turno = models.TextField()
    materias = models.ForeignKey('Materia')


class Cargo(models.Model):
    nombre = models.TextField()
    horas = models.IntegerField()
    modulos = models.IntegerField()


class HorasCatedra(models.Model):
    revista = models.TextField()
    modalidad = models.TextField()
    asignatura = models.TextField()
    cargos = models.ForeignKey('Cargo')
    cursos = models.ForeignKey('Curso')


class Docente(models.Model):
    apellido = models.TextField()
    nombre = models.TextField()
    cuil = models.TextField()
    fecha_nacimiento = models.DateTimeField(default=timezone.now)
    cupof = models.IntegerField()
    altasCeses = models.ForeignKey('AltasCese')
    inasistencias = models.ForeignKey('Inasistencia')
    horas = models.ForeignKey('HorasCatedra')


class Escuela(models.Model):
    nombre = models.TextField()
    direccion = models.TextField()
    numero = models.TextField()
    cue = models.TextField()
    docentes = models.ForeignKey('Docente')