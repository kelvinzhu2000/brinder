from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.

# The survey package. Essentially a wrapper to contain a set of questions
class Survey(models.Model):
    name = models.CharField(max_length=200)

# The individual survey questions
class Question(models.Model):
    TRUEFALSE   = 'TF'
    DROPDOWN    = 'DD'
    EXPLANATION = 'E'
    RADIOBUTTON = 'RB'
    MULTIPLE    = 'M'

    QUESTION_TYPE_CHOICES = (
        (TRUEFALSE, 'True/False'),
        (DROPDOWN, 'Dropdown'),
        (EXPLANATION, 'Explanation'),
        (RADIOBUTTON, 'Radio Button'),
        (MULTIPLE, 'Choose Multiple'),
    )
    survey       = models.ForeignKey(Survey)
    rank         = models.IntegerField()
    question     = models.CharField(max_length=200)
    question_type = models.CharField(max_length=2,
                                     choices=QUESTION_TYPE_CHOICES,
                                     default=TRUEFALSE)

# The facebook id associated with a user
class FacebookId(models.Model):
    user        = models.OneToOneField(User)
    facebook_id = models.CharField(max_length=200)

# An individual sent out survey message from a user to a recipient.
class Message(models.Model):
    sender    = models.ForeignKey(User, related_name='sender')
    recipient = models.ForeignKey(User, related_name='recipient')
    survey    = models.ForeignKey(Survey)
    status    = models.CharField(max_length=30)
    url       = models.SlugField(max_length=30)

# A recipient response to a survey question
class Answer(models.Model):
    question = models.ForeignKey(Question)
    message  = models.ForeignKey(Message)
    value    = models.IntegerField(default=0)
    comment  = models.TextField()
