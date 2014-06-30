# -*- coding: utf-8 -*-
from django.db import models

# imports
import os
from thumbs import ImageWithThumbsField


# Obtencion de rutas de imagenes
def get_image_marcas_path(instance, filename):
    return os.path.join('marcas', str(instance.id), filename)


def get_image_case_path(instance, filename):
    return os.path.join('case', str(instance.id), filename)


def get_image_mouse_path(instance, filename):
    return os.path.join('mouse', str(instance.id), filename)


def get_image_camara_path(instance, filename):
    return os.path.join('camara', str(instance.id), filename)


def get_image_teclado_path(instance, filename):
    return os.path.join('teclado', str(instance.id), filename)


def get_image_parlante_path(instance, filename):
    return os.path.join('parlante', str(instance.id), filename)


def get_image_audifono_path(instance, filename):
    return os.path.join('audifono', str(instance.id), filename)


def get_image_impresora_path(instance, filename):
    return os.path.join('impresora', str(instance.id), filename)


def get_image_monitor_path(instance, filename):
    return os.path.join('monitor', str(instance.id), filename)


def get_image_estabilizador_path(instance, filename):
    return os.path.join('estabilizador', str(instance.id), filename)


# Create your models here.
class TipoMemoria(models.Model):
    class Meta:
        verbose_name = ('TipoMemoria')
        verbose_name_plural = ('TipoMemorias')

    nombre = models.CharField(max_length=50, verbose_name=u'Nombre')
    abreviacion = models.CharField(max_length=10, verbose_name=u'Abreviación', blank=True)
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True)

    def __unicode__(self):
        return self.nombre


class TipoHDD(models.Model):
    class Meta:
        verbose_name = ('TipoHDD')
        verbose_name_plural = ('TipoHDDs')

    nombre = models.CharField(max_length=50, verbose_name=u'Nombre')
    abreviacion = models.CharField(max_length=10, verbose_name=u'Abreviación', blank=True)
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True)

    def __unicode__(self):
        return self.nombre


class TipoProcesador(models.Model):
    class Meta:
        verbose_name = ('TipoProcesador')
        verbose_name_plural = ('TipoProcesadores')

    nombre = models.CharField(max_length=50, verbose_name=u'Nombre')
    abreviacion = models.CharField(max_length=30, verbose_name=u'Abreviación', blank=True)
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True)

    def __unicode__(self):
        return self.nombre


class TipoFuente(models.Model):
    class Meta:
        verbose_name = ('TipoFuente')
        verbose_name_plural = ('TipoFuentes')

    nombre = models.CharField(max_length=50, verbose_name=u'Nombre')
    abreviacion = models.CharField(max_length=10, verbose_name=u'Abreviación', blank=True)
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True)

    def __unicode__(self):
        return self.nombre


class TipoMonitor(models.Model):
    class Meta:
        verbose_name = ('TipoMonitor')
        verbose_name_plural = ('TipoMonitores')

    nombre = models.CharField(max_length=50, verbose_name=u'Nombre')
    abreviacion = models.CharField(max_length=10, verbose_name=u'Abreviación', blank=True)
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True)

    def __unicode__(self):
        return self.nombre


class TipoCapacidad(models.Model):
    class Meta:
        verbose_name = ('TipoCapacidad')
        verbose_name_plural = ('TipoCapacidades')

    nombre = models.CharField(max_length=50, verbose_name=u'Nombre')
    abreviacion = models.CharField(max_length=10, verbose_name=u'Abreviación', blank=True)
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True)

    def __unicode__(self):
        return self.nombre


class TipoTeclado(models.Model):
    class Meta:
        verbose_name = ('TipoTeclado')
        verbose_name_plural = ('TipoTeclados')

    nombre = models.CharField(max_length=50, verbose_name=u'Nombre')
    abreviacion = models.CharField(max_length=10, verbose_name=u'Abreviación', blank=True)
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True)

    def __unicode__(self):
        return self.nombre


# otros a relacionar

class Marca(models.Model):
    class Meta:
        verbose_name = ('Marca')
        verbose_name_plural = ('Marcas')

    nombre = models.CharField(max_length=30, verbose_name=u'Nombre')
    logo = models.ImageField(upload_to=get_image_marcas_path, blank=True)

    def __unicode__(self):
        return self.nombre


# componentes
class Mouse(models.Model):
    class Meta:
        verbose_name = ('Mouse')
        verbose_name_plural = ('Mouses')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_mouse')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    #imagen = models.ImageField(upload_to=get_image_mouse_path, blank=True)
    imagen = ImageWithThumbsField(upload_to=get_image_mouse_path, sizes=((50, 50), (100, 100)))
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo

    def ulr_imagen_mostrar(self):
        return self.imagen.url_100x100


class Teclado(models.Model):
    class Meta:
        verbose_name = ('Teclado')
        verbose_name_plural = ('Teclados')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_teclado')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    tipoteclado = models.ForeignKey(TipoTeclado, related_name='tipoteclado_tec')
    distribucion = models.CharField(max_length=2, choices=(('ES', 'Español'), ('IN', 'Ingles'), ('LA', 'Latinoamericano')), verbose_name=u'Distribución')
    entrada = models.CharField(max_length=3, choices=(('USB', 'USB'), ('PS2', 'PS2')), verbose_name=u'Tipo de entrada')
    #imagen = models.ImageField(upload_to=get_image_teclado_path, blank=True)
    imagen = ImageWithThumbsField(upload_to=get_image_teclado_path, sizes=((50, 50), (195, 110)))
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo

    def ulr_imagen_mostrar(self):
        return self.imagen.url_195x110


