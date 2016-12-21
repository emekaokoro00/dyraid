from django.test import TestCase

import datetime
from django.utils import timezone
from .models import Logger
# Create your tests here.

class LoggerMethodTests(TestCase):
    
    def test_logger_edited_recently_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_log = Logger(last_edit_date = time)
        self.assertIs(future_log.was_edited_recently(), False)
    
    def test_logger_edited_recently_morethan1day(self):
        time = timezone.now() - datetime.timedelta(days=2)
        old_log = Logger(last_edit_date = time)
        self.assertIs(old_log.was_edited_recently(), False)
    
    def test_logger_made_recently_lessthan1day(self):
        time = timezone.now() - datetime.timedelta(hours=4)
        recent_log = Logger(last_edit_date = time)
        self.assertIs(recent_log.was_edited_recently(), True)