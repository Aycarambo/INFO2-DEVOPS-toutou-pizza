from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.constraints import UniqueConstraint


class Address(models.Model):
    nb = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True
    )
    street = models.CharField(max_length=250)
    zipcode = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    city = models.CharField(max_length=50)
    complement = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = "address"

    def __str__(self):
        return f"{self.nb}, {self.street} ({self.complement}) - {self.city} ({self.zipcode})"


class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = "restaurant"
        constraints = [
            UniqueConstraint(fields=["name", "address"], name="unq_restaurant")
        ]

    def __str__(self):
        return f"{self.name} at {self.address}"


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    allergen = models.BooleanField(default=False)

    class Meta:
        db_table = "ingredient"

    def __str__(self):
        return f"Ingredient: {self.name} (allergen: {'yes' if self.allergen else 'no'})"


class Pizza(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    ingredients = models.ManyToManyField(Ingredient)

    class Meta:
        db_table = "pizza"

    def __str__(self):
        return f"Pizza {self.name} ({self.price}€)"
