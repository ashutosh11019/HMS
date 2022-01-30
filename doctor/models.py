from django.db import models
from django.contrib.auth.models import User

# Create your models here.
chioce_opt=(('Patient','Patient'),('Doctor','Doctor'))

class Doctor_Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    First_name = models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dob = models.DateField()
    contact_no = models.CharField(max_length=20)
    designation = models.CharField(max_length=50,choices=chioce_opt)
    verify = models.BooleanField(default=False)
