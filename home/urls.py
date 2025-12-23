from django.urls import path
from .views import *

urlpatterns = [
    path('',MenuCategoryListAPI.as_view(),name='MenuCategoryList')
]