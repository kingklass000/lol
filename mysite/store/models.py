from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    have = models.BooleanField(default=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

class Productphotos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.product_name

class Comment(models.Model):
    name = models.CharField(max_length=16)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.product}'