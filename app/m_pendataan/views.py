from django.shortcuts import render
from django.http import HttpResponse
from app.utilities import ambil_menu

# Create your views here.


def index(request):
    context = {
        'dbmenu': ambil_menu('a'),
        'parent_segment': '-',
        'segment': '',
    }
    return render(request, 'pendataan/index.html', context)
