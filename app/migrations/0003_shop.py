# Generated by Django 3.1.7 on 2021-03-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShopName', models.CharField(max_length=50)),
                ('Slogan', models.CharField(blank=True, max_length=150, null=True)),
                ('Description', models.TextField(max_length=500)),
                ('Logo', models.ImageField(null=True, upload_to='Logos/')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('PhoneNo', models.IntegerField(default=0)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
