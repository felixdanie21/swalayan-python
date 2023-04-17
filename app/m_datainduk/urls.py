from django.urls import path
from app.views import blank
from . import views

urlpatterns = [
    path('', views.index, name='data induk'),
    path('mbrg_databarang', blank, name='mbrg_databarang'),
    path('mbrg_group', views.mbrg_group, name='mbrg_group'),
    path('mbrg_group_form/<str:method>', views.mbrg_group_form, name='mbrg_group_form'),
    path('mbrg_group_post/<str:method>', views.mbrg_group_post, name='mbrg_group_post'),
    path('mbrg_group_delete/<str:groupkode>',views.mbrg_group_delete, name='mbrg_group_delete'),
    path('mbrg_jenisbrg', views.mbrg_jenisbrg, name='mbrg_jenisbrg'),
    path('mbrg_jenisbrg_form/<str:method>',views.mbrg_jenisbrg_form,name='mbrg_jenisbrg_form'),
    path('mbrg_jenisbrg_post/<str:method>', views.mbrg_jenisbrg_post, name='mbrg_jenisbrg_post'),
    path('mbrg_jenisbrg_delete/<str:brgjnskode>', views.mbrg_jenisbrg_delete, name='mbrg_jenisbrg_delete'),
    path('mbrg_satuan', views.mbrg_satuan, name='mbrg_satuan'),
    path('mbrg_satuan_form/<str:method>',views.mbrg_satuan_form, name='mbrg_satuan_form'),
    path('mbrg_satuan_post/<str:method>',views.mbrg_satuan_post, name='mbrg_satuan_post'),
    path('mbrg_satuan_delete/<str:satuankode>',views.mbrg_satuan_delete, name='mbrg_satuan_delete'),
    path('mbrg_pabrik', views.mbrg_pabrik, name='mbrg_pabrik'),
    path('mbrg_pabrik_form/<str:method>', views.mbrg_pabrik_form, name='mbrg_pabrik_form'),
    path('mbrg_pabrik_post/<str:method>', views.mbrg_pabrik_post, name='mbrg_pabrik_post'),
    path('mbrg_pabrik_delete/<str:pabrikkode>', views.mbrg_pabrik_delete, name='mbrg_pabrik_delete'),
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
