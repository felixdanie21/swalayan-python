from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .decorators import login_required
from .utilities import ambil_menu
from .models import Modul, Muser


def blank(request):
    return render(request, 'blank.html')


def login(request):
    return render(request, 'login.html')


def login_post(request):
    userid = request.POST['userid'].upper()
    password = request.POST['password'].upper()
    if Muser.objects.filter(userid=userid).exists():
        user = Muser.objects.get(userid=userid)
        if password == user.password:
            request.session['userid'] = user.userid
            request.session['username'] = user.username
            request.session['userlevel'] = user.userlevel
            request.session['userimage'] = user.userimage
            request.session.save()
            messages.success(request, 'BERHASIL LOGIN')
            return redirect('dashboard')
        else:
            messages.error(request, 'PASSWORD SALAH')
    else:
        messages.error(request, 'USER TIDAK DITEMUKAN')
    return redirect('login')


def logout(request):
    request.session.flush()
    messages.success(request, 'BERHASIL LOGOUT')
    return redirect('login')


@login_required()
def dashboard(request):
    context = {
        'dbmenu': ambil_menu('dashboard'),
        'parent_segment': '-',
        'segment': 'modul',
        'dbmodul': Modul.objects.all()
    }
    return render(request, 'dashboard.html', context)
