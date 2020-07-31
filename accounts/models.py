from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    profile_pic=models.ImageField(default='initial_image.png',null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
                ('Indoor' , 'Indoor'),
                ('Outdoor' , 'Outdoor'),
                ('Unavailable' , 'Unavailable'),
                ('Others','Others')
             )

    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField(Tags)


    def __str__(self):
        return self.name

class Orders(models.Model):
    STATUS=(
        ('Pending' , 'Pending'),
        ('Delivered' , 'Delivered'),
        ('Out For Delivery' , 'Out For Delivery'),
        ('Delayed' , 'Delayed'),
        ('Cancelled' , 'Cancelled'),
        ('Out Of Stock' , 'Out Of Stock'),
        ('Other' , 'Other'),
        )
    customer=models.ForeignKey(Customer, null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product , null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status =  models.CharField(max_length=200, null=False ,choices=STATUS)
    def __str__(self):
        return self.status
