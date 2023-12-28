from django.db import models
import datetime
import os
from django.contrib.auth.models import User


def getFileName(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,null=False)
    image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name
    
class Products(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False)
    seller = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    orginal_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    bestseller = models.BooleanField(default=False,help_text="0-default,1-bestseller")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    product_quantity = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.user.username}"

    @property
    def total_cost(self):
        return self.product_quantity*self.products.selling_price


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
