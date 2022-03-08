from django.test import TestCase
from restaurant.models import Pizza, Ingredient


class PizzaTestCase(TestCase):
    def setUp(self) -> None:
        Ingredient.objects.create(name = "Farine de ble", allergen = True)
        Ingredient.objects.create(name = "Parmesan", allergen = False)
        test = Ingredient.objects.get("Farine de ble")
        Pizza.objects.create(name = "Reine", price = 9, ingredient = [])

    def testPrixPizza(self):
        reine = Pizza.objects.get("Reine")
        self.assertEqual(pizza.__str__(), "Pizza Reine (9€)")

    