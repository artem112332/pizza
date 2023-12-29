# Generated by Django 4.2.7 on 2023-12-14 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console1', '0005_order_chef_order_comments_order_courier_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='courier',
        ),
        migrations.AddField(
            model_name='customer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='deliveryinfo',
            name='courier',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Worker.courier+', to='console1.worker'),
        ),
    ]