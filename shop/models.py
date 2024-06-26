from django.db import models
from users.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def total_quantity_ordered(self):
        return (
            self.order_items.aggregate(
                total_quantity_ordered=models.Sum("quantity")
            ).get("total_quantity_ordered")
            or 0
        )

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"]), models.Index(fields=["-created"])]

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, related_name="carts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id}"

    @property
    def get_total_cost(self):
        return sum(item.get_cost for item in self.items.all())


class ItemBaseModel(models.Model):
    # cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def get_cost(self):
        return self.product.price * self.quantity


class CartItem(ItemBaseModel):
    cart = models.ForeignKey(Cart, related_name="cart_items", on_delete=models.CASCADE)


class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "pending"),
        ("PAID", "Paid"),
    ]
    user = models.ForeignKey(User, related_name="user_order", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    invoice = models.TextField(null=True)

    @property
    def get_total_cost(self):
        return sum(item.get_cost for item in self.order_items.all())


class OrderItem(ItemBaseModel):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )
