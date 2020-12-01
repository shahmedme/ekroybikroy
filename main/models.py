from django.db import models
from django.contrib.auth.models import User
from account.models import Profile


class Location(models.Model):
    LOCATION_CHOICES = [
        ('division', 'Division'),
        ('district', 'District'),
        ('thana', 'Thana'),
        ('city', 'City'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(
        upload_to="main/categories")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CONDITION_CHOICES = [
        ('used', 'Used'),
        ('new', 'New')
    ]

    title = models.CharField(max_length=500)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.FloatField()
    is_negotiable = models.BooleanField(default=False)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    contact = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Photo(models.Model):
    file = models.ImageField(upload_to='main/products')
    is_primary = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title


class SiteInfo(models.Model):
    name = models.CharField(max_length=20)
    tagline = models.CharField(max_length=50)
    sub_tagline = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='main/sites')
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
