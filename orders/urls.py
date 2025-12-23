from django.urls import path
from .views import *

urlpatterns = [
    path('restaurant/<int:pk>/createorder',create_order,name="createorder")
]