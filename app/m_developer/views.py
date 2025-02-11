from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from app.utilities import ambil_menu, insert_csv
from app.decorators import user_level_required, login_required
from app.models import Menu, Msatuan
import json
import csv


@login_required()
@user_level_required('0')
def index(request):
    context = {
        'dbmenu': ambil_menu('developer'),
        'parent_segment': '-',
        'segment': '',
    }
    return render(request, 'developer/index.html', context)


@login_required()
@user_level_required('0')
def import_csv(request):
    models = ContentType.objects.all().order_by('model')
    context = {
        'dbmenu': ambil_menu('developer'),
        'parent_segment': '-',
        'segment': 'import_csv',
        'models': models
    }
    return render(request, 'developer/import-csv.html', context)


@login_required()
@user_level_required('0')
def import_csv_post(request):
    csv_file = request.FILES['filecsv']
    decoded_file = csv_file.read().decode('utf-8-sig')
    reader = csv.reader(decoded_file.splitlines(),
                        delimiter='~', dialect='excel-tab')
    for row in reader:
        insert_csv(request.POST['table'], row)
    messages.success(request, 'Berhasil Import CSV.')
    return redirect('import_csv')


@login_required()
def contoh_form(request):
    context = {
        'dbmenu': ambil_menu('developer'),
        'parent_segment': '-',
        'segment': 'contoh_form',
    }
    return render(request, 'developer/contoh-form.html', context)


@login_required()
def contoh_table(request):
    context = {
        'dbmenu': ambil_menu('developer'),
        'parent_segment': '-',
        'segment': 'contoh_table',
        'msatuan': Msatuan.objects.all()
    }
    return render(request, 'developer/contoh-table.html', context)
