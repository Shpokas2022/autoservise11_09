from django.shortcuts import render
from django.http import HttpResponse
from . models import Car, Service, OrderLine

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