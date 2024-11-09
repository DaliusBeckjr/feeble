from django.db import models
from user.models import User
from PIL import Image
from server.settings import BASE_DIR



class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.ImageField(upload_to= 'product/images' ) # want to lead it back to product app folder and create an images folder to stay organized
    


"""
    the order model is more for a shopping cart feature so the idea here is
    that a user can order multiple products and the order model will store it
    in a list of products...one order many products (one to many)
"""
class Order(models.Model):
    pass


class Review(models.Model):
    pass