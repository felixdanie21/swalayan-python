from django.shortcuts import render
from django.http import HttpResponse
from .utilities import ambil_menu
from .models import Modul


def blank(request):
    return render(request, 'blank.html')


def login(request):
    return HttpResponse('halaman login')


def dashboard(request):
    context = {
        'dbmenu': ambil_menu('dashboard'),
        'parent_segment': '-',
        'segment': 'modul',
        'dbmodul': Modul.objects.all()
    }
    return render(request, 'dashboard.html', context)
