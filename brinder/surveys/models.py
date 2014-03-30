from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# The survey package. Essentially a wrapper to contain a set of questions
class Survey(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

# The individual survey questions
class Question(models.Model):
    TRUEFALSE   = 'TF'
    DROPDOWN    = 'DD'
    ORDER       = 'O'
    EXPLANATION = 'E'
    RADIOBUTTON = 'RB'
    MULTIPLE    = 'M'

    QUESTION_TYPE_CHOICES = (
        (TRUEFALSE, 'True/False'),
        (DROPDOWN, 'Dropdown'),
        (ORDER, 'Ordering'),
        (EXPLANATION, 'Explanation'),
        (RADIOBUTTON, 'Radio Button'),
        (MULTIPLE, 'Choose Multiple'),
    )
    survey           = models.ForeignKey(Survey)
    rank             = models.IntegerField()
    question_text    = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

# The data for various kinds of survey questions
class TrueFalseQuestion(Question):
    question_type = models.CharField(max_length=2, default=Question.TRUEFALSE,
                                     editable=False)

class DropDownQuestion(Question):
    question_type = models.CharField(max_length=2, default=Question.DROPDOWN,
                                     editable=False)

class DropDownChoice(Choice):
    question    = models.ForeignKey(DropDownQuestion)

class OrderingQuestion(Question):
    question_type = models.CharField(max_length=2, default=Question.ORDER,
                                     editable=False)

class OrderingChoice(Choice):
    question    = models.ForeignKey(OrderingQuestion)

class ExplanationQuestion(Question):
    question_type = models.CharField(max_length=2, default=Question.EXPLANATION,
                                     editable=False)

class RadioButtonQuestion(Question):
    question_type = models.CharField(max_length=2, default=Question.RADIOBUTTON,
                                     editable=False)

class RadioButtonChoice(Choice):
    question = models.ForeignKey(RadioButtonQuestion)

class MultipleChoiceQuestion(Question):
    question_type = models.CharField(max_length=2, default=Question.MULTIPLE,
                                     editable=False)

class MultipleChoiceChoice(Choice):
    choice = models.ForeignKey(MultipleChoiceQuestion)

# The facebook id associated with a user
class FacebookId(models.Model):
    user        = models.OneToOneField(User)
    facebook_id = models.CharField(max_length=200)

# An individual sent out survey message from a user to a recipient.
class Message(models.Model):
    sender    = models.ForeignKey(User, related_name='sender')
    recipient_email = models.CharField(max_length=200)
    survey    = models.ForeignKey(Survey)
    status    = models.CharField(max_length=30)
    url       = models.SlugField(max_length=30)

# A recipient response to a survey question
class Answer(models.Model):
    question = models.ForeignKey(Question)
    message  = models.ForeignKey(Message)

    def __unicode__(self):
        return "%s, %s %s" % (self.question.question_text, self.message.recipient.first_name, self.message.recipient.last_name)

class TrueFalseAnswer(Answer):
    value = models.BooleanField()

class DropDownAnswer(Answer):
    value = models.ForeignKey(DropDownChoice)

class OrderingAnswer(Answer):
    value = models.TextField(null=False)

class OrderingChoiceRankings(models.Model):
    answer = models.ForeignKey(OrderingAnswer)
    choice = models.ForeignKey(OrderingChoice)
    value  = models.IntegerField()

class ExplanationAnswer(Answer):
    value = models.TextField()

class RadioButtonAnswer(Answer):
    value = models.ForeignKey(RadioButtonChoice)

class MultipleChoiceAnswer(Answer):
    value = models.ForeignKey(MultipleChoiceChoice)
