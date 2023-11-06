from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact_view, name='contact'),
    path('area-aluno/', views.area_restrita, name='area_aluno'),
]
