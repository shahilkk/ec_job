from email import message
from email.mime import image
from email.policy import default
from inspect import classify_class_attrs
from unicodedata import category
from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=30) 
    userpassword = models.CharField(max_length=30) 
    usertype = models.CharField(max_length=30) 
    status = models.BooleanField(default=False)
    mode = models.CharField(max_length=30)

class UserDetails(models.Model):
    userlogin = models.ForeignKey(Login,on_delete=models.CASCADE )
    name = models.CharField(max_length=30) 
    phone = models.BigIntegerField()
    email =  models.CharField(max_length=30) 
    profilePic = models.ImageField(  blank = True, null = True,default='default.jpg')
    pincode = models.IntegerField()
    address = models.TextField()

class WorkerDetails(models.Model):
    workerlogin = models.ForeignKey(Login,on_delete=models.CASCADE )
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)
    w_email =  models.CharField(max_length=30)
    w_phone = models.BigIntegerField()
    w_profilePic = models.ImageField(upload_to='Worker_images/' ,blank=True,null=True)
    jobtype = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    subcategory = models.CharField(max_length=30)
    w_address = models.TextField()
    additional_information =models.TextField()
    date_of_birth = models.DateField()
    age = models.IntegerField()
    w_pincode = models.IntegerField()
    place = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    education_qualification = models.CharField(max_length=30)



class Quick_booking(models.Model):
    login = models.ForeignKey(UserDetails,on_delete=models.CASCADE )
    landmark = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()

class Booking(models.Model):
    user = models.ForeignKey(UserDetails,on_delete=models.CASCADE )
    worker = models.ForeignKey(WorkerDetails,on_delete=models.CASCADE )
    date = models.DateField()
    time = models.TimeField()

class Review(models.Model):
    login_user = models.ForeignKey(UserDetails,on_delete=models.CASCADE )
    worker = models.ForeignKey(WorkerDetails,on_delete=models.CASCADE )
    details = models.TextField()
    


class Package(models.Model):
    user = models.ForeignKey(UserDetails,on_delete=models.CASCADE )
    selected_Package = models.CharField(max_length=30)


class Contact(models.Model):
    user = models.ForeignKey(UserDetails,on_delete=models.CASCADE )
    message=models.CharField(max_length=300)