from rest_framework import serializers
from account.models import Customer,MenuItem
from .models import Order,OrderStatus
from account.serializers import CustomerSerializer,MenuItemSerializer
class OrderSerializer(serializers.Serializer):
    customer = CustomerSerializer()

    items = serializers.ListField(
        child = serializers.CharField()
    )

    def create(self,validated_data):
        
        customer = validated_data.pop('customer')
        items = validated_data.pop('items')
        
        status = OrderStatus.objects.get(name="pending")
        #LOWER case
        for item in items:
            item = item.lower()
    
        #create customer

        customer,created = Customer.objects.get_or_create(
            name = customer['name'],
            phone = customer['phone'],
            defaults= customer

        )

        
        #cal total price
        total_price = 0
        menuitems = MenuItem.objects.filter(name__in=items)

        for item in menuitems:
            if item.is_available:
                total_price += item.price
                
        #create order for created customer

        order = Order.objects.create(customer = customer, total_price=total_price,res_id=validated_data['res_id'],status=status )

        return order

