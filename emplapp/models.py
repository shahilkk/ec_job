from django.db import models
from userapp.models import Login
# Create your models here


class Gallery(models.Model):
    login = models.ForeignKey(Login,on_delete=models.CASCADE )
    picture = models.ImageField(upload_to='Display_images/',  blank = True, null = True)