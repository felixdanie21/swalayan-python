from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.decorators import login_required
from app.utilities import ambil_menu
from app.models import Msatuan,Mbrgjns,Mpabrik,Mgroup
from django.contrib import messages

@login_required()
def index(request):
    context = {
        'dbmenu': ambil_menu('c'),
        'parent_segment': '-',
        'segment': '',
    }
    return render(request, 'datainduk/index.html', context)
@login_required()
def mbrg_satuan(request):
    judul='Data Satuan'
    context = {
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010400',
        'msatuan':Msatuan.objects.all(),
        'judul':judul
    }
    return render(request,'datainduk/mbrg_satuan/index.html', context)

@login_required()
def mbrg_satuan_form(request,method):
    if method =='tambah':
        data = []
        judul = 'Tambah Satuan'
    elif method =='edit':
        satuankode = request.GET['satuankode']
        data = Msatuan.objects.get(satuankode=satuankode)
        judul = 'Edit Satuan'
    context = {
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010400',
        'method':method,
        'judul':judul,
        'data': data,
    }
    return render (request,'datainduk/mbrg_satuan/form.html',context)
@login_required()
def mbrg_satuan_post(request,method):
    if method == 'tambah':
        satuankode =request.POST['satuankode']
        satuannama= request.POST['satuannama']
        if Msatuan.objects.filter(satuankode=satuankode).exists():
            messages.error(request,'Kode Satuan Sudah Di Gunakan')
            return redirect('mbrg_satuan')
        else:
            tambahdata=Msatuan(
                satuankode=satuankode.upper(),
                satuannama=satuannama.upper(),
            )
            tambahdata.save()
            messages.success(request,'Berhasil Tambah Data Satuan')
    elif method == 'edit':
        satuankode = request.POST['satuankode']
        satuannama = request.POST['satuannama']

        satuan=Msatuan.objects.get(satuankode=satuankode)

        satuan.satuannama=satuannama.upper()
        satuan.save()
        messages.success(request,'Data anda telah di udah')
    return redirect('mbrg_satuan')
@login_required()
def mbrg_satuan_delete(request,satuankode):
    Msatuan.objects.get(satuankode=satuankode).delete()
    messages.success(request,'Data anda telah terhapus')
    return redirect('mbrg_satuan')
@login_required()
def mbrg_jenisbrg(request):
    judul='Data Jenis Barang'
    context={
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010300',
        'mjenis':Mbrgjns.objects.all(),
        'judul':judul
    }
    return render(request,'datainduk/mbrg_jenisbrg/index.html', context)
@login_required()
def mbrg_jenisbrg_form(request,method):
    if method == 'tambah':
        data = []
        judul ='Tambah Jenis Barang'
    elif method == 'edit':
        brgjnskode=request.GET['brgjnskode']
        data = Mbrgjns.objects.get(brgjnskode=brgjnskode)
        judul = 'Edit Jenis Barang'
    context = {
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010300',
        'method': method,
        'judul': judul,
        'data': data,
    }
    return render(request,'datainduk/mbrg_jenisbrg/form.html',context)
@login_required()
def mbrg_jenisbrg_post(request,method):
    if method == 'tambah':
        brgjnskode = request.POST['brgjnskode']
        brgjnsnama = request.POST['brgjnsnama']
        groupkode = request.POST['groupkode']
        if Mbrgjns.objects.filter(brgjnskode=brgjnskode).exists():
            messages.error(request, 'Kode Jenis Barang Sudah Di Gunakan')
            return redirect('mbrg_jenisbrg')
        else:
            tambahdata = Mbrgjns(
                brgjnskode=brgjnskode,
                brgjnsnama=brgjnsnama,
                groupkode=groupkode
            )
            tambahdata.save()
            messages.success(request, 'Berhasil Tambah Data Jenis Barang')
    elif method == 'edit':
        brgjnskode = request.POST['brgjnskode']
        brgjnsnama = request.POST['brgjnsnama']
        groupkode = request.POST['groupkode']

        mbrg_jenisbrg = Mbrgjns.objects.get(brgjnskode=brgjnskode)

        mbrg_jenisbrg.brgjnsnama = brgjnsnama
        mbrg_jenisbrg.groupkode=groupkode
        mbrg_jenisbrg.save()
        messages.success(request, 'Data anda telah di udah')
    return redirect('mbrg_jenisbrg')
