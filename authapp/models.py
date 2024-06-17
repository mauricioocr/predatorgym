from django.db import models

# Create your models here.

class Contacto(models.Model):
    Nombre=models.CharField(max_length=25)
    Email=models.EmailField()
    Telefono=models.CharField(max_length=12)
    Descripcion=models.TextField()    
    def __str__(self):
        return self.Email

class Usuario(models.Model):
    NombreCompleto = models.CharField(max_length=25)
    Cedula = models.IntegerField(max_length=8,blank=True,null=True)
    Email = models.EmailField()
    Telefono = models.CharField(max_length=12)
    FechaNacimiento = models.CharField(max_length=50)
    SeleccionarMembresia = models.CharField(max_length=200)
    SeleccionarEntrenador = models.CharField(max_length=55)
    Direccion = models.TextField()
    EstadoDePago = models.CharField(max_length=55, blank=True,null=True)
    Precio = models.IntegerField(max_length=55, blank=True,null=True)
    FechaVencimiento = models.DateTimeField(blank=True,null=True) 
    SelloDeTiempo = models.DateTimeField(auto_now_add=True,blank=True)   
    def __str__(self):
        return f'{self.NombreCompleto} - {self.Cedula}'

class Entrenadore(models.Model):
    Nombre = models.CharField(max_length=55)
    Genero = models.CharField(max_length=25)
    Telefono = models.CharField(max_length=25)
    Salario = models.IntegerField(max_length=25)
    SelloDeTiempo = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.Nombre

class Membresia(models.Model):
    Plan = models.CharField(max_length=185)
    Precio = models.IntegerField(max_length=55)
    def __int__(self):
        return self.id

class Asistencia(models.Model):
    Usuario=models.CharField(max_length=15)
    Fecha=models.DateField(auto_now_add=True)
    InicioSesion=models.CharField(max_length=200)
    FinSesion=models.CharField(max_length=200)
    Entrenamiento=models.CharField(max_length=200)
    def __int__(self):
        return self.id
