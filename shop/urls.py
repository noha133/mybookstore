from django.urls import path
from .views import ProductList, ProductDetail, CartItemList, OrderList


urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("cart/items/", CartItemList.as_view(), name="cart_list"),
    path("orders/", OrderList.as_view(), name="order_list"),
]
