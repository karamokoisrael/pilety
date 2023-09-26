from django.contrib import admin
from django.urls import path, include
# from users.api_views import *
# from allin.api_urls import api_routes
from users.api_views import (UserListAPIView, UserAddressListAPIView,
                             UserListCreateAPIView, UserAddressListCreateAPIView,
                             UserRetrieveUpdateDestroyAPIView,
                             UserAddressRetrieveUpdateDestroyAPIView,
                             
                             )
app_name = 'users'
urlpatterns = [
    # ListApi
    path('user/', UserListAPIView .as_view()),
    path('user/ad/', UserAddressListAPIView.as_view()),
    
    #ListCreateApi Views 
    path('list_create_User/', UserListCreateAPIView .as_view()),
    path('list_create_User/ad/', UserAddressListCreateAPIView.as_view()),
    
    #Update details views
    # path('_detail/<int:pk>/', .as_view() ),
    # path('_detail/<int:pk>/', .as_view() ),

    # Update retrieve destroy
    # path('_detail/<int:pk>/', .as_view() ),

    path('User_detail/<int:pk>/', UserRetrieveUpdateDestroyAPIView .as_view()),
    path('User_detail/ad/<int:pk>/', UserAddressRetrieveUpdateDestroyAPIView.as_view()),
    
]
# ] + api_routes
