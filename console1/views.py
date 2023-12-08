from django.shortcuts import render


def all_orders(request):

    return render(request, 'console/all_orders.html')


def all_staff(request):

    return render(request, 'console/all_staff.html')


def chef_all_orders(request):

    return render(request, 'console/chef_all_orders.html')


def chef_order(request):

    return render(request, 'console/chef_order.html')


def completed_order_info(request):

    return render(request, 'console/completed_order_info.html')


def completed_orders(request):

    return render(request, 'console/completed_orders.html')


def employees(request):

    return render(request, 'console/employees.html')


def login(request):

    return render(request, 'console/login.html')


def manager(request):

    return render(request, 'console/manager.html')


def new_order(request):

    return render(request, 'console/new_order.html')


def order(request):

    return render(request, 'console/order.html')


def products(request):

    return render(request, 'console/products.html')


def staff(request):

    return render(request, 'console/staff.html')


def storage(request):

    return render(request, 'console/storage.html')
