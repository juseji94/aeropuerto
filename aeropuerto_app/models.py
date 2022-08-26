from django.db import models


class Avion(models.Model):
    codigo_avion = models.CharField(max_length=20, unique=True)
    tipo_avion = models.CharField(max_length=20)
    ciudad_base = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)


class Piloto(models.Model):
    codigo_piloto = models.CharField(max_length=20, unique=True)
    nombre_piloto = models.CharField(max_length=50)
    horas_vuelo_piloto = models.IntegerField()


class Tripulacion(models.Model):
    codigo_tripulante = models.CharField(max_length=20, unique=True)
    nombre_tripulante = models.CharField(max_length=50)


class Vuelo(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.PROTECT)
    piloto = models.ForeignKey(Piloto, on_delete=models.PROTECT)
    numero_vuelo = models.CharField(max_length=6, unique=True)
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)


class Itinerario(models.Model):
    vuelo = models.ForeignKey(Vuelo, on_delete=models.PROTECT)
    tripulacion = models.ForeignKey(Tripulacion, on_delete=models.PROTECT)
    codigo_tabla = models.CharField(max_length=20, unique=True)
