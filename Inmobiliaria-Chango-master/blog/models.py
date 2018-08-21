from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    antiguedad = models.CharField(max_length=100)
    servicios = models.TextField()
    zona = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    alquiler = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    archivo = models.FileField(upload_to='documents/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Property(models.Model):
    address = models.TextField()

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images')
    image = models.ImageField()
