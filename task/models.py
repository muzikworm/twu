from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    aadhar = models.IntegerField(unique=True)
    area = models.CharField(max_length=200)
    amount = models.IntegerField()


