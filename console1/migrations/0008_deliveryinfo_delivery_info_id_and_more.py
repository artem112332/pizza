# Generated by Django 4.2.7 on 2023-12-18 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console1', '0007_alter_deliveryinfo_courier_alter_deliveryinfo_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryinfo',
            name='delivery_info_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='console1.order'),
        ),
    ]