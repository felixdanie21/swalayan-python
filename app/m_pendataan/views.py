from django.shortcuts import render
from django.http import HttpResponse
from app.utilities import ambil_menu
from app.decorators import login_required


@login_required()
def index(request):
    context = {
        'dbmenu': ambil_menu('a'),
        'parent_segment': '-',
        'segment': '',
    }
    return render(request, 'pendataan/index.html', context)
