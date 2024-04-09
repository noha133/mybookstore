# myapp/tasks.py
from __future__ import absolute_import
from celery import shared_task
from .models import Cart, Order
from django.conf import settings
from django.core.mail import send_mail

# from fcm_django.models import FCMDevice


@shared_task
def add_numbers(x, y):
    return x + y


@shared_task
def my_hourly_task():
    pass


# device = FCMDevice.objects.all().first()
# if device:
#     device.send_message(
#         title="Notification Title", body="Notification Body", data={"key": "value"}
#     )
# carts = Cart.objects.all
# for cart in cart:
#     user = cart.user.id
#     device = FCMDevice.objects.get(user=user)  # Get the device for a specific user
#     device.send_message(title="Notification Title", body="Notification Body", data={"key": "value"})


@shared_task
def order_created(order_id):
    order = Order.objects.filter(id=order_id).first()
    invoice = (
        f"You successfully place an order " f"Total amount = {order.get_total_cost}"
    )
    order.invoice = invoice
    order.save()
