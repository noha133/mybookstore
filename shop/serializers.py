from rest_framework import serializers
from .models import Product, CartItem, Order


class ProductSerializer(serializers.ModelSerializer):
    total_quantity_ordered = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Product
        fields = ["id", "name", "category", "price", "total_quantity_ordered"]

    def get_total_quantity_ordered(self):
        return self.total_quantity_ordered


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
