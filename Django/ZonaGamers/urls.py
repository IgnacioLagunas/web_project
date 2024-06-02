from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index,name="index"),
    path ("", views.index,name="about"),
    path ("", views.index,name="carrito"),
    path ("", views.index,name="login"),
    path ("", views.index,name="formulario"),
    path ("", views.index,name="producto_spider"),

]
