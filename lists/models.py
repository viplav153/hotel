from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class List(models.Model):
    city = models.CharField(max_length=25)
    state = models.TextField()
    available_date = models.DateField()
    image = models.ImageField(upload_to='image/')
    hotel_name=models.CharField(max_length=100)
    

    def __str__(self):
        return self.hotel_name
    

    
    