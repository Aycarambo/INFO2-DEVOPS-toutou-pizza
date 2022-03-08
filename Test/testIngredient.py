from django.test import TestCase
from restaurant.models import Ingredient


class IngredientTestCase(TestCase):
    def setUp(self) -> None:
        Ingredient.objects.create(name = "Farine de ble", allergen = True)

    def testIngredientAllergen(self):
        farine = Ingredient.objects.get(name = "Farine de ble")
        self.assertEqual(farine.__str__(), "Ingredient: Farine de ble (allergen: yes)")