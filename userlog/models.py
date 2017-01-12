from __future__ import unicode_literals
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.utils import timezone

from home.models import Meal


# Create your models here.

@python_2_unicode_compatible # to support Python 2
class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    # log_time = models.DateTimeField('Time Logged')
    log_time = models.DateTimeField('Time Logged', default=timezone.now())
    comment = models.CharField(max_length=1000)
    def __str__(self):
        return "Entry " + self.log_time.strftime('%Y/%b/%d/ - %I:%M:%S')
    def __unicode__(self):
        return unicode(self.user)
    def get_absolute_url(self): # sets the default url to revert to after changes
        return reverse('userlog:userlog_detail', kwargs={'pk': self.pk})