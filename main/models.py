from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    ingredients = models.ManyToManyField("Object")

    def __str__(self):
        return f'{self.name} -- {self.quantity}'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} -- {self.phone}'
