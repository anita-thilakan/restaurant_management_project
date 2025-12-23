from rest_framework import serializers
from .models import Restaurant,MenuItem,Customer
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


#staff 

class StaffLoginSerilizer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only= True)

#MenuItem

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['']


#Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','phone']