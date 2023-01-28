from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length = 100)