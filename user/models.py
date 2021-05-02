from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username ")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name, last_name):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):   # user model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True) # email has to be unique
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)   # date joined auto added
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)   # is active is always true
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)   # is superuser is always false unless overwritten

    USERNAME_FIELD = 'username' # main field required
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']  # other required fields

    objects = MyUserManager()   # call user manager

    class Meta:
        permissions = [
            ('can_view', 'can_view'),
            ('can_edit', 'can_edit')
        ]

    def __str__(self):
        return self.email

    def grant_permission(self):  # granting this user permissions
        if self.is_staff:
            self.has_perm('app.add_app'),
            self.has_perm('app.change_app'),
            self.has_perm('app.delete_app'),
            self.has_perm('app.view_app'),
        else:
            self.has_perm('app.view_app')

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Staff(models.Model):  # staff user model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)


def set_staff_status_receiver(sender, instance, *args, **kwargs):   # overwriting staff user to true
    if not instance.user.is_staff:
        instance.user.is_staff = True
        instance.user.save()


post_save.connect(set_staff_status_receiver, sender=Staff)


class NonStaff(models.Model):   # non-staff user model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)


def set_not_staff_status_receiver(sender, instance, *args, **kwargs):   # overwriting non-staff user to false
    if instance.user.is_staff:
        instance.user.is_staff = False
        instance.user.save()


post_save.connect(set_not_staff_status_receiver, sender=NonStaff)
