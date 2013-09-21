from django.db import models

class Survey(models.Model):


class Question(models.Model):


class User(models.Model):
    facebook_id = models.CharField(max_length=200)

class Recipient(models.Model):
