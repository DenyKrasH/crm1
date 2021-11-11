from accounts.views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<int:pk>', customer, name='customer'),
    path('create_order/<int:pk>', createOrder, name='create_order'),
    path('update_order/<int:pk>', updateOrder, name='update_order'),
    path('delete_order/<int:pk>', deleteOrder, name='delete_order'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('user/', userPage, name='user-page'),
    path('account/', accountSettings, name='account'),
]