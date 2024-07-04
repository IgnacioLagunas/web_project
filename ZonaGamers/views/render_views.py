from django.shortcuts import render
from django.urls import reverse
from ..models import Usuario, Carrito, Juego, CarritoJuego
# Create your views here.
# Genera la URL para la vista 'detalle_hotel' con id=1
#rl = reverse('index', args=[1])

# Imprime la URL generada
#print(url)

def index(request):
    context = {
        "user": ""
    } 
    return render(request,'pages/index.html',context)
    
def catalogo(request):
    juegos = Juego.objects.all()
    context = {
        "juegos": juegos
    } 
    return render(request,'pages/catalogo.html',context)
    

def about(request):
    context = {} 
    return render(request,'pages/about.html',context)

def carrito(request):
    carrito = CarritoJuego.objects.filter(carrito=1)
    total = 0
    for item in carrito:
        item.total = item.juego.precio * item.cantidad
        total += item.total
    carrito.total = total
    context = {'carrito': carrito} 
    return render(request, 'pages/carrito.html', context)

def login(request):
    context = {} 
    return render(request,'pages/login.html',context)

def formulario(request):
    context = {} 
    return render(request,'pages/formulario.html',context)

def producto_spider(request):
    context = {} 
    return render(request,'pages/producto_spider.html',context)

def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "pages/crud.html", context)

    





