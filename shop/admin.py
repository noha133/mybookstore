from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order
from users.models import User

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    raw_id_fields = ["product"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "status"]
    inlines = [CartItemAdmin]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "status"]

