from django.db import models

class Isla(models.Model):
    nombre = models.CharField(max_length=30)
    calificacion_tres = models.IntegerField()
    calificacion_dos = models.IntegerField()
    calificacion_uno = models.IntegerField()

    class Meta:
        db_table = 'isla'

class TipoNegocio(models.Model):
    tipo = models.CharField(max_length=30)

    class Meta:
        db_table = 'tipo_negocio'

class Negocio(models.Model):
    nombre = models.CharField(max_length=30)
    servicios = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    direccion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=300)
    tipo_negocio = models.ForeignKey(TipoNegocio, on_delete=models.CASCADE)
    isla = models.ForeignKey(Isla, on_delete=models.CASCADE)

    class Meta:
        db_table = 'negocio'

class Resena(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField()
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'resena'

class Biodiversidad(models.Model):
    nombre_comun = models.CharField(max_length=30)
    nombre_cientifico = models.CharField(max_length=50)
    dato = models.CharField(max_length=200)
    imagen = models.CharField(max_length=300)

    class Meta:
        db_table = 'biodiversidad'

class Fauna(Biodiversidad):
    habitat = models.CharField(max_length=50)
    alimentacion = models.CharField(max_length=50)

    class Meta:
        db_table = 'fauna'

class Flora(Biodiversidad):
    distribucion = models.CharField(max_length=50)
    usos = models.CharField(max_length=100)

    class Meta:
        db_table = 'flora'