@login_required()
def mbrg_jenisbrg_delete(request,brgjnskode):
    Mbrgjns.objects.get(brgjnskode=brgjnskode).delete()
    messages.success(request, 'Data anda telah terhapus')
    return redirect('mbrg_jenisbrg')

@login_required()
def mbrg_pabrik(request):
    judul='Data Pabrik'
    context={
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010500',
        'mpabrik':Mpabrik.objects.all(),
        'judul':judul
    }
    return render(request,'datainduk/mbrg_pabrik/index.html', context)
@login_required()
def mbrg_pabrik_form(request,method):
    if method == 'tambah':
        data = []
        judul ='Tambah Data Pabrik'
    elif method == 'edit':
        pabrikkode=request.GET['pabrikkode']
        data=Mpabrik.objects.get(pabrikkode=pabrikkode)
        judul='Edit Data Pabrik'

    context = {
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010500',
        'method': method,
        'judul':judul,
        'data':data
     }
    return render(request, 'datainduk/mbrg_pabrik/form.html', context)
@login_required()
def mbrg_pabrik_post(request,method):
    if method == 'tambah':
        pabrikkode =request.POST['pabrikkode']
        pabriknama= request.POST['pabriknama']
        if Mpabrik.objects.filter(pabrikkode=pabrikkode).exists():
            messages.error(request,'Kode Satuan Sudah Di Gunakan')
            return redirect('mbrg_pabrik')
        else:
            tambahdata=Mpabrik(
                pabrikkode=pabrikkode,
                pabriknama=pabriknama,
            )
            tambahdata.save()
            messages.success(request,'Berhasil Tambah Data Satuan')
    elif method == 'edit':
        pabrikkode = request.POST['pabrikkode']
        pabriknama = request.POST['pabriknama']

        pabrik=Mpabrik.objects.get(pabrikkode=pabrikkode)

        pabrik.pabriknama=pabriknama
        pabrik.save()
        messages.success(request,'Data anda telah di udah')
    return redirect('mbrg_pabrik')
@login_required()
def mbrg_pabrik_delete(request,pabrikkode):
    Mpabrik.objects.get(pabrikkode=pabrikkode).delete()
    messages.success(request,'Data anda telah terhapus')
    return redirect('mbrg_pabrik')
def mbrg_group(request):
    judul='Data Group'
    context={  
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010200',
        'mgroup':Mgroup.objects.all(),
        'judul':judul
    }
    return render(request,'datainduk/mbrg_group/index.html',context)
def mbrg_group_form(request,method):  
    if method == 'tambah':
        data = []
        judul ='Tambah Data Group'
    elif method == 'edit':
        groupkode=request.GET['groupkode']
        data=Mgroup.objects.get(groupkode=groupkode)
        judul='Edit Data Group'

    context = {
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010200',
        'method': method,
        'judul':judul,
        'data':data
     }
    return render(request, 'datainduk/mbrg_group/form.html', context)

def mbrg_group_post(request,method):
    if method=='tambah':
        groupkode=request.POST['groupkode']
        groupnama=request.POST['groupnama']
        if Mgroup.objects.filter(groupkode=groupkode).exists():
            messages.error(request,'Kode Group Sudah Di Gunakan')
            return redirect(mbrg_group)
        else :
            tambah = Mgroup(groupkode=groupkode, groupnama=groupnama)
            tambah.save()
            messages.success(request,'Berhasil Tambahkan Data Group')
    elif method == 'edit':
        groupkode=request.POST['groupkode']
        groupnama=request.POST['groupnama']
        
        group = Mgroup.objects.get(groupkode=groupkode)
        group.groupnama=groupnama
        group.save()
        messages.success(request,'Data anda telah di udah')
    return redirect(mbrg_group)

def mbrg_group_delete(request, groupkode):
    Mgroup.objects.get(groupkode=groupkode).delete()
    messages.success(request,'Data anda telah terhapus')
    return redirect('mbrg_group')
