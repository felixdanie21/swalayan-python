from django.shortcuts import render
from django.http import HttpResponse
from app.utilities import ambil_menu

# Create your views here.


def index(request):
    context = {
        'dbmenu': ambil_menu('c'),
        'parent_segment': '-',
        'segment': '',
    }
    return render(request, 'datainduk/index.html', context)
