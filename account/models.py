from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='main/profiles')
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Customer_details(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=30, null=True)
    c_password = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.first_name
