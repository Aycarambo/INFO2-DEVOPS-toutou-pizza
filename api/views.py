from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response

from api.serializers import RestaurantSerializer, PizzaSerializer, OrderSerializer, OrderSerializerDisplay
from online_orders.models import Order
from restaurant.models import *


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.all()

    def list(self, request, *args, **kwargs):
        zipcode = self.request.query_params.get("zipcode", None)
        queryset = self.get_queryset()
        if zipcode is not None:
            queryset = queryset.filter(address__zipcode=zipcode)
        return Response(self.serializer_class(queryset, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, name=kwargs.get("name"))
        return Response(self.serializer_class(restaurant).data)


class PizzaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        return Pizza.objects.all()

    def list(self, request, *args, **kwargs):
        price = self.request.query_params.get("price", None)
        queryset = self.get_queryset()
        if price is not None:
            queryset = queryset.filter(price__lt=price)
        return Response(self.serializer_class(queryset, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        pizza = get_object_or_404(Pizza, name=kwargs.get("name"))
        return Response(self.serializer_class(pizza).data)


class OrderViewSet(generics.UpdateAPIView, viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def retrieve(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs.get("pk"))
        return Response(OrderSerializerDisplay(order).data)
