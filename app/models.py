from django.db import models


class Address(models.Model):
    AddressLine1 = models.CharField(max_length=50)
    AddressLine2 = models.CharField(max_length=50, blank=True, null=True)
    TownCity = models.CharField(max_length=50)
    County = models.CharField(max_length=50)
    EirCode = models.CharField(primary_key=True, max_length=50, blank=False)

    def __str__(self):
        return self.EirCode


class Shop(models.Model):
    ShopName = models.CharField(max_length=50, blank=False)
    Slogan = models.CharField(max_length=150, blank=True, null=True)
    Description = models.TextField(max_length=500, blank=False)
    Logo = models.ImageField(upload_to='Logos/', null=True, blank=False)
    Image = models.ImageField(upload_to='Images/', null=True, blank=True)
    PhoneNo = models.IntegerField(default=0)
    Email = models.EmailField(blank=False)


class Product(models.Model):
    ProductCode = models.IntegerField(primary_key=True, auto_created=True, blank=False, unique=True)
    Name = models.CharField(max_length=50, blank=False)
    Price = models.DecimalField(default=0, max_digits=10000, decimal_places=2)
    Category = models.CharField(default='Select Category', max_length=50, blank=False)
    Image = models.ImageField(upload_to='Images/', null=True, blank=True)
    ProductDescription = models.TextField(max_length=250, blank=True)
    Quantity = models.IntegerField(default=0)
    EntryDate = models.DateTimeField(auto_now_add=True, null=True)
    LastUpdate = models.DateTimeField(auto_now=True, null=True)
    Weight = models.DecimalField(default=0, max_digits=100, decimal_places=1)

    def __str__(self):
        return self.Name
