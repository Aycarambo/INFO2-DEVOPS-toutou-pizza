from rest_framework import serializers

from online_orders.models import Order, Client
from restaurant.models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["nb", "street", "complement", "city", "zipcode"]


class RestaurantSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = ["name", "address"]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name", "allergen"]


class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Pizza
        fields = ["name", "price", "ingredients"]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    address = AddressSerializer()

    def create(self, validated_data):
        client_data = validated_data.get("client")
        client = Client.objects.create(**client_data)
        address_data = validated_data.get("address")
        address = Address.objects.create(**address_data)
        order = Order.objects.create(
            client=client,
            restaurant=validated_data.get("restaurant"),
            delivery_hour=validated_data.get("delivery_hour"),
            address=address
        )
        order.pizzas.set(validated_data.get("pizzas"))
        return order

    def update(self, instance, validated_data):
        client_data = validated_data.get("client")
        instance.client.name = client_data.get('name')
        instance.client.email = client_data.get('email')
        address_data = validated_data.get("address")
        instance.address.nb = address_data.get('nb')
        instance.address.street = address_data.get('street')
        instance.address.zipcode = address_data.get('zipcode')
        instance.address.city = address_data.get('city')
        instance.address.complement = address_data.get('complement')
        return instance

    class Meta:
        model = Order
        fields = "__all__"


class OrderSerializerDisplay(OrderSerializer):
    pizzas = PizzaSerializer(many=True)
