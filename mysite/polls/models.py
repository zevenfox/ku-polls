import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('ending date', null=True, default=timezone.now)

    def __str__(self):
        """Return questions."""
        return self.question_text

    def was_published_recently(self):
        """Return true if questions is published recently."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def is_published(self):
        """Return true if questions is published"""
        now = timezone.now()
        return self.pub_date <= now

    def can_vote(self):
        """Return true if questions can vote"""
        now = timezone.now()
        return self.pub_date <= now <= self.end_date



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Returns choices."""
        return self.choice_text

class Vote(models.Model):

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        """Return Votes"""
        return f"Vote by {self.user.username} for {self.choice.choice_text}"