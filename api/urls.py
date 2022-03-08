from django.urls import path

from api import views

app_name = "api"

urlpatterns = [

    path("pizzas", views.PizzaViewSet.as_view({"get": "list"})),
    path("pizza/<str:name>", views.PizzaViewSet.as_view({"get": "retrieve"})),

    path("restaurants", views.RestaurantViewSet.as_view({"get": "list"})),
    path("restaurant/<str:name>", views.RestaurantViewSet.as_view({"get": "retrieve"})),

    path("orders/<int:pk>", views.OrderViewSet.as_view(
        {"get": "retrieve", "post": "create", "delete": "destroy", "put": "update"}
    ))
]
