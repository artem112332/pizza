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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from console1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('manager/', manager),
    path('all_staff/', all_staff),
    path('all_staff/<int:employee_id>', staff),
    path('all_orders/', all_orders),
    path('new_order/', new_order),
    path('new_order/send_to_kitchen/<int:order_id>', send_to_kitchen),
    path('all_orders/<int:order_id>', order),
    path('products/', products),
    path('completed_orders/', completed_orders),
    path('completed_orders/<int:order_id>', completed_order_info),
    path('completed_order_info/', completed_order_info),
    path('chef_all_orders/', chef_all_orders),
    path('chef_all_orders/<int:order_id>', chef_order),
    path('chef_all_orders/set_ready/<int:order_id>', set_ready),
    path('chef_all_orders/cancel/<int:order_id>', cancel),
    path('chef_all_orders/take_order/<int:order_id>', take_order),
    path('courier_all_orders', courier_all_orders),
    path('courier_all_orders/<int:order_id>', courier_order),
    path('courier_all_orders/pickup_order/<int:order_id>', pickup_order),
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
