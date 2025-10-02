from rest_framework import serializers
from .models import Restaurant,MenuItem
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


#staff 

class StaffLoginSerilizer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only= True)

#MenuItem

class MenuIemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'