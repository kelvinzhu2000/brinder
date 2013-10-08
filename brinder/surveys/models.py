from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

# The survey package. Essentially a wrapper to contain a set of questions
class Survey(models.Model):
    name = models.CharField(max_length=200)

# The individual survey questions
class NewQuestion(models.Model):
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
    question = models.ForeignKey(NewQuestion)
    message  = models.ForeignKey(Message)
    value    = models.IntegerField(default=0)
    comment  = models.TextField()
