from django.shortcuts import render
from console1.models import Employee, Order, Product, Pizza, Recipe

pizzas_names = [pizza.name for pizza in Pizza.objects.all()]
recipes = {f'{recipe.pizza.name}': {f'{recipe.product_1}': recipe.product_1_amount,
                                    f'{recipe.product_2}': recipe.product_2_amount,
                                    f'{recipe.product_3}': recipe.product_3_amount,
                                    f'{recipe.product_4}': recipe.product_4_amount,
                                    f'{recipe.product_5}': recipe.product_5_amount,
                                    f'{recipe.product_6}': recipe.product_6_amount,
                                    f'{recipe.product_7}': recipe.product_7_amount,
                                    f'{recipe.product_8}': recipe.product_8_amount,
                                    f'{recipe.product_9}': recipe.product_9_amount,
                                    f'{recipe.product_10}': recipe.product_10_amount,
                                    f'{recipe.product_11}': recipe.product_11_amount,
                                    f'{recipe.product_12}': recipe.product_12_amount,
                                    f'{recipe.product_13}': recipe.product_13_amount,
                                    f'{recipe.product_14}': recipe.product_14_amount,
                                    f'{recipe.product_15}': recipe.product_15_amount
                                    } for recipe in Recipe.objects.all()}


def manager(request):
    return render(request, 'console/manager.html')


def all_staff(request):
    workers = Employee.objects.all()

    return render(request, 'console/all_staff.html',
                  context={'workers': workers})


def staff(request, employee_id):
    employee = Employee.objects.get(worker_id=employee_id)

    return render(request, 'console/staff.html', {'employee': employee})


def all_orders(request):
    all_orders_list = Order.objects.all()
    orders = []
    for order_info in all_orders_list:
        if order_info.status in ["Ожидает", "Готовится", "Отменён", "Готов"]:
            orders.append(order_info)
    new_orders_count = Order.objects.filter(status='Принят').count()

    return render(request, 'console/all_orders.html',
                  context={'orders': orders, 'new_orders_count': new_orders_count})


def order(request, order_id):
    order_info = Order.objects.get(order_id=order_id)
    delivery_info = order_info.delivery_info
    customer = order_info.customer
    pizzas_amounts = {f'{pizzas_names[0]}': order_info.pizza_1_amount,
                      f'{pizzas_names[1]}': order_info.pizza_2_amount,
                      f'{pizzas_names[2]}': order_info.pizza_3_amount,
                      f'{pizzas_names[3]}': order_info.pizza_4_amount,
                      f'{pizzas_names[4]}': order_info.pizza_5_amount}

    return render(request, 'console/order.html',
                  context={'order': order_info, 'delivery_info': delivery_info, 'customer': customer,
                           'pizzas_amounts': pizzas_amounts, 'pizzas': pizzas_names, })


def new_order(request):
    new_orders = Order.objects.filter(status='Принят')
    if len(new_orders) > 0:
        new_order_info = new_orders[0]
        delivery_info = new_order_info.delivery_info
        customer = new_order_info.customer

        pizzas_amounts = {f'{pizzas_names[0]}': new_order_info.pizza_1_amount,
                          f'{pizzas_names[1]}': new_order_info.pizza_2_amount,
                          f'{pizzas_names[2]}': new_order_info.pizza_3_amount,
                          f'{pizzas_names[3]}': new_order_info.pizza_4_amount,
                          f'{pizzas_names[4]}': new_order_info.pizza_5_amount}

        return render(request, 'console/new_order.html',
                      context={'new_order': new_order_info, 'customer': customer, 'delivery_info': delivery_info,
                               'pizzas_amounts': pizzas_amounts, 'pizzas': pizzas_names})

    else:
        return render(request, 'console/new_order.html', context={'new_order': None})


def send_to_kitchen(request, order_id):
    order_to_send = Order.objects.get(order_id=order_id)
    order_to_send.status = 'Ожидает'
    order_to_send.save()
    request.GET = '/new_order/'

    return new_order(request)


def completed_orders(request):
    orders = Order.objects.filter(status='Завершён')
    delivery_infos = [order_info.delivery_info for order_info in orders]

    return render(request, 'console/completed_orders.html',
                  context={'orders': orders, 'delivery_infos': delivery_infos})


