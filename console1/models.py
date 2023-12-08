from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)


class DeliveryInfo(models.Model):
    order = models.OneToOneField('Orders', to_field='order_id', on_delete=models.DO_NOTHING, primary_key=True, blank=True, null=False)
    adress = models.CharField(max_length=100, blank=True, null=True)
    delivery_type = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=300, blank=True, null=True)


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True, blank=True, null=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, to_field='customer_id', blank=True, null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    pizza_1_amount = models.SmallIntegerField(blank=True, null=True)
    pizza_2_amount = models.SmallIntegerField(blank=True, null=True)
    pizza_3_amount = models.SmallIntegerField(blank=True, null=True)
    pizza_4_amount = models.SmallIntegerField(blank=True, null=True)
    pizza_5_amount = models.SmallIntegerField(blank=True, null=True)


class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.SmallIntegerField(blank=True, null=True)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(max_length=20, blank=True, null=True)
    amount = models.SmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.SmallIntegerField(blank=True, null=True)


class Recipe(models.Model):
    pizza = models.OneToOneField(Pizza, models.DO_NOTHING, primary_key=True, blank=True, null=False)
    product_1 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_1_set', blank=True, null=True)
    product_2 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_2_set', blank=True, null=True)
    product_3 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_3_set', blank=True, null=True)
    product_4 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_4_set', blank=True, null=True)
    product_5 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_5_set', blank=True, null=True)


class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True, blank=True, null=False)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    post = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    login = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
