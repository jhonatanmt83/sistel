# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
#, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
# , HttpResponseRedirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from django.utils import simplejson
import json
# from django.views.decorators.csrf import csrf_exempt

# Importacion de modelos
from pc.models import *

# Importacion de formularios
from pc.forms import *

#import datetime


def home(request):
    return render_to_response('index.html', {})


def arma_tu_pc(request):
    cases = Case.objects.all()
    placas = Motherboard.objects.all()
    memorias = Memoria.objects.all()
    procesadores = Procesador.objects.all()
    discos = HDD.objects.all()
    monitores = Monitor.objects.all()
    teclados = Teclado.objects.all()
    mouses = Mouse.objects.all()
    camaras = Camara.objects.all()
    parlantes = Parlante.objects.all()
    audifonos = Audifono.objects.all()
    impresoras = Impresora.objects.all()
    estabilizadores = Estabilizador.objects.all()
    datos = {
        'cases': cases,
        'placas': placas,
        'memorias': memorias,
        'procesadores': procesadores,
        'discos': discos,
        'monitores': monitores,
        'teclados': teclados,
        'mouses': mouses,
        'camaras': camaras,
        'parlantes': parlantes,
        'audifonos': audifonos,
        'impresoras': impresoras,
        'estabilizadores': estabilizadores,
    }
    return render_to_response('arma_tu_pc.html', {'datos': datos}, context_instance=RequestContext(request))


def datos_objeto(request, codigo, objeto):
    """Devuelve datos necesarios de un objeto determinado"""
    lista = [Case, Motherboard, Memoria, Procesador, HDD, Monitor, Teclado, Mouse, Camara, Parlante, Impresora, Estabilizador, Audifono]
    objeto = lista[int(objeto) - 1].objects.get(pk=int(codigo))
    new_result = []
    datos = {}
    datos['precio'] = str(objeto.precio)
    datos['modelo'] = str(objeto.modelo)
    try:
        datos['url_img'] = str(objeto.ulr_imagen_mostrar())
    except:
        pass
    new_result.append(datos)
    return HttpResponse(json.dumps(new_result))


def datos_componentes(request, id_placa):
    """Devuelve datos necesarios de una placa determinada"""
    placa = Motherboard.objects.get(pk=int(id_placa))
    # memorias
    tipo_memoria = placa.tipomemoria.all()
    memorias = Memoria.objects.filter(tipomemoria=tipo_memoria)
    # procesadores
    tipo_procesador = placa.tipoprocesador.all()
    procesadores = Procesador.objects.filter(tipoprocesador=tipo_procesador)
    # discos
    tipo_disco = placa.tipohdd.all()
    discos = HDD.objects.filter(tipohdd=tipo_disco)
    new_result = []
    datos = {}
    memorias_add = []
    for x in memorias:
        memorias_add.append({'modelo': x.modelo, 'pk': x.pk, 'precio': str(x.precio)})
    datos['memorias'] = {'seccion': 'memoria', 'datos': memorias_add}
    procesadores_add = []
    for x in procesadores:
        procesadores_add.append({'modelo': x.modelo, 'pk': x.pk, 'precio': str(x.precio)})
    datos['procesadores'] = {'seccion': 'procesador', 'datos': procesadores_add}
    discos_add = []
    for x in discos:
        discos_add.append({'modelo': x.modelo, 'pk': x.pk, 'precio': str(x.precio)})
    datos['discos'] = {'seccion': 'disco', 'datos': discos_add}
    new_result.append(datos)
    return HttpResponse(json.dumps(new_result))
