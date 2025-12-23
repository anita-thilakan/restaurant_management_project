from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100,unique=True)
    owner_name = models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=200,unique=True)
    phone = models.CharField(max_length=13,unique=True)
    address = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

#menu item 
class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.name)



#custom manager that gives tools like create_user and create_Superuser 
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Enail must be set")
        email = self.normalize_email(email)
        # this creates user instance based on custo user model
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("res_id",None)

        
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    

    def __str__(self):
        return self.email

#customer(dine-in/ guests)
class Customer(models.Model):
    name = models.CharField(max_length=100,null=True,default="Anonymous")
    phone = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Guest Customer"





    