def completed_order_info(request, order_id):
    order_info = Order.objects.get(order_id=order_id)
    chef = Employee.objects.get(worker_id=order_info.chef.worker_id)

    return render(request, 'console/completed_order_info.html', context={'order': order_info, 'chef': chef})


def products(request):
    all_products = Product.objects.all()

    return render(request, 'console/products.html', {'products': all_products})


def chef_all_orders(request):
    all_orders_list = Order.objects.all()
    orders = []
    for order_info in all_orders_list:
        if order_info.status in ["Ожидает", "Готовится"]:
            orders.append(order_info)

    return render(request, 'console/chef_all_orders.html',
                  context={'orders': orders})


def chef_order(request, order_id):
    order_info = Order.objects.get(order_id=order_id)

    pizzas_amounts = {f'{pizzas_names[0]}': order_info.pizza_1_amount,
                      f'{pizzas_names[1]}': order_info.pizza_2_amount,
                      f'{pizzas_names[2]}': order_info.pizza_3_amount,
                      f'{pizzas_names[3]}': order_info.pizza_4_amount,
                      f'{pizzas_names[4]}': order_info.pizza_5_amount}

    return render(request, 'console/chef_order.html',
                  context={'order': order_info, 'pizzas_amounts': pizzas_amounts, 'pizzas': pizzas_names,
                           'recipes': recipes})


def calculate_used_products(order_id):
    order_info = Order.objects.get(order_id=order_id)
    cooked_pizzas_amounts = {f'{pizzas_names[0]}': order_info.pizza_1_amount,
                             f'{pizzas_names[1]}': order_info.pizza_2_amount,
                             f'{pizzas_names[2]}': order_info.pizza_3_amount,
                             f'{pizzas_names[3]}': order_info.pizza_4_amount,
                             f'{pizzas_names[4]}': order_info.pizza_5_amount}

    cooked_pizzas = [pizza_name for pizza_name in cooked_pizzas_amounts if cooked_pizzas_amounts[pizza_name] > 0]
    used_products = {}

    for pizza_name in cooked_pizzas:
        recipe = recipes[pizza_name]
        del recipe['None']
        for product_name in recipe.keys():
            used_products[product_name] = recipe[product_name] / 1000

    for product_name in used_products.keys():
        product = Product.objects.get(name=product_name)
        product.amount -= used_products[product_name]
        product.save()


def set_ready(request, order_id):
    calculate_used_products(order_id)

    order_to_set_ready = Order.objects.get(order_id=order_id)
    order_to_set_ready.status = 'Готов'
    order_to_set_ready.save()

    request.GET = '/chef_all_orders/'

    return chef_all_orders(request)


def cancel(request, order_id):
    order_to_cancel = Order.objects.get(order_id=order_id)
    order_to_cancel.status = 'Отменён'
    order_to_cancel.save()
    request.GET = '/chef_all_orders/'

    return chef_all_orders(request)


def take_order(request, order_id):
    order_to_take = Order.objects.get(order_id=order_id)
    order_to_take.status = 'Готовится'
    order_to_take.save()
    request.GET = '/chef_all_orders/'

    return chef_all_orders(request)


def courier_all_orders(request):
    orders = Order.objects.filter(status='Готов')

    return render(request, 'console/courier_all_orders.html',
                  context={'orders': orders})


def courier_order(request, order_id):
    order_info = Order.objects.get(order_id=order_id)
    pizzas_amounts = {f'{pizzas_names[0]}': order_info.pizza_1_amount,
                      f'{pizzas_names[1]}': order_info.pizza_2_amount,
                      f'{pizzas_names[2]}': order_info.pizza_3_amount,
                      f'{pizzas_names[3]}': order_info.pizza_4_amount,
                      f'{pizzas_names[4]}': order_info.pizza_5_amount}

    return render(request, 'console/courier_order.html',
                  context={'order': order_info, 'pizzas_amounts': pizzas_amounts, 'pizzas': pizzas_names})


def login(request):
    return render(request, 'console/login.html')