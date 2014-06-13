from django.db import models

from kudzu.account.models import User


class Seed(models.Model):
    url = models.URLField()
    user = models.ForeignKey(User)


def upload_to(instance, filename):
    return "kudzu/%s/%s.webm" % (str(instance.id)[0], instance.id)


class Question(models.Model):
    order = models.IntegerField(default=0)
    seed = models.ForeignKey(Seed)
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)
    video = models.FileField(upload_to=upload_to, max_length=255, blank=True, default='')


class Reply(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    url = models.URLField()
