from rest_framework.routers import DefaultRouter
from mynotes import views
from django.urls import path


router = DefaultRouter()
router.register(r'user',views.NoteViewset,basename='user')


urlpatterns = [
    path('',views.login,name='login'),
    # path('token/', obtain_auth_token, name='api_token_auth'),  # now /api/notes/ is token login
    ]

urlpatterns += router.urls


