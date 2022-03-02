
from django.db import models

# Create your models here.


class Store(models.Model):
    name=models.CharField(max_length=20)


class Item(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
    store=models.ForeignKey(Store,on_delete=models.CASCADE,related_name="items")
    stock=models.PositiveBigIntegerField()


class Order(models.Model):
    _status_choices = (
        ('1', 'Processing'),
        ('2', 'on Route'),
        ('3', 'Delivered'),
    )
    destination_long = models.DecimalField(max_digits=18, decimal_places=9)
    destination_lat = models.DecimalField(max_digits=18, decimal_places=9)
    driver=models.ForeignKey("user.StoreDriver", on_delete=models.CASCADE,null=True,blank=True)
    slug=models.SlugField(unique=True)
    status=models.CharField(max_length=25,choices=_status_choices)


class OrderItems(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE,related_name="order_items")
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    qty=models.PositiveBigIntegerField()







