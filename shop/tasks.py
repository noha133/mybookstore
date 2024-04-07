# myapp/tasks.py
from __future__ import absolute_import
from celery import shared_task
from .models import Cart, Product


@shared_task
def add_numbers(x, y):
    return x + y


@shared_task
def my_hourly_task():

    carts = Product.objects.first()
    carts.delete()
