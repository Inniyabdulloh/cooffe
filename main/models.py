from django.db import models

# Create your models here.

class CoffeeOffer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')


class CustomersReview(models.Model):
    first_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    review = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()


