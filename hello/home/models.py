from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)


    def __str__(self):
        return self.name
class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Filter_Price(models.Model):
    FILTER_PRICE = (

        ('1000 TO 10000' , '1000 TO 10000'),
        ('10000 TO 20000' , '10000 TO 20000'),
        ('20000 TO 50000' , '20000 TO 50000'),
        ('50000 TO 100000' , '50000 TO 100000'),
        
    )

    price = models.CharField(choices=FILTER_PRICE,max_length=200)

    def __str__(self):
        return self.price
    

class Product(models.Model):
    CONDITION = (('New', 'New'),('Old','Old'))
    STOCK = (('IN STOCK', 'IN STOCK'),('OUT OF STOCK' , 'OUT OF STOCK'))
    STATUS = (('Publish','Publish'),('Draft','Draft'))
    unique_id = models.CharField(unique=True , max_length=200 , null=True ,blank=True)
    image = models.ImageField(upload_to='shop/images' , default="")
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION,max_length=200)
    information = models.TextField()
    description = models.TextField()
    stock = models.CharField(choices=STOCK,max_length=200)
    status = models.CharField(choices=STATUS,max_length=200)
    created_date = models.CharField(default=timezone.now  , max_length=200)
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE)


    def save(self , *args , **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args , **kwargs)


    def __str__(self):
        return self.name
class Productone(models.Model):
    CONDITION = (('New', 'New'),('Old','Old'))
    STOCK = (('IN STOCK', 'IN STOCK'),('OUT OF STOCK' , 'OUT OF STOCK'))
    STATUS = (('Publish','Publish'),('Draft','Draft'))
    unique_id = models.CharField(unique=True , max_length=200 , null=True ,blank=True)
    image = models.ImageField(upload_to='shop/images' , default="")
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION,max_length=200)
    information = models.TextField()
    description = models.TextField()
    stock = models.CharField(choices=STOCK,max_length=200)
    status = models.CharField(choices=STATUS,max_length=200)
    created_date = models.CharField(default=timezone.now  , max_length=200)
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE)
    
    def save(self , *args , **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args , **kwargs)


    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='shop/images' , default="")
    product = models.ForeignKey(Product , on_delete=models.CASCADE)

    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Imagess(models.Model):
    image = models.ImageField(upload_to='shop/images' , default="")
    product = models.ForeignKey(Productone , on_delete=models.CASCADE)

    

class Tags(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Productone , on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.CharField(max_length=155)
    subject = models.CharField(max_length=155)
    message = models.TextField()
    # date = models.DateField()
    def __str__(self):
        return self.name
    
class Signup(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=155)
    repeatpassword = models.CharField(max_length=155)

    def __str__(self):
        return self.username
    

class Checkout(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=155)
    lastname = models.CharField(max_length=155)
    country = models.CharField(max_length=155)
    address = models.CharField(max_length=155)
    city = models.CharField(max_length=155)
    state = models.CharField(max_length=155)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    payment_id = models.CharField(max_length=400 , null=True , blank=True)
    paid = models.BooleanField(default=False , null=True)
    amount = models.CharField(max_length=200)  
    date = models.DateField()

    def __str__(self):
        return self.user.username
    
class OrderItem(models.Model):
    oredr = models.ForeignKey(Checkout , on_delete=models.CASCADE)
    product = models.CharField(max_length=300)
    image = models.ImageField(upload_to='shop/images' , default="")
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=60)
    total = models.CharField(max_length=3000)
    razorpay_order_id = models.CharField(max_length=255, null=True, blank=True)  # Add this field



    def __str__(self):
        return self.oredr.user.username
    

class Commingsoon(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email 




class Shoptwocolum(models.Model):
    CONDITION = (('New', 'New'),('Old','Old'))
    STOCK = (('IN STOCK', 'IN STOCK'),('OUT OF STOCK' , 'OUT OF STOCK'))
    STATUS = (('Publish','Publish'),('Draft','Draft'))
    unique_id = models.CharField(unique=True , max_length=200 , null=True ,blank=True)
    image = models.ImageField(upload_to='shop/imagessss' , default="")
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION,max_length=200)
    information = models.TextField()
    description = models.TextField()
    stock = models.CharField(choices=STOCK,max_length=200)
    status = models.CharField(choices=STATUS,max_length=200)
    created_date = models.CharField(default=timezone.now  , max_length=200)
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE)
    
    # def save(self , *args , **kwargs):
    #     if self.unique_id is None and self.created_date and self.id:
    #         self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
    #     return super().save(*args , **kwargs)

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            if isinstance(self.created_date, str):
                self.created_date = datetime.strptime(self.created_date, "%Y-%m-%d %H:%M:%S")
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Imagessss(models.Model):
    image = models.ImageField(upload_to='shop/imagessss' , default="")
    shopcolum = models.ForeignKey(Shoptwocolum , on_delete=models.CASCADE)
    

class Tagsss(models.Model):
    name = models.CharField(max_length=200)
    shopcolum = models.ForeignKey(Shoptwocolum , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

