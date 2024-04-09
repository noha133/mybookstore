from .models import Product, Order, Cart, CartItem, OrderItem, User
from .serializers import (
    ProductSerializer,
    CartItemSerializer,
    OrderSerializer,
    CategorySerializer,
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .tasks import order_created

# Create your views here.


class CategoryList(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):
    """
    List all products, or create new product.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CartItemList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        product_id = request.data.get("product")

        cart, _ = Cart.objects.get_or_create(user=user)
        product = get_object_or_404(Product, id=product_id)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        serializer = CartItemSerializer(cart_item)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        orders = Order.objects.filter(user=user)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        request.data["user"] = user.id

        cart = get_object_or_404(Cart, user=user.id)
        cart_items = cart.cart_items.all()

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            for item in cart_items:
                OrderItem.objects.create(
                    order=order, product=item.product, quantity=item.quantity
                )
            cart.delete()
            order_created.delay(order.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
