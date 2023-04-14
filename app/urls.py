from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name=''),
    path('login', views.login, name='login'),
    path('login_post', views.login_post, name='login_post'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]
