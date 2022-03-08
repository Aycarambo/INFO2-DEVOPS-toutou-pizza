from django.db import models

from restaurant.models import Pizza, Address


class Client(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)

    class Meta:
        db_table = "client"

    def __str__(self):
        return f"{self.name} ({self.email})"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    delivery_hour = models.DateTimeField()
    created = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name="Order time", null=True
    )

    class Meta:
        db_table = "order"

    def __str__(self):
        return f"Order for {self.client.name} at {self.delivery_hour}, {self.address}"
