from random import random
from django.shortcuts import render
#from django.http import HttpResponse
import random

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    generar_contraseña = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        caracteres.extend(list('!@#$%&()/*+-_'))

    if request.GET.get('special'):
        caracteres.extend(list('0123456789'))

    for x in range(length):
        generar_contraseña += random.choice(caracteres)

    return render(request, 'generator/password.html', {'password': generar_contraseña})