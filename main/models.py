from django.db import models
from ckeditor.fields import RichTextField
from account.models import Profile


class Division(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)


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
    address = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    price = models.FloatField()
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    is_negotiable = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='main/products')
    timestamp = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    short_desc = models.TextField()
    desc = RichTextField()
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    img_url = models.ImageField(upload_to='main/products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class SiteInfo(models.Model):
    name = models.CharField(max_length=20)
    tagline = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='main/sites')
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=50)
    facebook = models.CharField(max_length=20)
    instagram = models.CharField(max_length=20)
    youtube = models.CharField(max_length=20)
