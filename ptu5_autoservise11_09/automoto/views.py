from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from . models import Car, Service, OrderLine, CarModel, Order

# Create your views here.
def index(request):
    car_model_count = Car.objects.count()
    order_line_count = OrderLine.objects.count()
    service_count = Service.objects.count()
    context = {
        'car_model_count': car_model_count,
        'order_line_count': order_line_count,
        'service_count': service_count,
    }

    return render(request,'automoto/index.html', context)

def cars(request):
    return render(request, 'automoto/cars.html', {'cars': Car.objects.all()})

def car_info(request, car_id):
    return render(request, 'automoto/car_info.html', {'car': get_object_or_404(Car,id=car_id)})

def orders(request):
    return render(request, 'automoto/orders.html', {'orders':Order.objects.all()})

class OrderDetailView(DetailView):
    model = Order
    template_name = 'automoto/order_detail.html'
