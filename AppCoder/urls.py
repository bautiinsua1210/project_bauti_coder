from django.urls import path
from .views import *



urlpatterns = [
    path("client/", clients, name="clients"),
    path("car/", cars, name="cars"),
    path("service/", services, name="services"),
    path("", home, name="home"),

    path("clientForm/", clientForm, name="clientForm"),
    path("carForm/", carForm, name="carForm"),
    path("serviceForm/", serviceForm, name="serviceForm"),

    path("readClient/", readClient, name="readClient"),
    path("deleteClient/<id>", deleteClient, name="deleteClient"),
    path("clientEdit/<id>", clientEdit, name="clientEdit"),

    path("readCar/", readCar, name="readCar"),
    path("deleteCar/<id>", deleteCar, name="deleteCar"),
    path("carEdit/<id>", carEdit, name="carEdit"),

    path("readService/", readService, name="readService"),
    path("deleteService/<id>", deleteService, name="deleteService"),
    path("serviceEdit/<id>", serviceEdit, name="serviceEdit"),

    path("brandSearch/", brandSearch, name="brandSearch"),
    path("search/", search, name="search"),
]