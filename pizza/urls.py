"""
URL configuration for pizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from console1.views import all_orders, all_staff, chef_all_orders, chef_order, \
    completed_order_info, completed_orders, employees, login, manager, new_order, \
    order, products, staff, storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('all_orders/', all_orders),
    path('all_orders/login.html', login),
    path('all_staff/', all_staff),
    path('all_staff/login.html', login),
    path('chef_all_orders', chef_all_orders),
    path('chef_all_orders/login.html', login),
    path('chef_order/', chef_order),
    path('completed_order_info/', completed_order_info),
    path('completed_orders/', completed_orders),
    path('employees/', employees),
    path('login.html/', login),
    path('manager/', manager),
    path('manager/products.html', products),
    path('manager/all_orders.html', all_orders),
    path('manager/all_staff.html', all_staff),
    path('manager/completed_orders.html', completed_orders),
    path('manager/new_order.html', new_order),
    path('new_order/', new_order),
    path('order/', order),
    path('products/', products),
    path('staff/', staff),
    path('storage/', storage),
]
