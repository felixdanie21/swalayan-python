from django.urls import path
from app.views import blank
from . import views

urlpatterns = [
    path('', views.index, name='pendataan'),
    path('tjua_piutang', blank, name='tjua_piutang'),
    path('tjua_return', blank, name='tjua_return'),
    path('tjua_poinmember', blank, name='tjua_poinmember'),
    path('tbli_terima', blank, name='tbli_terima'),
    path('tbli_faktur', blank, name='tbli_faktur'),
    path('tbli_hutang', blank, name='tbli_hutang'),
    path('tbli_return', blank, name='tbli_return'),
    path('tbli_order', blank, name='tbli_order'),
    path('stok_mutasi', blank, name='stok_mutasi'),
    path('stok_deviasi', blank, name='stok_deviasi'),
    path('stok_opname', blank, name='stok_opname'),
    path('info_harga', blank, name='info_harga'),
    path('info_supplier', blank, name='info_supplier'),
    path('info_stock', blank, name='info_stock'),
    path('info_history', blank, name='info_history'),
    path('info_perubahan', blank, name='info_perubahan'),
    path('info_tidaklaku', blank, name='info_tidaklaku'),
    path('tacc_jurnalumum', blank, name='tacc_jurnalumum'),
    path('tacc_jurnaltrans', blank, name='tacc_jurnaltrans'),
    path('tacc_neracaawal', blank, name='tacc_neracaawal'),
    path('tpjk_pphmasabln', blank, name='tpjk_pphmasabln'),
    path('tpjk_ppnmasukan', blank, name='tpjk_ppnmasukan'),
    path('tpjk_ppnkeluaran', blank, name='tpjk_ppnkeluaran'),
    path('tpjk_pph21', blank, name='tpjk_pph21'),
    path('tpjk_spttahunan', blank, name='tpjk_spttahunan'),
]
