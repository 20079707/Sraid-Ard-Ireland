# Generated by Django 3.1.7 on 2021-04-17 22:23

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_remove_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category_description', models.CharField(max_length=400)),
                ('category_image', models.ImageField(blank=True, default='', upload_to=app.models.upload_path)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='app.category'),
        ),
    ]
