from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import ModelForm
from django.forms import forms
from django.utils import timezone
from django.template.defaultfilters import default

import datetime
from unittest.util import _MAX_LENGTH
from enum import Enum

DEFAULT_VALUE = 1

# Create your models here.
    
# class to simulate enum
class User_Type(Enum):
    End_User = 0
    Restaurant = 1
    Fitness_Center = 2
     
class Sex(Enum):
    Female = 0
    Male = 1
 
@python_2_unicode_compatible # to support Python 2
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_VALUE)
    date_of_birth = models.DateTimeField('Date of Birth', default=timezone.now)
    sex_type = models.IntegerField(default=Sex.Female.value)
    user_type = models.IntegerField(default=User_Type.End_User.value)
    check_comment = models.CharField(max_length=100)
#     def save(self, *args, **kwargs):
#         self.check_comment = 'check'
#         super(UserProfile, self).save(*args, **kwargs)
    def __str__(self):
        return self.user.name    
    def __unicode__(self):
        return unicode(self.user)
    def get_absolute_url(self): # sets the default url to revert to after changes
        return reverse('home:userprofile_detail', kwargs={'pk': self.user.pk})
    
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

    
