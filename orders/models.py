from django.db import models

# Create your models here.

#OrderStatus

class OrderStatus(models.Model):
    name = models.CharField(max_length=100,unique= True)

    def __str__(self):
        return self.name

class Coupons(models.Model):
    code = models.CharField(max_length= 10,unique=True)
    discount = models.DecimalField(max_digits=4,decimal_places=2)
    status = models.CharField(max_length=50)

class Order(models.Model):
    status = models.ForeignKey(OrderStatus,on_delete=models.SET_NULL,null=True)
    coupon = models.ForeignKey(Coupons,on_delete=models.SET_NULL,null=True)

    