from django.urls import path
from ipsoftapp import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('ipsoftapp/', views name='pacientes')
]