from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    worker_id = models.AutoField(primary_key=True, blank=True, null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    post = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    first_work_day = models.DateField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.full_name, self.post)

    @property
    def full_name(self):
        return '{} {} {}'.format(self.user.last_name, self.user.first_name, self.middle_name)

    @property
    def name(self):
        return '{} {}.{}'.format(self.user.last_name, self.user.first_name[0], self.middle_name[0])


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)  # имя
    last_name = models.CharField(max_length=30, blank=True, null=True)  # фамилия
    middle_name = models.CharField(max_length=30, blank=True, null=True)  # отчество
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return 'ID: {}, {} {}'.format(self.customer_id, self.last_name, self.first_name)

    @property
    def name(self):
        return '{} {}.{}'.format(self.last_name, self.first_name[0], self.middle_name[0])


class DeliveryInfo(models.Model):
    delivery_info_id = models.AutoField(primary_key=True, blank=True, null=False)
    adress = models.CharField(max_length=100, blank=True, null=True)
    delivery_type = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=300, blank=True, null=True)
    courier = models.ForeignKey(Employee, to_field='worker_id', related_name='Worker.courier+',
                                on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.adress}'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, blank=True, null=False)
    delivery_info = models.ForeignKey(DeliveryInfo, on_delete=models.SET_NULL, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True,
                                 null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    pizza_1_amount = models.SmallIntegerField(blank=False, null=True, default=0)
    pizza_2_amount = models.SmallIntegerField(blank=False, null=True, default=0)
    pizza_3_amount = models.SmallIntegerField(blank=False, null=True, default=0)
    pizza_4_amount = models.SmallIntegerField(blank=False, null=True, default=0)
    pizza_5_amount = models.SmallIntegerField(blank=False, null=True, default=0)
    order_date = models.DateField(blank=True, null=True)
    StatusChoices = [
        ('Принят', 'Принят'),
        ('Ожидает', 'Ожидает'),
        ('Готовится', 'Готовится'),
        ('Отменён', 'Отменён'),
        ('Готов', 'Готов'),
        ('Доставляется', 'Доставляется'),
        ('Завершён', 'Завершён')
    ]
    status = models.CharField(max_length=15, blank=True, choices=StatusChoices, null=True)

    # Статусы:
    # "Принят" (первичный статус для заказов в консоли)
    # "Ожидает" (после отправки на кухню менеджером)
    # "Готовится" (после нажатия кнопки поваром)
    # "Отменён" (после нажатия кнопки поваром)
    # "Готов" (и ожидает курьера)
    # "Доставляется" (после получения заказа курьером)
    # "Завершён" (доставлен)
    # Статуса "Оплачен" нет, потому что заказ в теории может быть оплачен как онлайн, так и наличными при получении
    chef = models.ForeignKey(Employee, to_field='worker_id', related_name='Worker.chef+', on_delete=models.SET_NULL,
                             blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Заказ №{} {} - {}'.format(self.order_id, self.order_date, self.status)


class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'ID: {self.pizza_id} {self.name}'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(max_length=20, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.SmallIntegerField(blank=True, null=True)
    critical_amount = models.FloatField(blank=True, null=True)

    # def __str__(self):
    #     if self.amount < 1:
    #         return '{} - {} г'.format(self.name, int(self.amount * 1000))
    #     return '{} - {} кг'.format(self.name, self.amount)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    pizza = models.ForeignKey(Pizza, models.DO_NOTHING, primary_key=True, blank=True, null=False)
    product_1 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_1_set',
                                  blank=True, null=True)
    product_1_amount = models.SmallIntegerField(blank=True, null=True)
    product_2 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_2_set',
                                  blank=True, null=True)
    product_2_amount = models.SmallIntegerField(blank=True, null=True)
    product_3 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_3_set',
                                  blank=True, null=True)
    product_3_amount = models.SmallIntegerField(blank=True, null=True)
    product_4 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_4_set',
                                  blank=True, null=True)
    product_4_amount = models.SmallIntegerField(blank=True, null=True)
    product_5 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_5_set',
                                  blank=True, null=True)
    product_5_amount = models.SmallIntegerField(blank=True, null=True)
    product_6 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_6_set',
                                  blank=True, null=True)
    product_6_amount = models.SmallIntegerField(blank=True, null=True)
    product_7 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_7_set',
                                  blank=True, null=True)
    product_7_amount = models.SmallIntegerField(blank=True, null=True)
    product_8 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_8_set',
                                  blank=True, null=True)
    product_8_amount = models.SmallIntegerField(blank=True, null=True)
    product_9 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_9_set',
                                  blank=True, null=True)
    product_9_amount = models.SmallIntegerField(blank=True, null=True)
    product_10 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_10_set',
                                   blank=True, null=True)
    product_10_amount = models.SmallIntegerField(blank=True, null=True)
    product_11 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_11_set',
                                   blank=True, null=True)
    product_11_amount = models.SmallIntegerField(blank=True, null=True)
    product_12 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_12_set',
                                   blank=True, null=True)
    product_12_amount = models.SmallIntegerField(blank=True, null=True)
    product_13 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_13_set',
                                   blank=True, null=True)
    product_13_amount = models.SmallIntegerField(blank=True, null=True)
    product_14 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_14_set',
                                   blank=True, null=True)
    product_14_amount = models.SmallIntegerField(blank=True, null=True)
    product_15 = models.ForeignKey(Product, models.DO_NOTHING, to_field='product_id', related_name='product_15_set',
                                   blank=True, null=True)
    product_15_amount = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'Рецепт "{Pizza.objects.get(pizza_id=self.pizza_id).name}"'
