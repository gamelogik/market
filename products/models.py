from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)  # (unique=True)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=9.99, null=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=6.99, null=True, blank=True)

    def __unicode__(self):
        return self.title

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(product_pre_save_reciever, sender=Product)
#
# def product_post_save_reciever(sender, instance, *args, **kwargs):
#     if instance.slug != slugify(instance.title):
#         instance.slug = slugify(instance.title)
#         instance.save()
#
# pre_save.connect(product_post_save_reciever, sender=Product)

