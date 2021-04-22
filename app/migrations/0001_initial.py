# Generated by Django 3.1.7 on 2021-04-21 12:24

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_line1', models.CharField(max_length=50)),
                ('address_line2', models.CharField(blank=True, max_length=50, null=True)),
                ('town_city', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('eir_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category_description', models.TextField(max_length=400)),
                ('category_image', models.ImageField(blank=True, default='', upload_to=app.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_name', models.CharField(max_length=50)),
                ('slogan', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(max_length=500)),
                ('logo', models.ImageField(default='', upload_to='logos')),
                ('shop_image', models.ImageField(blank=True, default='', upload_to=app.models.upload_path)),
                ('phone_no', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('business_reg', models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('address', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='app.address')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_code', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('product_image', models.ImageField(blank=True, default='', upload_to=app.models.upload_path)),
                ('product_description', models.TextField(blank=True, max_length=250)),
                ('quantity', models.IntegerField(default=0)),
                ('colour', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('White', 'White'), ('Black', 'Black'), ('Navy', 'Navy'), ('Brown', 'Brown'), ('Purple', 'Purple'), ('Pink', 'Pink')], default='Black', max_length=10)),
                ('stock', models.CharField(choices=[('In Stock', 'In Stock'), ('Out Of Stock', 'Out Of Stock')], default='In Stock', max_length=50)),
                ('shipping_fee', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('entry_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('weight', models.DecimalField(decimal_places=1, default=0, max_digits=100)),
                ('category', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='app.category')),
                ('shop', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='app.shop')),
            ],
        ),
    ]
