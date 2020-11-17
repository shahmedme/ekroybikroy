from django.contrib import admin
from main.models import *

class PhotoAdmin(admin.StackedInline):
    model = Photo

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SiteInfo)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Product

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass