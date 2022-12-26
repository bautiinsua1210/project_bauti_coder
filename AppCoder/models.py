from django.db import models


class Client(models.Model):
    name= models.CharField(max_length=50)
    surname= models.CharField(max_length=50)
    email= models.EmailField()
    role= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname} {self.email} {self.role}"

class Car(models.Model):
    brand= models.CharField(max_length=50)
    model= models.CharField(max_length=50)
    year= models.IntegerField()
    mile= models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} {self.year} {self.mile}"

class Service(models.Model):
    type= models.CharField(max_length=50)
    time= models.IntegerField()
    price= models.IntegerField()

    def __str__(self):
        return f"{self.type} {self.time} {self.price}"




