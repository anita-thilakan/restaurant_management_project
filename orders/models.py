from django.db import models

# Create your models here.
<<<<<<< HEAD

#OrderStatus

class OrderStatus(models.Model):
    name = models.CharField(max_length=100,unique= True)
=======
class OrderStatus(models.Model):
    name = models.CharField(max_length = 100, unique= True)
>>>>>>> bac5e779490cd9da5091f129f83c3043fd071cc9

    def __str__(self):
        return self.name

<<<<<<< HEAD
class Coupons(models.Model):
    code = models.CharField(max_length= 10,unique=True)
    discount = models.DecimalField(max_digits=4,decimal_places=2)
    status = models.CharField(max_length=50)

class Order(models.Model):
    status = models.ForeignKey(OrderStatus,on_delete=models.SET_NULL,null=True)
    coupon = models.ForeignKey(Coupons,on_delete=models.SET_NULL,null=True)

    
=======
class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete = models.SET_NULL, null=True)
>>>>>>> bac5e779490cd9da5091f129f83c3043fd071cc9
