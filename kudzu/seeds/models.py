from django.db import models

from kudzu.account.models import User


class Seed(models.Model):
    url = models.URLField()
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return "Seed %s" % self.id


def upload_to_question(instance, filename):
    return "kudzu/question/%s/%s.webm" % (str(instance.id)[0], instance.id)


class Question(models.Model):
    order = models.IntegerField(default=0)
    seed = models.ForeignKey(Seed)
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)
    video = models.FileField(upload_to=upload_to_question, max_length=255, blank=True, default='')


def upload_to_reply(instance, filename):
    return "kudzu/reply/%s/%s.webm" % (str(instance.id)[0], instance.id)


class Reply(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User, null=True)
    url = models.URLField(blank=True)
    video = models.FileField(upload_to=upload_to_reply, max_length=255, blank=True, default='')
