from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.decorators import api_view
from .models import Restaurant,MenuItem,Customer
from .serializers import RestaurantSerializer,StaffLoginSerilizer,MenuItemSerializer,CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,get_user_model
from rest_framework.views import APIView
from django.urls import reverse
# Create your views here.
@api_view(['GET'])
def restaurants(request,pk=None):
    if pk is not None:
        restaurant = get_object_or_404(Restaurant,pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif pk is None:
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants,many=True)
        
        return Response(serializer.data)

@api_view(['POST','PUT'])
def register(request,pk=None):
    if pk is not None:
        restaurant = get_object_or_404(Restaurant,pk=pk)
        serializer = RestaurantSerializer(restaurant,data=request.data,partial = True)

    
    elif pk is None:
         serializer = RestaurantSerializer(data=request.data)


   
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def delete_restaurant(request,pk):
    restaurant = get_object_or_404(Restaurant,pk=pk)
    restaurant.delete()
    print('deleted')

    return Response(status=status.HTTP_204_NO_CONTENT)


#staff login view

class StaffLoginAPIView(APIView):
    def post(self,request):
        serializer = StaffLoginSerilizer(data= request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            #user model
            User = get_user_model()
            #get the user object
            try:

                myuser = User.objects.get(email=email)
                res_id = myuser.res_id.id
                url = reverse('menuitems',kwargs={'pk':res_id})
                return redirect(url)
            except User.DoesNotExist:
                return Response({"error": "invalid user!"})

            # print('user ...',myuser)
            # user_valid = myuser.check_password(password)
            # print("Authenticated user:", user) 
            
            if myuser.check_password(password):
                return Response({"message":"login successful","staff id":myuser.id}, status=status.HTTP_200_OK)
            return Response({
                    "error": "Invalid credentials or not a staff user."
                }, status=status.HTTP_401_UNAUTHORIZED)

#MenuItem 

@api_view(['GET'])
def menuitems(request,pk):
    restaurant = Restaurant.objects.get(id=pk)
    menuitems = MenuItem.objects.filter(restaurant= restaurant)
    serializer = MenuItemSerializer(menuitems,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def create_menu_item(request,pk):
    serializer = MenuItemSerializer(data=request.data)
    restaurant = Restaurant.objects.get(pk=pk)
    if serializer.is_valid():
        serializer.save(restaurant= restaurant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

@api_view(['PUT'])
def update_menu_item(request,pk):
    menuitem = MenuItem.objects.get(pk=pk)
    serializer = MenuItemSerializer(menuitem,data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_menuitem(request,pk):
    menuitem = MenuItem.objects.get(pk=pk)
    menuitem.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

# get customers
@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers,many=True)
    return Response(serializer.data)

#create customer
@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

