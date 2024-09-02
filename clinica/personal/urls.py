from django.urls import path
from personal import views


urlpatterns = [
    path('', views.listar_empleados, name='empleados'),
]