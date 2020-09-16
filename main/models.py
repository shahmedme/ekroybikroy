from django.db import models
from ckeditor.fields import RichTextField
from account.models import Profile


class Location(models.Model):
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)

    def __str__(self):
        return self.division + ',' + self.district + ',' + self.thana


class Category(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(
        upload_to="main/categories", max_length="100")

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
    is_negotiable = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='main/products')
    timestamp = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=15)
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
