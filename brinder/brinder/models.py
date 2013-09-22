from django.db import models
from django.contrib.auth.models import User

# The survey package. Essentially a wrapper to contain a set of questions
class Survey(models.Model):
    name = models.CharField(max_length=200)

# The individual survey questions
class Question(models.Model):
    survey   = models.ForeignKey(Survey)
    question = models.CharField(max_length=200)

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

# A recipient response to a survey question
class Answer(models.Model):
    question = models.ForeignKey(Question)
    message  = models.ForeignKey(Message)
    value    = models.IntegerField(default=0)
    comment  = models.TextField()
