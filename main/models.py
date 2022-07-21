from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


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


class ContactBook(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(Contact, related_name='book')

    def __str__(self):
        return f"{self.owner}'s Contact Book"
