from django.contrib import admin
from .models import Order,OrderStatus,Coupons
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Coupons)
