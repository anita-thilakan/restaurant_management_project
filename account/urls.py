from django.urls import path
from .views import *

urlpatterns = [
    path('',restaurants,name='restaurants' ),
    path('register',register,name="register"),
    path('restaurant/<int:pk>',restaurants,name='restaurant' ),
    path('update/<int:pk>',register,name="update"),
    path('delete/<int:pk>',delete_restaurant,name='delete'),
    path('staff',StaffLoginAPIView.as_view(),name='stafflogin'),
    # id of the restaurant
    path('restaurant/<int:pk>/menuitems',menuitems,name='menuitems'),
    path('restaurant/<int:pk>/createmenu',create_menu_item,name='createmenuitem'),
    path('menuitem/update/<int:pk>',update_menu_item,name="updatemenu"),
    path('menuitem/delete/<int:pk>',delete_menuitem,name="deletemenu"),
    #customer fetch
    path('customers',get_customers,name="getcustomers"),
    path('customer/create',create_customer,name="createcustomer")


]