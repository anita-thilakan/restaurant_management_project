from rest_framework import serializers
from account.models import Customer,MenuItem
from .models import Order,OrderStatus,Restaurant
from account.serializers import CustomerSerializer,MenuItemSerializer
class OrderSerializer(serializers.Serializer):
    customer = CustomerSerializer()

    items = serializers.ListField(
        child = serializers.CharField()
    )

    res = serializers.IntegerField()

    def create(self,validated_data):
        
        customer = validated_data.pop('customer')
        items = validated_data.pop('items')
        res = validated_data.pop('res')
        
        # status = OrderStatus.objects.get(name="pending")
        #LOWER case
        for item in items:
            item = item.lower()
    
        #create customer

        customer,created = Customer.objects.get_or_create(
            name = customer['name'],
            phone = customer['phone'],
            defaults= customer

        )

        restaurant = Restaurant.objects.get(pk=res)
        #cal total price
        total_price = 0
        menuitems = MenuItem.objects.filter(name__in=items, restaurant = restaurant )

        for item in menuitems:
            if item.is_available:
                print(item.price)
                total_price += item.price
                
        #create order for created customer

        order = Order.objects.create(customer = customer, total_price=total_price,res=restaurant)

        return order

