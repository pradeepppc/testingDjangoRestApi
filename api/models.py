from django.db import models

# Create your models here.

class User(models.Model):
    """ Represents a user in the visa service"""
    email = models.EmailField(max_length = 255, unique=True)
    name = models.CharField(max_length = 255)
    cardNumber = models.CharField(max_length = 16, unique=True)
    password = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.email



class Restaurant(models.Model):
    """ Represents a Restaurants in the visa service """

    name = models.CharField(max_length = 255, unique=True)
    address = models.CharField(max_length = 255)
    cuisine = models.CharField(max_length = 255)
    expence = models.CharField(max_length = 255)
    offers = models.CharField(max_length = 255)
    waitTime = models.IntegerField()

    class Meta:
        get_latest_by = "waitTime"

    def __str__(self):
        return self.name


class Reservation(models.Model):
    """ This class represants the active reservations present in the visa service"""
    email = models.EmailField(max_length = 255)
    restaurant = models.CharField(max_length = 255)
    numberOfPeople = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return self.email + '-' + self.restaurant


class Invoice(models.Model):
    """ This is a invoice in visa service """
    itemName = models.CharField(max_length = 255)
    quantity = models.IntegerField()
    itemPrice = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return self.itemName
