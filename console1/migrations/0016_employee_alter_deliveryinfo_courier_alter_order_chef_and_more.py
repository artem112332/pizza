# Generated by Django 4.2.7 on 2023-12-24 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('console1', '0015_alter_recipe_product_10_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('worker_id', models.AutoField(primary_key=True, serialize=False)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('post', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('first_work_day', models.DateField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Worker.courier+', to='console1.employee'),
        ),
        migrations.AlterField(
            model_name='order',
            name='chef',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Worker.chef+', to='console1.employee'),
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]