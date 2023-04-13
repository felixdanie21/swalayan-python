from django.urls import path
from app.views import blank
from . import views

urlpatterns = [
    path('', blank, name='laporan')
]
