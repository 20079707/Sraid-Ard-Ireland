from django.db import models


def upload_path(instance, filename):
    return '/'.join(['images/', str(instance.name), filename])


class Address(models.Model):
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50, blank=True, null=True)
    town_city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    eir_code = models.CharField(primary_key=True, max_length=50, blank=False)

    def __str__(self):
        return self.eir_code


class Shop(models.Model):
    shop_name = models.CharField(max_length=50, blank=False)
    slogan = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=500, blank=False)
    logo = models.ImageField(upload_to='logos', default='', blank=False)
    shop_image = models.ImageField(upload_to=upload_path, default='', blank=True)
    phone_no = models.IntegerField(default=0)
    email = models.EmailField(blank=False)
    business_reg = models.CharField(primary_key=True, max_length=10, default='', blank=False, unique=True)
    address = models.OneToOneField(Address, null=False, default='', blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.shop_name)


class Category(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, auto_created=True)
    name = models.CharField(max_length=100, blank=False)
    category_description = models.TextField(max_length=400, blank=False)
    category_image = models.ImageField(upload_to=upload_path, default='', blank=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    red = 'Red'
    blue = 'Blue'
    green = 'Green'
    orange = 'Orange'
    yellow = 'Yellow'
    white = 'White'
    black = 'Black'
    navy = 'Navy'
    brown = 'Brown'
    purple = 'Purple'
    pink = 'Pink'
    in_stock = 'In Stock'
    out_of_stock = 'Out Of Stock'

    STOCK = [
        (in_stock, 'In Stock'),
        (out_of_stock, 'Out Of Stock'),
    ]

    COLOUR_CHOICES = [
        (red, 'Red'),
        (blue, 'Blue'),
        (green, 'Green'),
        (orange, 'Orange'),
        (yellow, 'Yellow'),
        (white, 'White'),
        (black, 'Black'),
        (navy, 'Navy'),
        (brown, 'Brown'),
        (purple, 'Purple'),
        (pink, 'Pink'),
    ]

    product_code = models.IntegerField(primary_key=True, auto_created=True, blank=False, unique=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    product_image = models.ImageField(upload_to=upload_path, default='', blank=True)
    product_description = models.TextField(max_length=250, blank=True)
    quantity = models.IntegerField(default=0)
    colour = models.CharField(max_length=10, choices=COLOUR_CHOICES, default=black)
    stock = models.CharField(max_length=50, choices=STOCK, default=in_stock)
    shipping_fee = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    last_update = models.DateTimeField(auto_now=True, null=True)
    weight = models.DecimalField(default=0, max_digits=100, decimal_places=1)
    shop = models.ForeignKey(Shop, null=True, default='', blank=False, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, null=True, default='', blank=False, on_delete=models.PROTECT)
