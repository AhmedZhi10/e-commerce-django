from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from product.models import Product

# Get cart
@extend_schema(responses=CartSerializer)
class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        user = self.request.user if self.request.user.is_authenticated else None
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key

        cart, _ = Cart.objects.get_or_create(
            user=user if user else None,
            session_key=None if user else session_key
        )
        return cart

# Add item
@extend_schema(request=CartItemSerializer, responses=CartSerializer)
class CartAddItemView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        user = request.user if request.user.is_authenticated else None
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key

        cart, _ = Cart.objects.get_or_create(
            user=user if user else None,
            session_key=None if user else session_key
        )

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={"quantity": quantity}
        )
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Update quantity
@extend_schema(request=CartItemSerializer, responses=CartSerializer)
class CartUpdateItemView(generics.UpdateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        cart_item_id = self.kwargs.get("pk")
        quantity = request.data.get("quantity")

        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

        cart_item.quantity = int(quantity)
        cart_item.save()
        serializer = CartSerializer(cart_item.cart)
        return Response(serializer.data)

# Remove item
@extend_schema(responses=CartSerializer)
class CartRemoveItemView(generics.DestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        cart_item_id = self.kwargs.get("pk")
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

        cart = cart_item.cart
        cart_item.delete()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

# Clear cart
@extend_schema(responses=CartSerializer)
class CartClearView(generics.DestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key

        cart, _ = Cart.objects.get_or_create(
            user=user if user else None,
            session_key=None if user else session_key
        )

        cart.items.all().delete()
        serializer = CartSerializer(cart)
        return Response(serializer.data)