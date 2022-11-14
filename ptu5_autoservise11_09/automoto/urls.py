from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('car/', views.cars, name='cars'),
    path('car/<int:car_id>/', views.car_info, name='car'),
    path('orders/', views.orders, name="orders"),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name="order"),
]
