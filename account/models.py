from django.db import models


class Profile(models.Model):
    avatar = models.ImageField(upload_to='main/profiles')
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
