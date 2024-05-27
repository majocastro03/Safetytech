from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=10, null=True, blank=True)
    archivo = models.ImageField(upload_to='users/', null=True, default='users/default.png')
    bio = models.TextField(max_length=400, null=True, blank=True)

    # Re-definimos groups y user_permissions con un related_name único
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="usuario_groups_set",  # Nombre único para related_name
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="usuario_user_permissions_set",  # Nombre único para related_name
        related_query_name="usuario",
    )

from django.core.validators import FileExtensionValidator
class Empleado(models.Model):
    codEmpleado=models.CharField(max_length=3, primary_key=True, unique=True, verbose_name="Codigo Empleado")
    Identificacion=models.CharField(max_length=12)
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    email=models.EmailField(max_length=50, verbose_name="Email")
    cargos= [
        ("R", "Rector"),
        ("CA", "Coordinador Academico"),
        ("CC", "Coordinador Convivencia"),
        ("P", "Profesor"),
        ("S", "Secretaria"),
    ]
    cargo=models.CharField(max_length=40, choices=cargos, default="P", verbose_name="Cargo")
    fecha_registro=models.DateField(default=timezone.now, null=True, verbose_name="Fecha de Registro")
    archivo=models.FileField(upload_to='media/', null=True, verbose_name="Imagen")
    archivo_pdf = models.FileField(upload_to='media/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="PDF")
    codadmin=models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Codigo Admin")

    def __str__(self):
        txt="{0} (Nombre: {1}, Cargo: {2})"
        return txt.format(self.codEmpleado, self.nombre, self.cargo)

class Instalacion(models.Model):
    codInstalacion=models.CharField(max_length=3, primary_key=True, verbose_name="Codigo Instalacion")
    nombre=models.CharField(max_length=40, verbose_name="Nombre")
    fecha_instalacion=models.DateField(default=timezone.now, null=True, verbose_name="Fecha Instalacion")

    def __str__(self):
        txt="{0} (Nombre: {1}, fecha: {2})"
        return txt.format(self.codInstalacion, self.nombre, self.fecha_instalacion)

class Bitacora(models.Model):
    codBitacora=models.CharField(max_length=3, primary_key=True, verbose_name="Codigo Bitacora")
    nombre=models.CharField(max_length=40, verbose_name="Nombre")
    estado=models.CharField(max_length=15, verbose_name="Estado")
    cantidad=models.CharField(max_length=10, verbose_name="Cantidad")
    observaciones=models.CharField(max_length=100, verbose_name="Observaciones")
    ubicacion=models.CharField(max_length=40, verbose_name="Ubicacion")
    riesgo=[
        ("B", "Bajo"),
        ("A", "Alto"),
    ]
    nivel_riesgo=models.CharField(max_length=20, choices=riesgo, default="B", verbose_name="Nivel de Riesgo")
    fecha_cambio=models.DateField(default=timezone.now, null=True, verbose_name="Fecha de Cambio")
    codInstalacion=models.ForeignKey(Instalacion, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Codigo Instalacion")

    def __str__(self):
        txt="{0} (Nombre: {1}, Ubicacion: {2})"
        return txt.format(self.codBitacora, self.nombre, self.ubicacion)

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
