"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.contrib.auth.models import User
from models import Survey, Message
from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_message(self):
        senderName = "chaoyan"
        names = ['aceyan', 'hyperyan'];
        emails = ['aceyan8996@gmail.com', 'chaoyanla@gmail.com']
        
        #new_sender = User.objects.get(username=senderName)
        new_sender = User.objects.all()[0]
        for name, email_addr in zip(names, emails):
            cur_survey = Survey.objects.all()[0]
            msg = Message(sender=new_sender, recipient_email=email_addr, survey=cur_survey, status="default", url=randomUrl)
            msg.save()

    def runTest(self):
        test_message()


