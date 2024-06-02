from django.shortcuts import render

# Create your views here.

def index(request):
    context = {} 
    return render(request,'pages/index.html',context)

def about(request):
    context = {} 
    return render(request,'pages/about.html',context)

def carrito(request):
    context = {} 
    return render(request,'pages/carrito.html',context)

def login(request):
    context = {} 
    return render(request,'pages/login.html',context)

def formulario(request):
    context = {} 
    return render(request,'pages/formulario.html',context)

def producto_spider(request):
    context = {} 
    return render(request,'pages/producto_spider.html',context)




