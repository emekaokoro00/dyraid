from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import ModelForm
from django.forms import forms
from unittest.util import _MAX_LENGTH
from django.utils import timezone
import datetime

# Create your models here.
@python_2_unicode_compatible # to support Python 2
class Logger(models.Model): #{
    last_edit_date = models.DateTimeField('Last Date Edited')
    title = models.CharField(max_length=100, default="Title")
    entry = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    # testNum = models.IntegerField(default=0)
    def __str__(self):
        return self.title    
    def was_edited_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.last_edit_date <= now
#}
    
@python_2_unicode_compatible # to support Python 2
class Meal_Type(models.Model):
    meal_type_name = models.CharField(max_length=100)
    description = models.CharField(max_length=50, default="Title")
    def __str__(self):
        return self.meal_type_name

@python_2_unicode_compatible # to support Python 2
class Meal(models.Model):
    food_name = models.CharField(max_length=100)
    food_type = models.ForeignKey(Meal_Type, on_delete=models.CASCADE)
    calories = models.IntegerField(default=0)
    def __str__(self):
        return self.food_name
    def get_absolute_url(self): # sets the default url to revert to after changes
        return reverse('home:meal_detail', kwargs={'pk': self.pk})
    
