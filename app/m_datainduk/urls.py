from django.urls import path
from app.views import blank
from . import views

urlpatterns = [
    path('', views.index, name='data induk'),
    path('mbrg_databarang', blank, name='mbrg_databarang'),
    path('mbrg_group', blank, name='mbrg_group'),
    path('mbrg_jenisbrg', blank, name='mbrg_jenisbrg'),
    path('mbrg_satuan', blank, name='mbrg_satuan'),
    path('mbrg_pabrik', blank, name='mbrg_pabrik'),
    path('msup_supplier', blank, name='msup_supplier'),
    path('msup_barang', blank, name='msup_barang'),
    path('memb_datamember', blank, name='memb_datamember'),
    path('memb_poinbarang', blank, name='memb_poinbarang'),
    path('memb_hadiah', blank, name='memb_hadiah'),
    path('macc_dataakun', blank, name='macc_dataakun'),
    path('macc_kodejurnal', blank, name='macc_kodejurnal'),
    path('mdum_gudang', blank, name='mdum_gudang'),
    path('mdum_aturjual', blank, name='mdum_aturjual'),
    path('mdum_dscperiode', blank, name='mdum_dscperiode'),
]
