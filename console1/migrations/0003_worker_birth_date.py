# Generated by Django 4.2.7 on 2023-12-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console1', '0002_orders_order_date_worker_first_work_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]