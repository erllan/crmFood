from django.utils import timezone
from .managers import CustomUserManager
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    login = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name', 'email', 'surname']
    objects = CustomUserManager()

    def __str__(self):
        return self.login

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(100000000000000000000000)
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class OrderMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True, blank=True)
    count = models.IntegerField(default=0)

    def name(self):
        return self.meal.name

    def total(self):
        total = self.count * self.meal.price
        return total

    def price(self):
        price = self.meal.price
        return price


class Order(models.Model):
    tableid = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    ordermeal = models.ManyToManyField(OrderMeal)
    waiterid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def table_name(self):
        name = self.tableid.name
        return name


class Check(models.Model):
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def meals(self):
        meals = self.orderid.ordermeal.all()
        return meals

    def total(self):
        test = self.meals()
        total = 0
        for a in test:
            total += a.total()
        return total
