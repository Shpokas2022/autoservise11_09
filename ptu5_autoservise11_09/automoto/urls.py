from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('car/', views.cars, name='cars'),
    path('car/<int:pk>/', views.cars, name='car'),
    path('orders/', views.orders, name="order")
]
