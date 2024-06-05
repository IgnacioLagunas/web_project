from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index,name="index"),
    path ("", views.about,name="about"),
    path ("", views.carrito,name="carrito"),
    path ("", views.login,name="login"),
    path ("", views.formulario,name="formulario"),
    path ("", views.producto_spider,name="producto_spider"),
    path ("crud",views.crud,name="crud"),
    

]
