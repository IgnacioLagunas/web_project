from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index,name="index"),
    path ("about", views.about,name="about"),
    path ("carrito", views.carrito,name="carrito"),
    path ("login", views.login,name="login"),
    path ("formulario", views.formulario,name="formulario"),
    path ("producto_spiders", views.producto_spider,name="producto_spider"),
    path ("crud",views.crud,name="crud"),
    

]
