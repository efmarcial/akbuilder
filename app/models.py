from ast import mod
from turtle import back
from django.db import models

# Create your models here.
class GalleryImage(models.Model):

    customer = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True)
    

    def __str__(self) -> str:
        return self.customer

class Video(models.Model):

    customer = models.CharField(max_length=100, null=True)
    video = models.FileField(upload_to='videos/', null=True)

    def __str__(self) -> str:
        return self.customer

class Testimonial(models.Model):

    customer = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.customer

class Service(models.Model):

    service = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.service

class Contact(models.Model):

    fullname = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20, null=True)
    message = models.CharField(max_length=500, null=True)

