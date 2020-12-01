from django.dispatch import receiver
from django.db.models.signals import pre_save
from main.models import Product
from utils.main import unique_slug_generator


@receiver(pre_save, sender=Product)
def create_product_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, for_=instance.title)