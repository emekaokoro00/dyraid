from __future__ import unicode_literals
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.utils import timezone
from django.template.defaultfilters import default

# Create your models here.

DEFAULT_VALUE = 1
    
# class to simulate enum
class Meal_Size:
    VerySmall, Small, Medium, Large, VeryLarge = range(5)
    
@python_2_unicode_compatible # to support Python 2
class Meal_Type(models.Model):
    meal_type_name = models.CharField(max_length=100)
    description = models.CharField(max_length=50, default="Title")
    def __str__(self):
        return self.meal_type_name
        
@python_2_unicode_compatible
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50, default="Title")
    def __str__(self):
        return self.name
    
@python_2_unicode_compatible
class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_VALUE)
    food_name = models.CharField(max_length=100)
    food_type = models.ForeignKey(Meal_Type, on_delete=models.CASCADE, default=DEFAULT_VALUE)
    restaurant_offering = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=DEFAULT_VALUE)
    calories = models.IntegerField(default=0)
    def __str__(self):
        return self.food_name
    def get_absolute_url(self): # sets the default url to revert to after changes
        return reverse('meal:meal_detail', kwargs={'pk': self.pk})
