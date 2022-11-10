from django.contrib import admin
from . import models


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('service', 'quantity', 'price', 'total', 'order')
    ordering = ('order', 'id')
    list_filter = ('order', )

class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'date')

class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model', 'plate', 'vin')
    list_filter = ('client', 'car_model')
    ordering = ('client', )
    search_fields = ('plate', 'vin')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(models.Car, CarAdmin)
admin.site.register(models.CarModel)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderLine, OrderLineAdmin)