class Camara(models.Model):
    class Meta:
        verbose_name = ('Camara')
        verbose_name_plural = ('Camaras')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_camara')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    #imagen = models.ImageField(upload_to=get_image_camara_path, blank=True)
    imagen = ImageWithThumbsField(upload_to=get_image_camara_path, sizes=((50, 50), (195, 110)))
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo

    def ulr_imagen_mostrar(self):
        return self.imagen.url_195x110


class Parlante(models.Model):
    class Meta:
        verbose_name = ('Parlante')
        verbose_name_plural = ('Parlantes')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_parlante')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    #imagen = models.ImageField(upload_to=get_image_parlante_path, blank=True)
    imagen = ImageWithThumbsField(upload_to=get_image_parlante_path, sizes=((50, 50), (150, 110)))
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo

    def ulr_imagen_mostrar(self):
        return self.imagen.url_150x110


class Audifono(models.Model):
    class Meta:
        verbose_name = ('Audifono')
        verbose_name_plural = ('Audifonos')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_audifono')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    #imagen = models.ImageField(upload_to=get_image_audifono_path, blank=True)
    imagen = ImageWithThumbsField(upload_to=get_image_audifono_path, sizes=((50, 50), (150, 110)))
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo

    def ulr_imagen_mostrar(self):
        return self.imagen.url_150x110


class Impresora(models.Model):
    class Meta:
        verbose_name = ('Impresora')
        verbose_name_plural = ('Impresoras')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_impresora')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    #imagen = models.ImageField(upload_to=get_image_impresora_path, blank=True)
    imagen = ImageWithThumbsField(upload_to=get_image_impresora_path, sizes=((50, 50), (150, 210)))
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo

    def ulr_imagen_mostrar(self):
        return self.imagen.url_150x210


class Estabilizador(models.Model):
    class Meta:
        verbose_name = ('Estabilizador')
        verbose_name_plural = ('Estabilizadores')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_estabilizador')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    #imagen = models.ImageField(upload_to=get_image_estabilizador_path, blank=True)
    imagen = ImageWithThumbsField(upload_to=get_image_estabilizador_path, sizes=((50, 50), (150, 110)))
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo

    def ulr_imagen_mostrar(self):
        return self.imagen.url_150x110


class Procesador(models.Model):
    class Meta:
        verbose_name = ('Procesador')
        verbose_name_plural = ('Procesadores')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_procesador')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    capacidad = models.CharField(max_length=50, verbose_name=u'Capacidad')
    tipoprocesador = models.ForeignKey(TipoProcesador, related_name='tipoprocesador_pro')
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo


class Memoria(models.Model):
    class Meta:
        verbose_name = ('Memoria')
        verbose_name_plural = ('Memorias')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_memoria')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    capacidad = models.IntegerField(verbose_name=u'Capacidad')
    tipocapacidad = models.ForeignKey(TipoCapacidad, related_name='tipocapacidad_mem', verbose_name=u'Unidad de medida')
    tipomemoria = models.ForeignKey(TipoMemoria, related_name='tipomemoria_mem')
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo


class Monitor(models.Model):
    class Meta:
        verbose_name = ('Monitor')
        verbose_name_plural = ('Monitores')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_monitor')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    pulgadas = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Pulgadas')
    tipomonitor = models.ForeignKey(TipoMonitor, related_name='tipomonitor_mon')
    entrada = models.CharField(max_length=4, choices=(('HDMI', 'HDMI'), ('VGA', 'VGA')), verbose_name=u'Tipo de entrada')
    #imagen = models.ImageField(upload_to=get_image_monitor_path, blank=True)
    imagen = ImageWithThumbsField(upload_to=get_image_monitor_path, sizes=((50, 50), (195, 210)))
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo

    def ulr_imagen_mostrar(self):
        return self.imagen.url_195x210


class HDD(models.Model):
    class Meta:
        verbose_name = ('HDD')
        verbose_name_plural = ('HDDs')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_hdd')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    capacidad = models.IntegerField(verbose_name=u'Capacidad')
    tipocapacidad = models.ForeignKey(TipoCapacidad, related_name='tipocapacidad_hdd', verbose_name=u'Unidad de medida')
    tipohdd = models.ForeignKey(TipoHDD, related_name='tipohdd_hdd')
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo


class Case(models.Model):
    class Meta:
        verbose_name = ('Case')
        verbose_name_plural = ('Cases')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_case')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    #imagen = models.ImageField(upload_to=get_image_case_path, blank=True)
    imagen = ImageWithThumbsField(upload_to=get_image_case_path, sizes=((50, 80), (100, 200)))
    descripcion = models.TextField(verbose_name=u'Descripción', blank=True, null=True)

    def __unicode__(self):
        return self.modelo

    def ulr_imagen_mostrar(self):
        return self.imagen.url_100x200


class Motherboard(models.Model):
    class Meta:
        verbose_name = ('Motherboard')
        verbose_name_plural = ('Motherboards')

    modelo = models.CharField(max_length=50, verbose_name=u'Modelo')
    marca = models.ForeignKey(Marca, verbose_name=u'Marca', related_name='marca_motherboard')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio S/.')
    tipomemoria = models.ManyToManyField(TipoMemoria, related_name='tipomemoria_mb', verbose_name=u'Tipo de memoria')
    tipohdd = models.ManyToManyField(TipoHDD, related_name='tipohdd_mb', verbose_name=u'Tipo de HDD')
    tipoprocesador = models.ManyToManyField(TipoProcesador, related_name='tipoprocesador_mb', verbose_name=u'Tipo de procesador')
    descripcion = models.TextField(verbose_name=u'Descripción')

    def __unicode__(self):
        return self.modelo
