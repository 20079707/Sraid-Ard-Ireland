# Generated by Django 3.1.7 on 2021-03-30 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210310_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='AddressLine1',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='AddressLine2',
            new_name='address_line2',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='County',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='EirCode',
            new_name='eir_code',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='TownCity',
            new_name='town_city',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='EntryDate',
            new_name='entry_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='LastUpdate',
            new_name='last_update',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ProductCode',
            new_name='product_code',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ProductDescription',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Shop',
            new_name='shop',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Weight',
            new_name='weight',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='BusinessReg',
            new_name='business_reg',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='Logo',
            new_name='logo',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='PhoneNo',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='ShopName',
            new_name='shop_name',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='Slogan',
            new_name='slogan',
        ),
    ]
