from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.decorators import login_required
from app.utilities import ambil_menu
from app.models import Msatuan,Mbrgjns,Mpabrik,Mgroup,Mbarang
from django.contrib import messages
import json

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
        group=Mgroup.objects.all()
        judul ='Tambah Jenis Barang'
    elif method == 'edit':
        group=Mgroup.objects.all()
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
        'group': group
    
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
            messages.error(request,'Kode Pabrik Sudah Di Gunakan')
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
@login_required()
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
@login_required()
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

@login_required()
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
@login_required()
def mbrg_group_delete(request, groupkode):
    Mgroup.objects.get(groupkode=groupkode).delete()
    messages.success(request,'Data Group Telah Dihapus')
    return redirect('mbrg_group')
@login_required()
def mbrg_databarang(request):
    judul='Data Barang'
    jenisbarang = Mbarang.objects.extra(
        select={
            'brgjnsnama': 'mbrgjns.brgjnsnama',
            'satuannama': 'msatuan.satuannama',
        },
        tables=['mbrgjns', 'msatuan'],
        where=[
            'mbrgjns.brgjnskode = mbarang.brgjnskode',
            'msatuan.satuankode = mbarang.satuankode',
        ]
    ) 
    context = {
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010100',
        'mbarang':jenisbarang,
        'judul':judul
    }
    return render(request,'datainduk/mbrg_databarang/index.html', context)
@login_required()
def mbrg_databarang_form(request, method):
    if method == 'tambah':
        data=[]
        judul='Tambah Data Barang'
        jenisbarang=Mbrgjns.objects.all()
        satuanbarang=Msatuan.objects.all()
    elif method=='edit':
        jenisbarang=Mbrgjns.objects.all()
        satuanbarang=Msatuan.objects.all()
        kodebarang=request.GET['barangkode']
        data=Mbarang.objects.get(barangkode=kodebarang)
        judul='Edit Data Barang'
    context = {
        'dbmenu': ambil_menu('c'),
        'parent_segment': 'C010000',
        'segment': 'C010100',
        'data':data,
        'jenisbarang': jenisbarang,
        'satuanbarang': satuanbarang,
        'method': method,
        'judul':judul
    }
    return render(request,'datainduk/mbrg_databarang/form.html',context)

def mbrg_databarang_post(request,method):
    if method == 'tambah':
        brgnama= request.POST['brgnama']
        brgkode= request.POST['brgkode']
        brgjnskode= request.POST['brgjnskode']
        baranghrgbppn = request.POST['baranghrgbppn']
        satuankode= request.POST['satuankode']
        baranghrgsppn= request.POST['baranghrgsppn']
        barangterakhir = request.POST['barangterakhir']
        baranghrgpokok= request.POST['baranghrgpokok']
        baranghrgkhusus= request.POST['baranghrgkhusus']
        barangjumsat = request.POST['barangjumsat']
        barangtglbliakh = request.POST['barangtglbliakh']
        barangupdate= request.POST['barangupdate']
        barangstatpoin= request.POST['barangstatpoin']
        barangbarcode= request.POST['barangbarcode']
        if Mbarang.objects.filter(barangkode=brgkode).exists():
            messages.error(request,'Kode Barang Sudah Di Gunakan')
            return redirect('mbrg_databarang')
        else:
            tambah = Mbarang(barangkode=brgkode,barangnama=brgnama,brgjnskode=brgjnskode,satuankode=satuankode,barangbarcode=barangbarcode,baranghrgbppn=baranghrgbppn,baranghrgsppn=baranghrgsppn,barangterakhir=barangterakhir,baranghrgpokok=baranghrgpokok,baranghrgkhusus=baranghrgkhusus,barangjumsat=barangjumsat,barangtglbliakh=barangtglbliakh,barangupdate=barangupdate,barangstatpoin=barangstatpoin)
            tambah.save()
            messages.success(request,'Berhasil Di Tambah ')
    elif method == 'edit':
        brgnama= request.POST['brgnama']
        brgkode= request.POST['brgkode']
        brgjnskode= request.POST['brgjnskode']
        baranghrgbppn = request.POST['baranghrgbppn']
        satuankode= request.POST['satuankode']
        baranghrgsppn= request.POST['baranghrgsppn']
        barangterakhir = request.POST['barangterakhir']
        baranghrgpokok= request.POST['baranghrgpokok']
        baranghrgkhusus= request.POST['baranghrgkhusus']
        barangjumsat = request.POST['barangjumsat']
        barangtglbliakh = request.POST['barangtglbliakh']
        barangupdate= request.POST['barangupdate']
        barangstatpoin= request.POST['barangstatpoin']
        barangbarcode= request.POST['barangbarcode']

        barang = Mbarang.objects.get(barangkode=brgkode)
        barang.barangnama=brgnama
        barang.brgjnskode=brgjnskode
        barang.satuankode=satuankode
        barang.barangbarcode=barangbarcode
        barang.baranghrgpokok=baranghrgpokok
        barang.baranghrgbppn=baranghrgbppn
        barang.baranghrgsppn=baranghrgsppn
        barang.baranghrgkhusus=baranghrgkhusus
        barang.barangjumsat=barangjumsat
        barang.barangtglbliakh=barangtglbliakh
        barang.barangupdate=barangupdate
        barang.barangstatpoin=barangstatpoin
        barang.save()
        messages.success(request,'Barang Berhasil di ubah')
    return redirect('mbrg_databarang')
def mbrg_databarang_delete(request ,barangkode):
    Mbarang.objects.get(barangkode=barangkode).delete()
    messages.success(request,'Data Barang Telah Dihapus')
    return redirect('mbrg_databarang')