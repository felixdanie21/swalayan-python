from django.urls import path
from app.views import blank
from . import views

urlpatterns = [
    path('', views.index, name="developer"),
    path('import_csv', views.import_csv, name="import_csv"),
    path('import_csv_post', views.import_csv_post, name="import_csv_post"),
    path('contoh_form', views.contoh_form, name="contoh_form"),
    path('contoh_table', views.contoh_table, name="contoh_table"),
]
