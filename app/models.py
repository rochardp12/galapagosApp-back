from django.db import models

class Usuario(models.Model):
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'usuario'

class Isla(models.Model):
    nombre = models.CharField(max_length=30)
    calificacion_tres = models.IntegerField()
    calificacion_dos = models.IntegerField()
    calificacion_uno = models.IntegerField()
    descripcion = models.CharField(max_length=300)
    imagen = models.CharField(max_length=500)
    
    class Meta:
        db_table = 'isla'

class TipoNegocio(models.Model):
    tipo = models.CharField(max_length=30)

    class Meta:
        db_table = 'tipo_negocio'

class Negocio(models.Model):
    nombre = models.CharField(max_length=30)
    servicios = models.CharField(max_length=200)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    direccion = models.CharField(max_length=100)
    imagen = models.CharField(max_length=500)
    tipo_negocio = models.ForeignKey(TipoNegocio, on_delete=models.CASCADE)
    isla = models.ForeignKey(Isla, on_delete=models.CASCADE)

    class Meta:
        db_table = 'negocio'

class Resena(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'resena'

class Biodiversidad(models.Model):
    nombre_comun = models.CharField(max_length=30)
    nombre_cientifico = models.CharField(max_length=50)
    dato = models.CharField(max_length=200)
    imagen = models.CharField(max_length=500)

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

class Actividad(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    edad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    isla = models.ForeignKey(Isla, on_delete=models.CASCADE)

    class Meta:
        db_table = 'actividad'

class GuiasTuristicos(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    imagen = models.CharField(max_length=500)
    isla = models.ForeignKey(Isla, on_delete=models.CASCADE)

    class Meta:
        db_table = 'guias_turisticos'

class Ecosistema(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=500)
    class Meta:
        db_table = 'ecosistema'

class Comentario(models.Model):
    comentario = models.CharField(max_length=200)
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comentario'

class Calificacion(models.Model):
    voto = models.BooleanField(default = False)
    puntuacion = models.IntegerField()
    isla = models.ForeignKey(Isla, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'calificacion'