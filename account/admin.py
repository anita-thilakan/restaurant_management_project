from django.contrib import admin
from .models import Restaurant,CustomUser,MenuItem,Customer
# Register your models here.
admin.site.register(Restaurant)
# adm
admin.site.register(CustomUser)
admin.site.register(MenuItem)
admin.site.register(Customer)