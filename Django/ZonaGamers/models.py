from django.db import models

#Integrar con el modelo de django para seguridad
class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=80)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    password = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return (
            str(self.nombre)
            + " " +
            str(self.apellido_paterno)
            + " " +
            str(self.apellido_materno)
        )
    
   

class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    descripcion = models.TextField(max_length=100)  

    def __str__(self):
        return (
            str(self.producto_id)
            + " " +
            str(self.nombre)
            + " - " +
            str(self.precio)
        )

            
class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)  
    fecha_pedido = models.DateTimeField(auto_now_add=True) 
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2)  
    cantidad = models.CharField(max_length=50)
    
    

    def __str__(self):
        return (
            str(self.pedido_id)
            + " - " +
            str(self.cliente)
            + " - " +
            str(self.total_pedido)
            + " - " +
            str(self.cantidad)
        )
   
    
# Create your models here.
