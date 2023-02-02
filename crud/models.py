from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length = 14)
    photo = models.ImageField(upload_to= "myimage")
    date = models.DateTimeField(auto_now_add= True)