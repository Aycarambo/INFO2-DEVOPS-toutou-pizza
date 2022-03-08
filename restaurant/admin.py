from django.contrib import admin
from django.contrib.admin import ModelAdmin

from restaurant.models import Restaurant, Ingredient, Pizza, Address


@admin.register(Restaurant)
class RestaurantAdmin(ModelAdmin):
    list_display = ['name', 'address']


@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = ['nb', 'street', 'zipcode', 'city', 'complement']


@admin.register(Pizza)
class PizzaAdmin(ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ['name', 'allergen']
