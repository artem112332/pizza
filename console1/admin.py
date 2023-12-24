from django.contrib import admin

from console1.models import Worker, Order, Pizza, Product, Recipe, Customer, DeliveryInfo

admin.site.register(Worker)
admin.site.register(Order)
admin.site.register(Pizza)
admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(Customer)
admin.site.register(DeliveryInfo)