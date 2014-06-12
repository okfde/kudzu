from django.db import models

from kudzu.account.models import User


class Seed(models.Model):
    url = models.URLField()
    user = models.ForeignKey(User)


class Question(models.Model):
    seed = models.ForeignKey(Seed)
    text = models.TextField()


class Reply(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    url = models.URLField()
