from django.db import models

product_types = (
    ('p', 'Physical'),
    ('d', 'Digital')
)

class ProductCategory(models.Model):
    category_name = models.CharField(null=False, max_length=128)
    short_description = models.TextField(max_length=255)
    description = models.TextField(blank=True)
    featured_image = models.ImageField()
    slug = models.SlugField()
    is_available = models.BooleanField()

class ProductType(models.Model):
    key_type = models.CharField(max_length=1)
    display_name = models.CharField(null=False, max_length=255)

class Product(models.Model):
    product_name = models.CharField(null=False, max_length=255)
    short_description = models.TextField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0)
    type = models.ForeignKey(choices=product_types, on_delete=models.CASCADE, to=ProductType)
    # discount_price = models.FloatField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField()
    in_stock = models.BooleanField(default=False)
    stock_quantity = models.IntegerField(default=0, null=False)
    featured_image = models.ImageField()
    gallery_image_1 = models.ImageField()
    gallery_image_2 = models.ImageField()
    gallery_image_3 = models.ImageField()
    gallery_image_4 = models.ImageField()
    gallery_image_5 = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)