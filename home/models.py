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
from django.template.defaultfilters import default

DEFAULT_VALUE = 1

# Create your models here.
    
# class to simulate enum
class User_Type(models.Model):
    end_user, restaurant, fitness_center = range(3)
 
@python_2_unicode_compatible # to support Python 2
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_VALUE)
    user_type = models.IntegerField(default=User_Type.end_user)
    check_comment = models.CharField(max_length=100)
#     def save(self, *args, **kwargs):
#         self.check_comment = 'check'
#         super(UserProfile, self).save(*args, **kwargs)
    def __str__(self):
        return self.user.name    
    def __unicode__(self):
        return unicode(self.user)
    def get_absolute_url(self): # sets the default url to revert to after changes
        return reverse('userlog:userlog_detail', kwargs={'pk': self.pk})
    
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

    
