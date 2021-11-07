from accounts.views import home, products, customer
from django.urls import path

urlpatterns = [
    path('', home),
    path('products/', products),
    path('customer', customer)
]