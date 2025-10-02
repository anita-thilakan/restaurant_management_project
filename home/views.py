from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer
<<<<<<< HEAD
# Create your views here.
=======

# Create your views here.

>>>>>>> bac5e779490cd9da5091f129f83c3043fd071cc9
class MenuCategoryListAPI(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

