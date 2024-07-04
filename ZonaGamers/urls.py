from django.urls import path
from .views import render_views, carrito_views

urlpatterns = [

    #  Render views
    path ("", render_views.index,name="index"),
    path ("about", render_views.about,name="about"),
    path ("carrito", render_views.carrito,name="carrito"),
    path ("catalogo", render_views.catalogo,name="catalogo"),
    path ("login", render_views.login,name="login"),
    path ("formulario", render_views.formulario,name="formulario"),
    path ("producto_spiders", render_views.producto_spider,name="producto_spider"),
    path ("crud", render_views.crud,name="crud"), 

    # Carrito views
    path ("add_to_cart/<int:id>", carrito_views.add_to_cart,name="add_to_cart"),
    path ("remove_from_cart/<int:id>", carrito_views.remove_from_cart,name="remove_from_cart"),
]
